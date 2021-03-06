# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Mechanical Synthesis System. 
##Copyright (C) 2016-2018 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from core.QtModules import *
from core.graphics import PreviewCanvas, edges_view
from core.io import get_from_parenthesis, get_front_of_parenthesis
import pprint
from math import sqrt
from networkx import Graph
from string import ascii_uppercase
from itertools import product
'''
'CollectionsDialog',
'ConstraintsDialog',
'CustomsDialog',
'TargetsDialog',
'SolutionsDialog',
'list_texts',
'combo_texts',
'''
from .TriangularIteration_dialog import *
from .Ui_TriangularIteration import Ui_Form

#This is a generator to get a non-numeric and non-repeat name string.
#('A', 'B', ..., 'AA', 'AB', ..., 'AAA', 'AAB', ...)
def letter_names():
    i = 0
    while True:
        i += 1
        for e in product(ascii_uppercase, repeat=i):
            yield ''.join(e)

class PreviewWindow(PreviewCanvas):
    set_joint_number = pyqtSignal(int)
    
    def __init__(self, get_solutions_func, parent):
        super(PreviewWindow, self).__init__(get_solutions_func, parent)
        self.pressed = False
        self.get_joint_number = parent.joint_name.currentIndex
    
    def mousePressEvent(self, event):
        mx = (event.x() - self.ox) / self.zoom
        my = (event.y() - self.oy) / -self.zoom
        for node, (x, y) in self.pos.items():
            if node in self.same:
                continue
            if sqrt((mx - x)**2 + (my - y)**2)<=5:
                self.set_joint_number.emit(node)
                self.pressed = True
                break
    
    def mouseReleaseEvent(self, event):
        self.pressed = False
    
    def mouseMoveEvent(self, event):
        if self.pressed:
            row = self.get_joint_number()
            if row>-1:
                mx = (event.x() - self.ox) / self.zoom
                my = (event.y() - self.oy) / -self.zoom
                if -120 <= mx <= 120:
                    self.pos[row] = (mx, self.pos[row][1])
                else:
                    self.pos[row] = (120 if -120 <= mx else -120, self.pos[row][1])
                if -120 <= my <= 120:
                    self.pos[row] = (self.pos[row][0], my)
                else:
                    self.pos[row] = (self.pos[row][0], 120 if -120 <= my else -120)
                self.update()

warning_icon = "<img width=\"15\" src=\":/icons/warning.png\"/> "

