# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/io/workbook_overview.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 544)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setObjectName("toolBox")
        self.page0 = QtWidgets.QWidget()
        self.page0.setGeometry(QtCore.QRect(0, 0, 424, 329))
        self.page0.setObjectName("page0")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.storage_label = QtWidgets.QLabel(self.page0)
        self.storage_label.setObjectName("storage_label")
        self.verticalLayout_2.addWidget(self.storage_label)
        self.storage_list = QtWidgets.QListWidget(self.page0)
        self.storage_list.setObjectName("storage_list")
        self.verticalLayout_2.addWidget(self.storage_list)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/mechanism.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page0, icon, "")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 424, 329))
        self.page1.setObjectName("page1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.variables_label = QtWidgets.QLabel(self.page1)
        self.variables_label.setObjectName("variables_label")
        self.verticalLayout_3.addWidget(self.variables_label)
        self.variables_list = QtWidgets.QListWidget(self.page1)
        self.variables_list.setObjectName("variables_list")
        self.verticalLayout_3.addWidget(self.variables_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.records_label = QtWidgets.QLabel(self.page1)
        self.records_label.setObjectName("records_label")
        self.verticalLayout_4.addWidget(self.records_label)
        self.records_list = QtWidgets.QListWidget(self.page1)
        self.records_list.setObjectName("records_list")
        self.verticalLayout_4.addWidget(self.records_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page1, icon1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setGeometry(QtCore.QRect(0, 0, 424, 329))
        self.page2.setObjectName("page2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.structures_label = QtWidgets.QLabel(self.page2)
        self.structures_label.setObjectName("structures_label")
        self.verticalLayout_6.addWidget(self.structures_label)
        self.structures_list = QtWidgets.QListWidget(self.page2)
        self.structures_list.setObjectName("structures_list")
        self.verticalLayout_6.addWidget(self.structures_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.triangular_iteration_label = QtWidgets.QLabel(self.page2)
        self.triangular_iteration_label.setObjectName("triangular_iteration_label")
        self.verticalLayout_5.addWidget(self.triangular_iteration_label)
        self.triangular_iteration_list = QtWidgets.QListWidget(self.page2)
        self.triangular_iteration_list.setObjectName("triangular_iteration_list")
        self.verticalLayout_5.addWidget(self.triangular_iteration_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page2, icon2, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setGeometry(QtCore.QRect(0, 0, 424, 329))
        self.page3.setObjectName("page3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.results_label = QtWidgets.QLabel(self.page3)
        self.results_label.setObjectName("results_label")
        self.verticalLayout_7.addWidget(self.results_label)
        self.results_list = QtWidgets.QListWidget(self.page3)
        self.results_list.setObjectName("results_list")
        self.verticalLayout_7.addWidget(self.results_list)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page3, icon3, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.storage_label.setText(_translate("Dialog", "Storage:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page0), _translate("Dialog", "Mechanism"))
        self.variables_label.setText(_translate("Dialog", "Variables:"))
        self.records_label.setText(_translate("Dialog", "Records:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page1), _translate("Dialog", "Inputs"))
        self.structures_label.setText(_translate("Dialog", "Structures:"))
        self.triangular_iteration_label.setText(_translate("Dialog", "Triangular iteration:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), _translate("Dialog", "Collections"))
        self.results_label.setText(_translate("Dialog", "Results:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page3), _translate("Dialog", "Dimensional Synthesis"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

