# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(400, 300)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtWidgets.QTabWidget(Preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_general)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_general)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.preferences_options_general_browser_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_browser_value.setObjectName("preferences_options_general_browser_value")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_browser_value)
        self.preferences_options_general_process_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_process_value.setObjectName("preferences_options_general_process_value")
        self.preferences_options_general_process_value.addItem("")
        self.preferences_options_general_process_value.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_process_value)
        self.label_2 = QtWidgets.QLabel(self.tab_general)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout.addLayout(self.formLayout)
        self.tabs.addTab(self.tab_general, "")
        self.verticalLayout.addWidget(self.tabs, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Preferences)
        self.tabs.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.tabs, self.preferences_options_general_browser_value)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.label.setText(_translate("Preferences", "Select the browser to be used"))
        self.preferences_options_general_browser_value.setItemText(0, _translate("Preferences", "pyqt5"))
        self.preferences_options_general_browser_value.setItemText(1, _translate("Preferences", "firefox"))
        self.preferences_options_general_browser_value.setItemText(2, _translate("Preferences", "safari"))
        self.preferences_options_general_process_value.setToolTip(_translate("Preferences", "If qt, stdout and stderr are shown in the GUI. If unix shell, snakemake output is kept in the parent unix shell."))
        self.preferences_options_general_process_value.setItemText(0, _translate("Preferences", "qt"))
        self.preferences_options_general_process_value.setItemText(1, _translate("Preferences", "unix shell"))
        self.label_2.setText(_translate("Preferences", "Process runner "))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_general), _translate("Preferences", "General"))

