# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/panel/run_Path_Track.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(521, 492))
        Dialog.setMaximumSize(QtCore.QSize(521, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bezier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.mainPanel = QtWidgets.QWidget(Dialog)
        self.mainPanel.setObjectName("mainPanel")
        self.mainPanelLayout = QtWidgets.QHBoxLayout(self.mainPanel)
        self.mainPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPanelLayout.setObjectName("mainPanelLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.mainPanel)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.allShafts = QtWidgets.QRadioButton(self.mainPanel)
        self.allShafts.setChecked(False)
        self.allShafts.setObjectName("allShafts")
        self.verticalLayout_4.addWidget(self.allShafts)
        self.chooseShafts = QtWidgets.QRadioButton(self.mainPanel)
        self.chooseShafts.setChecked(True)
        self.chooseShafts.setObjectName("chooseShafts")
        self.verticalLayout_4.addWidget(self.chooseShafts)
        self.shaftsScrollArea = QtWidgets.QScrollArea(self.mainPanel)
        self.shaftsScrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shaftsScrollArea.sizePolicy().hasHeightForWidth())
        self.shaftsScrollArea.setSizePolicy(sizePolicy)
        self.shaftsScrollArea.setMinimumSize(QtCore.QSize(150, 0))
        self.shaftsScrollArea.setWidgetResizable(True)
        self.shaftsScrollArea.setObjectName("shaftsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 148, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.shaftsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.shaftsScrollArea)
        self.mainPanelLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.mainPanel)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Point_list = QtWidgets.QListWidget(self.mainPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Point_list.sizePolicy().hasHeightForWidth())
        self.Point_list.setSizePolicy(sizePolicy)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.mainPanelLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QToolButton(self.mainPanel)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.remove_botton = QtWidgets.QToolButton(self.mainPanel)
        self.remove_botton.setObjectName("remove_botton")
        self.verticalLayout.addWidget(self.remove_botton)
        self.mainPanelLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.mainPanel)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.Run_list = QtWidgets.QListWidget(self.mainPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Run_list.sizePolicy().hasHeightForWidth())
        self.Run_list.setSizePolicy(sizePolicy)
        self.Run_list.setObjectName("Run_list")
        self.verticalLayout_3.addWidget(self.Run_list)
        self.mainPanelLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.mainPanel)
        self.subPanel = QtWidgets.QWidget(Dialog)
        self.subPanel.setObjectName("subPanel")
        self.subPanelLayout = QtWidgets.QHBoxLayout(self.subPanel)
        self.subPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.subPanelLayout.setObjectName("subPanelLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.subPanelLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.subPanel)
        self.label_4.setObjectName("label_4")
        self.subPanelLayout.addWidget(self.label_4)
        self.Resolution = QtWidgets.QDoubleSpinBox(self.subPanel)
        self.Resolution.setMinimum(0.5)
        self.Resolution.setMaximum(45.0)
        self.Resolution.setSingleStep(0.5)
        self.Resolution.setProperty("value", 5.0)
        self.Resolution.setObjectName("Resolution")
        self.subPanelLayout.addWidget(self.Resolution)
        self.verticalLayout_5.addWidget(self.subPanel)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_5.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Path Track"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose these points to execution path simulation.</span></p><p><span style=\" font-size:12pt;\">Active element will be operational in order.</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Shaft(s):</span></p></body></html>"))
        self.allShafts.setText(_translate("Dialog", "All"))
        self.chooseShafts.setText(_translate("Dialog", "Let me Choose:"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Point(s):</span></p></body></html>"))
        self.add_button.setText(_translate("Dialog", ">"))
        self.remove_botton.setText(_translate("Dialog", "<"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Track Point(s):</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Resolution:"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

