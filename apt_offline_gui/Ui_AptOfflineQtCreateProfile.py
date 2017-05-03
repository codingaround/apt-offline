# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtCreateProfile.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateProfile(object):
    def setupUi(self, CreateProfile):
        CreateProfile.setObjectName("CreateProfile")
        CreateProfile.setWindowModality(QtCore.Qt.ApplicationModal)
        CreateProfile.resize(443, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateProfile.sizePolicy().hasHeightForWidth())
        CreateProfile.setSizePolicy(sizePolicy)
        CreateProfile.setMinimumSize(QtCore.QSize(443, 400))
        CreateProfile.setMaximumSize(QtCore.QSize(443, 500))
        CreateProfile.setFocusPolicy(QtCore.Qt.NoFocus)
        self.srcBuildDeps = QtWidgets.QCheckBox(CreateProfile)
        self.srcBuildDeps.setEnabled(False)
        self.srcBuildDeps.setGeometry(QtCore.QRect(11, 230, 131, 25))
        self.srcBuildDeps.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.srcBuildDeps.setObjectName("srcBuildDeps")
        self.aptBackendComboBox = QtWidgets.QComboBox(CreateProfile)
        self.aptBackendComboBox.setGeometry(QtCore.QRect(164, 276, 110, 30))
        self.aptBackendComboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.aptBackendComboBox.setObjectName("aptBackendComboBox")
        self.aptBackendComboBox.addItem("")
        self.aptBackendComboBox.addItem("")
        self.aptBackendComboBox.addItem("")
        self.upgradeTaskComboBox = QtWidgets.QComboBox(CreateProfile)
        self.upgradeTaskComboBox.setEnabled(False)
        self.upgradeTaskComboBox.setGeometry(QtCore.QRect(330, 276, 100, 30))
        self.upgradeTaskComboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.upgradeTaskComboBox.setObjectName("upgradeTaskComboBox")
        self.upgradeTaskComboBox.addItem("")
        self.upgradeTaskComboBox.addItem("")
        self.upgradeTaskComboBox.addItem("")
        self.targetReleaseCheckBox = QtWidgets.QCheckBox(CreateProfile)
        self.targetReleaseCheckBox.setEnabled(False)
        self.targetReleaseCheckBox.setGeometry(QtCore.QRect(11, 123, 143, 25))
        self.targetReleaseCheckBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetReleaseCheckBox.setObjectName("targetReleaseCheckBox")
        self.targetReleaseTextInput = QtWidgets.QLineEdit(CreateProfile)
        self.targetReleaseTextInput.setEnabled(False)
        self.targetReleaseTextInput.setGeometry(QtCore.QRect(164, 121, 265, 30))
        self.targetReleaseTextInput.setMinimumSize(QtCore.QSize(0, 30))
        self.targetReleaseTextInput.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetReleaseTextInput.setReadOnly(False)
        self.targetReleaseTextInput.setClearButtonEnabled(True)
        self.targetReleaseTextInput.setObjectName("targetReleaseTextInput")
        self.label = QtWidgets.QLabel(CreateProfile)
        self.label.setGeometry(QtCore.QRect(290, 281, 40, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CreateProfile)
        self.label_2.setGeometry(QtCore.QRect(62, 281, 100, 20))
        self.label_2.setObjectName("label_2")
        self.generateChangelog = QtWidgets.QCheckBox(CreateProfile)
        self.generateChangelog.setEnabled(False)
        self.generateChangelog.setGeometry(QtCore.QRect(160, 230, 111, 25))
        self.generateChangelog.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.generateChangelog.setObjectName("generateChangelog")
        self.cancelButton = QtWidgets.QPushButton(CreateProfile)
        self.cancelButton.setGeometry(QtCore.QRect(224, 451, 100, 32))
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.createProfileButton = QtWidgets.QPushButton(CreateProfile)
        self.createProfileButton.setEnabled(True)
        self.createProfileButton.setGeometry(QtCore.QRect(72, 451, 100, 32))
        self.createProfileButton.setMinimumSize(QtCore.QSize(100, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createProfileButton.setIcon(icon1)
        self.createProfileButton.setObjectName("createProfileButton")
        self.lblConsoleOutput = QtWidgets.QLabel(CreateProfile)
        self.lblConsoleOutput.setGeometry(QtCore.QRect(2, 313, 116, 20))
        self.lblConsoleOutput.setObjectName("lblConsoleOutput")
        self.consoleOutputHolder = QtWidgets.QTextEdit(CreateProfile)
        self.consoleOutputHolder.setGeometry(QtCore.QRect(2, 339, 427, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleOutputHolder.sizePolicy().hasHeightForWidth())
        self.consoleOutputHolder.setSizePolicy(sizePolicy)
        self.consoleOutputHolder.setMinimumSize(QtCore.QSize(0, 100))
        self.consoleOutputHolder.setMaximumSize(QtCore.QSize(16777215, 100))
        self.consoleOutputHolder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.consoleOutputHolder.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.consoleOutputHolder.setTabChangesFocus(True)
        self.consoleOutputHolder.setUndoRedoEnabled(False)
        self.consoleOutputHolder.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.consoleOutputHolder.setObjectName("consoleOutputHolder")
        self.lblSaveProfile = QtWidgets.QLabel(CreateProfile)
        self.lblSaveProfile.setGeometry(QtCore.QRect(30, 83, 131, 20))
        self.lblSaveProfile.setObjectName("lblSaveProfile")
        self.profileFilePath = QtWidgets.QLineEdit(CreateProfile)
        self.profileFilePath.setEnabled(True)
        self.profileFilePath.setGeometry(QtCore.QRect(167, 80, 170, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileFilePath.sizePolicy().hasHeightForWidth())
        self.profileFilePath.setSizePolicy(sizePolicy)
        self.profileFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.profileFilePath.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.profileFilePath.setClearButtonEnabled(True)
        self.profileFilePath.setObjectName("profileFilePath")
        self.browseFilePathButton = QtWidgets.QPushButton(CreateProfile)
        self.browseFilePathButton.setGeometry(QtCore.QRect(341, 80, 85, 30))
        self.browseFilePathButton.setMinimumSize(QtCore.QSize(0, 30))
        self.browseFilePathButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.browseFilePathButton.setObjectName("browseFilePathButton")
        self.srcPackageList = QtWidgets.QLineEdit(CreateProfile)
        self.srcPackageList.setEnabled(False)
        self.srcPackageList.setGeometry(QtCore.QRect(164, 193, 265, 30))
        self.srcPackageList.setMinimumSize(QtCore.QSize(0, 30))
        self.srcPackageList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.srcPackageList.setReadOnly(False)
        self.srcPackageList.setClearButtonEnabled(True)
        self.srcPackageList.setObjectName("srcPackageList")
        self.installSrcPackagesCheckBox = QtWidgets.QCheckBox(CreateProfile)
        self.installSrcPackagesCheckBox.setGeometry(QtCore.QRect(11, 195, 147, 25))
        self.installSrcPackagesCheckBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.installSrcPackagesCheckBox.setObjectName("installSrcPackagesCheckBox")
        self.packageList = QtWidgets.QLineEdit(CreateProfile)
        self.packageList.setEnabled(False)
        self.packageList.setGeometry(QtCore.QRect(164, 157, 265, 30))
        self.packageList.setMinimumSize(QtCore.QSize(0, 30))
        self.packageList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.packageList.setReadOnly(False)
        self.packageList.setClearButtonEnabled(True)
        self.packageList.setObjectName("packageList")
        self.installPackagesCheckBox = QtWidgets.QCheckBox(CreateProfile)
        self.installPackagesCheckBox.setGeometry(QtCore.QRect(11, 159, 143, 25))
        self.installPackagesCheckBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.installPackagesCheckBox.setObjectName("installPackagesCheckBox")
        self.updateCheckBox = QtWidgets.QCheckBox(CreateProfile)
        self.updateCheckBox.setGeometry(QtCore.QRect(150, 10, 81, 25))
        self.updateCheckBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.updateCheckBox.setObjectName("updateCheckBox")
        self.upgradePackagesCheckBox = QtWidgets.QCheckBox(CreateProfile)
        self.upgradePackagesCheckBox.setGeometry(QtCore.QRect(260, 10, 159, 25))
        self.upgradePackagesCheckBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.upgradePackagesCheckBox.setObjectName("upgradePackagesCheckBox")
        self.lblInstallType = QtWidgets.QLabel(CreateProfile)
        self.lblInstallType.setGeometry(QtCore.QRect(3, 10, 117, 20))
        self.lblInstallType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblInstallType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblInstallType.setObjectName("lblInstallType")

        self.retranslateUi(CreateProfile)
        QtCore.QMetaObject.connectSlotsByName(CreateProfile)
        CreateProfile.setTabOrder(self.updateCheckBox, self.upgradePackagesCheckBox)
        CreateProfile.setTabOrder(self.upgradePackagesCheckBox, self.profileFilePath)
        CreateProfile.setTabOrder(self.profileFilePath, self.browseFilePathButton)
        CreateProfile.setTabOrder(self.browseFilePathButton, self.targetReleaseCheckBox)
        CreateProfile.setTabOrder(self.targetReleaseCheckBox, self.targetReleaseTextInput)
        CreateProfile.setTabOrder(self.targetReleaseTextInput, self.installPackagesCheckBox)
        CreateProfile.setTabOrder(self.installPackagesCheckBox, self.packageList)
        CreateProfile.setTabOrder(self.packageList, self.installSrcPackagesCheckBox)
        CreateProfile.setTabOrder(self.installSrcPackagesCheckBox, self.srcPackageList)
        CreateProfile.setTabOrder(self.srcPackageList, self.srcBuildDeps)
        CreateProfile.setTabOrder(self.srcBuildDeps, self.generateChangelog)
        CreateProfile.setTabOrder(self.generateChangelog, self.aptBackendComboBox)
        CreateProfile.setTabOrder(self.aptBackendComboBox, self.upgradeTaskComboBox)
        CreateProfile.setTabOrder(self.upgradeTaskComboBox, self.createProfileButton)
        CreateProfile.setTabOrder(self.createProfileButton, self.cancelButton)

    def retranslateUi(self, CreateProfile):
        _translate = QtCore.QCoreApplication.translate
        CreateProfile.setWindowTitle(_translate("CreateProfile", "Generate Signature"))
        self.srcBuildDeps.setToolTip(_translate("CreateProfile", "Check to also include the Build Dependencies for the Source Packages"))
        self.srcBuildDeps.setText(_translate("CreateProfile", "Src Build Deps"))
        self.aptBackendComboBox.setToolTip(_translate("CreateProfile", "Choose APT backend. Default backend is the most tested and known to work under all scenarios"))
        self.aptBackendComboBox.setItemText(0, _translate("CreateProfile", "apt-get"))
        self.aptBackendComboBox.setItemText(1, _translate("CreateProfile", "apt"))
        self.aptBackendComboBox.setItemText(2, _translate("CreateProfile", "python-apt"))
        self.upgradeTaskComboBox.setToolTip(_translate("CreateProfile", "Choose upgrade type to perform"))
        self.upgradeTaskComboBox.setItemText(0, _translate("CreateProfile", "upgrade"))
        self.upgradeTaskComboBox.setItemText(1, _translate("CreateProfile", "dist-upgrade"))
        self.upgradeTaskComboBox.setItemText(2, _translate("CreateProfile", "dselect-upgrade"))
        self.targetReleaseCheckBox.setToolTip(_translate("CreateProfile", "Check to set the target release. If not specified, system default is picked"))
        self.targetReleaseCheckBox.setText(_translate("CreateProfile", "Target Release"))
        self.targetReleaseTextInput.setToolTip(_translate("CreateProfile", "Please specify valid target release name. If not specified, system default is picked"))
        self.label.setToolTip(_translate("CreateProfile", "Choose upgrade type to perform"))
        self.label.setText(_translate("CreateProfile", "Task"))
        self.label_2.setToolTip(_translate("CreateProfile", "Choose APT backend. Default backend is the most tested and known to work under all scenarios"))
        self.label_2.setText(_translate("CreateProfile", "APT Backend"))
        self.generateChangelog.setToolTip(_translate("CreateProfile", "Check to generate changelog for the packages"))
        self.generateChangelog.setText(_translate("CreateProfile", "Changelog"))
        self.cancelButton.setText(_translate("CreateProfile", "Cancel"))
        self.createProfileButton.setText(_translate("CreateProfile", "Create"))
        self.lblConsoleOutput.setText(_translate("CreateProfile", "Console Output:"))
        self.lblSaveProfile.setToolTip(_translate("CreateProfile", "New filename to save the signature data"))
        self.lblSaveProfile.setText(_translate("CreateProfile", "Save Signature As "))
        self.profileFilePath.setToolTip(_translate("CreateProfile", "New filename to save the signature data"))
        self.browseFilePathButton.setText(_translate("CreateProfile", "Browse"))
        self.srcPackageList.setToolTip(_translate("CreateProfile", "List of Source packages to install, separated by space"))
        self.installSrcPackagesCheckBox.setToolTip(_translate("CreateProfile", "Check to install Source Packages"))
        self.installSrcPackagesCheckBox.setText(_translate("CreateProfile", "Source Packages"))
        self.packageList.setToolTip(_translate("CreateProfile", "List of Binary packages to install, separated by space"))
        self.installPackagesCheckBox.setToolTip(_translate("CreateProfile", "Check to install Binary packages"))
        self.installPackagesCheckBox.setText(_translate("CreateProfile", "Binary Packages"))
        self.updateCheckBox.setToolTip(_translate("CreateProfile", "Check to include APT Package Database Updates"))
        self.updateCheckBox.setText(_translate("CreateProfile", "Update"))
        self.upgradePackagesCheckBox.setToolTip(_translate("CreateProfile", "Check to include Package Upgrades"))
        self.upgradePackagesCheckBox.setText(_translate("CreateProfile", "Upgrade Packages"))
        self.lblInstallType.setToolTip(_translate("CreateProfile", "Check all tasks that apply. Eg. Update, Upgrade"))
        self.lblInstallType.setText(_translate("CreateProfile", "Installation Type"))

import resources_rc