class CollectionsTriangularIteration(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(CollectionsTriangularIteration, self).__init__(parent)
        self.setupUi(self)
        self.unsaveFunc = parent.workbookNoSave
        '''
        self.addToCollection = CollectionsStructure.addCollection
        '''
        self.collections = {}
        self.parm_bind = {}
        #Canvas
        self.PreviewWindow = PreviewWindow(
            lambda: tuple(
                self.Expression_list.item(row).text()
                for row in range(self.Expression_list.count())
            ),
            self
        )
        self.PreviewWindow.set_joint_number.connect(self.joint_name.setCurrentIndex)
        self.main_layout.insertWidget(0, self.PreviewWindow)
        self.show_solutions.clicked.connect(self.PreviewWindow.setShowSolutions)
        #Signals
        self.joint_name.currentIndexChanged.connect(self.hasSolution)
        self.Expression_list.itemChanged.connect(self.set_parm_bind)
        self.clear()
    
    def addCollections(self, collections):
        self.collections.update(collections)
    
    def clear(self):
        self.collections.clear()
        self.clearPanel()
    
    def clearPanel(self):
        self.profile_name = ""
        self.PreviewWindow.clear()
        self.joint_name.clear()
        self.Expression_list.clear()
        self.parm_bind.clear()
        self.grounded_list.clear()
        self.Driver_list.clear()
        self.Follower_list.clear()
        self.Target_list.clear()
        self.constraint_list.clear()
        self.Link_Expression.clear()
        self.Expression.clear()
        for label in [
            self.Expression_list_label,
            self.grounded_label,
            self.Driver_label,
            self.Follower_label,
            self.Target_label
        ]:
            self.setWarning(label, True)
    
    @pyqtSlot()
    def on_clear_button_clicked(self):
        reply = QMessageBox.question(self, "New profile",
            "Triangular iteration should be added structure diagrams from structure collections.\n"+
            "Do you want to create a new profile?",
            (QMessageBox.Yes | QMessageBox.No),
            QMessageBox.Yes
        )
        if reply==QMessageBox.Yes:
            self.clearPanel()
    
    def setWarning(self, label, warning: bool):
        label.setText(label.text().replace(warning_icon, ''))
        if warning:
            label.setText(warning_icon + label.text())
    
    @pyqtSlot()
    def on_addToCollection_button_clicked(self):
        self.addToCollection(tuple(self.PreviewWindow.G.edges))
    
    @pyqtSlot(Graph, dict)
    def setGraph(self, G, pos):
        self.clear()
        self.PreviewWindow.setGraph(G, pos)
        for link in G.nodes:
            self.grounded_list.addItem("({})".format(", ".join(
                'P{}'.format(n)
                for n, edge in edges_view(G) if link in edge
            )))
        #Point name as (P1, P2, P3, ...).
        for node in pos:
            self.joint_name.addItem('P{}'.format(node))
    
    @pyqtSlot(int)
    def on_grounded_list_currentRowChanged(self, row):
        self.setWarning(self.grounded_label, not row>-1)
        self.PreviewWindow.setGrounded(row)
        self.hasSolution()
        self.Expression_list.clear()
        self.Expression.clear()
        self.Follower_list.clear()
        self.Driver_list.clear()
        if row>-1:
            self.Follower_list.addItems(
                self.grounded_list.currentItem().text()
                .replace('(', '')
                .replace(')', '')
                .split(", ")
            )
        self.setWarning(self.Follower_label, not row>-1)
        self.setWarning(self.Driver_label, True)
        self.setWarning(self.Expression_list_label, True)
    
    @pyqtSlot(int)
    def hasSolution(self, index=None):
        if index is None:
            index = self.joint_name.currentIndex()
        if index>-1:
            status = self.PreviewWindow.getStatus(index)
            if not status:
                status_str = "Not known."
            elif index in self.PreviewWindow.same:
                status_str = "Same as P{}.".format(self.PreviewWindow.same[index])
            else:
                status_str = "Grounded."
                for expr in list_texts(self.Expression_list):
                    if index==int(get_from_parenthesis(expr, '(', ')').replace('P', '')):
                        status_str = "From {}.".format(
                            get_front_of_parenthesis(expr, '[')
                        )
            self.status.setText(status_str)
            self.PLAP_solution.setEnabled(not status)
            self.PLLP_solution.setEnabled(not status)
        else:
            self.status.setText("N/A")
            self.PLAP_solution.setEnabled(False)
            self.PLLP_solution.setEnabled(False)
    
    @pyqtSlot()
    def on_add_customization_clicked(self):
        dlg = CustomsDialog(self)
        dlg.show()
        dlg.exec_()
        self.PreviewWindow.update()
    
    @pyqtSlot()
    def on_Driver_add_clicked(self):
        row = self.Follower_list.currentRow()
        if row>-1:
            self.Driver_list.addItem(self.Follower_list.takeItem(row))
            self.setWarning(self.Driver_label, False)
    
    @pyqtSlot()
    def on_Follower_add_clicked(self):
        row = self.Driver_list.currentRow()
        if row>-1:
            self.Follower_list.addItem(self.Driver_list.takeItem(row))
            self.setWarning(self.Driver_label, not bool(self.Driver_list.count()))
    
    def expression(self):
        expr_list = set([])
        for expr in self.Expression.text().split(';'):
            param_list = get_from_parenthesis(expr, '[', ']').split(',')
            param_list.append(get_from_parenthesis(expr, '(', ')'))
            expr_list.update(param_list)
        return expr_list
    
    def getParam(self, angle: bool =False) -> int:
        i = 0
        p = '{}{{}}'.format('a' if angle else 'L')
        while p.format(i) in self.expression():
            i += 1
        return i
    
    def get_currentMechanismParams(self) -> dict:
        self.set_parm_bind()
        return {
            #To keep the origin graph.
            'Graph':tuple(self.PreviewWindow.G.edges),
            #To keep the position of points.
            'pos':self.PreviewWindow.pos.copy(),
            'cus':self.PreviewWindow.cus.copy(),
            'same':self.PreviewWindow.same.copy(),
            'name_dict':{v:k for k, v in self.parm_bind.items()},
            #Mechanism params.
            'Driver':{
                self.parm_bind[s]:None for s in list_texts(self.Driver_list)
                if not self.PreviewWindow.name_in_same(s)
            },
            'Follower':{
                self.parm_bind[s]:None for s in list_texts(self.Follower_list)
                if not self.PreviewWindow.name_in_same(s)
            },
            'Target':{
                self.parm_bind[s]:None for s in list_texts(self.Target_list)
            },
            'Link_Expression':self.Link_Expression.text(),
            'Expression':self.Expression.text(),
            'constraint':[tuple(
                self.parm_bind[name] for name in s.split(", ")
            ) for s in list_texts(self.constraint_list)]
        }
    
    @pyqtSlot()
    def on_load_button_clicked(self):
        dlg = CollectionsDialog(self)
        dlg.show()
        if dlg.exec_():
            params = dlg.mechanismParams
            mapping = params['name_dict']
            #Add customize joints.
            G = Graph(params['Graph'])
            self.setGraph(G, params['pos'])
            self.PreviewWindow.cus = params['cus']
            self.PreviewWindow.same = params['same']
            #Grounded setting.
            Driver = [mapping[e] for e in params['Driver']]
            Follower = [mapping[e] for e in params['Follower']]
            for row, link in enumerate(G.nodes):
                points = set(
                    'P{}'.format(n)
                    for n, edge in edges_view(G) if link in edge
                )
                if set(Driver + Follower) <= points:
                    self.grounded_list.setCurrentRow(row)
                    break
            #Driver, Follower, Target
            for row in reversed(range(self.Follower_list.count())):
                if self.Follower_list.item(row).text() in Driver:
                    self.Follower_list.setCurrentRow(row)
                    self.Driver_add.click()
            self.Target_list.addItems([mapping[e] for e in params['Target']])
            self.setWarning(self.Target_label, not self.Target_list.count()>0)
            #Constraints
            self.constraint_list.addItems([
                ", ".join(mapping[e] for e in c) for c in params['constraint']
            ])
            #Expression
            for expr in params['Expression'].split(';'):
                params = get_from_parenthesis(expr, '[', ']').split(',')
                target = get_from_parenthesis(expr, '(', ')')
                params.append(target)
                for p in params:
                    try:
                        #Try to avoid replace function name.
                        expr = mapping[p].join(expr.rsplit(p, 1))
                    except KeyError:
                        continue
                item = QListWidgetItem()
                self.Expression_list.addItem(item)
                item.setText(expr)
                self.PreviewWindow.setStatus(mapping[target], True)
            self.setWarning(self.Expression_list_label, not self.PreviewWindow.isAllLock())
    
    @pyqtSlot()
    def on_constraints_button_clicked(self):
        dlg = ConstraintsDialog(self)
        dlg.show()
        if dlg.exec_():
            self.constraint_list.clear()
            for constraint in list_texts(dlg.main_list):
                self.constraint_list.addItem(constraint)
    
    @pyqtSlot()
    def on_Target_button_clicked(self):
        dlg = TargetsDialog(self)
        dlg.show()
        if dlg.exec_():
            self.Target_list.clear()
            for target in list_texts(dlg.targets_list):
                self.Target_list.addItem(target)
            self.setWarning(self.Target_label, not self.Target_list.count()>0)
    
    @pyqtSlot()
    def on_PLAP_solution_clicked(self):
        dlg = SolutionsDialog('PLAP', self)
        dlg.show()
        if dlg.exec_():
            point = self.joint_name.currentText()
            item = QListWidgetItem()
            self.Expression_list.addItem(item)
            item.setText("PLAP[{},{},{},{}]({})".format(
                dlg.point_A.currentText(),
                'L{}'.format(self.getParam()),
                'a{}'.format(self.getParam(angle=True)),
                dlg.point_B.currentText(),
                point
            ))
            self.PreviewWindow.setStatus(point, True)
            self.hasSolution()
            self.setWarning(self.Expression_list_label, not self.PreviewWindow.isAllLock())
    
    @pyqtSlot()
    def on_PLLP_solution_clicked(self):
        dlg = SolutionsDialog('PLLP', self)
        dlg.show()
        if dlg.exec_():
            point = self.joint_name.currentText()
            link_num = self.getParam()
            item = QListWidgetItem()
            self.Expression_list.addItem(item)
            item.setText("PLLP[{},{},{},{}]({})".format(
                dlg.point_A.currentText(),
                'L{}'.format(link_num),
                'L{}'.format(link_num + 1),
                dlg.point_B.currentText(),
                point
            ))
            self.PreviewWindow.setStatus(point, True)
            self.hasSolution()
            self.setWarning(self.Expression_list_label, not self.PreviewWindow.isAllLock())
    
    @pyqtSlot(QListWidgetItem)
    def set_parm_bind(self, item=None):
        self.parm_bind.clear()
        expr_list = []
        #At this time, we should turn the points number to letter names.
        ln = letter_names()
        #Set functional expression.
        for expr in list_texts(self.Expression_list):
            params = get_from_parenthesis(expr, '[', ']').split(',')
            params.append(get_from_parenthesis(expr, '(', ')'))
            for name in params:
                if 'P' in name:
                    #Find out with who was shown earlier.
                    if name not in self.parm_bind:
                        self.parm_bind[name] = next(ln)
                    expr = expr.replace(name, self.parm_bind[name])
            expr_list.append(expr)
        #If there has any joints not named yet.
        for name in combo_texts(self.joint_name):
            if name not in self.parm_bind:
                self.parm_bind[name] = next(ln)
        #Set link expression.
        link_expr_list = []
        self.Expression.setText(';'.join(expr_list))
        for row, gs in list_texts(self.grounded_list, True):
            try:
                link_expr = []
                #Links from grounded list.
                for name in gs.replace('(', '').replace(')', '').split(", "):
                    if self.PreviewWindow.name_in_same(name):
                        name = 'P{}'.format(self.PreviewWindow.same[int(name.replace('P', ''))])
                    link_expr.append(self.parm_bind[name])
            except KeyError:
                continue
            else:
                #Customize joints.
                for joint, link in self.PreviewWindow.cus.items():
                    if row==link:
                        link_expr.append(self.parm_bind[joint])
                link_expr_str = ','.join(sorted(set(link_expr)))
                if row==self.grounded_list.currentRow():
                    link_expr_list.insert(0, link_expr_str)
                else:
                    link_expr_list.append(link_expr_str)
        self.Link_Expression.setText(';'.join(
            ('ground' if i==0 else '') + "[{}]".format(link)
            for i, link in enumerate(link_expr_list)
        ))
    
    @pyqtSlot()
    def on_Expression_pop_clicked(self):
        count = self.Expression_list.count()
        if count:
            expr = self.Expression_list.item(count-1).text()
            self.Expression_list.takeItem(count-1)
            self.PreviewWindow.setStatus(get_from_parenthesis(expr, '(', ')'), False)
            self.set_parm_bind()
    
    @pyqtSlot()
    def on_Expression_clear_clicked(self):
        self.PreviewWindow.setGrounded(self.grounded_list.currentRow())
        self.Expression_list.clear()
        self.Expression.clear()
        self.hasSolution()
    
    @pyqtSlot()
    def on_save_button_clicked(self):
        if self.profile_name:
            name = self.profile_name
            ok = True
        else:
            name, ok = QInputDialog.getText(self, "Profile name", "Please enter the profile name:")
        if ok:
            i = 0
            while (name not in self.collections) and (not name):
                name = "Structure_{}".format(i)
            self.collections[name] = self.get_currentMechanismParams()
            self.profile_name = name
            self.unsaveFunc()
    
    @pyqtSlot()
    def on_clipboard_button_clicked(self):
        QApplication.clipboard().setText(pprint.pformat(self.get_currentMechanismParams()))
