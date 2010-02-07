# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtMain.ui'
#
# Created: Sun Feb  7 15:40:12 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AptOfflineMain(object):
    def setupUi(self, AptOfflineMain):
        AptOfflineMain.setObjectName("AptOfflineMain")
        AptOfflineMain.resize(432, 544)
        AptOfflineMain.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        AptOfflineMain.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(AptOfflineMain)
        self.centralwidget.setObjectName("centralwidget")
        self.createProfileButton = QtGui.QPushButton(self.centralwidget)
        self.createProfileButton.setGeometry(QtCore.QRect(30, 20, 371, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createProfileButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/contact-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createProfileButton.setIcon(icon)
        self.createProfileButton.setObjectName("createProfileButton")
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(30, 80, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.downloadButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon1)
        self.downloadButton.setObjectName("downloadButton")
        self.restoreButton = QtGui.QPushButton(self.centralwidget)
        self.restoreButton.setGeometry(QtCore.QRect(30, 140, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restoreButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setObjectName("restoreButton")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 220, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.descriptionField = QtGui.QLabel(self.frame)
        self.descriptionField.setGeometry(QtCore.QRect(0, 0, 371, 211))
        self.descriptionField.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionField.setWordWrap(True)
        self.descriptionField.setMargin(10)
        self.descriptionField.setObjectName("descriptionField")
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(280, 450, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.exitButton.setObjectName("exitButton")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        AptOfflineMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AptOfflineMain)
        self.statusbar.setObjectName("statusbar")
        AptOfflineMain.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(AptOfflineMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        self.menuOperations = QtGui.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AptOfflineMain.setMenuBar(self.menubar)
        self.menuCreateProfile = QtGui.QAction(AptOfflineMain)
        self.menuCreateProfile.setIcon(icon)
        self.menuCreateProfile.setObjectName("menuCreateProfile")
        self.menuDownload = QtGui.QAction(AptOfflineMain)
        self.menuDownload.setIcon(icon1)
        self.menuDownload.setObjectName("menuDownload")
        self.menuInstall = QtGui.QAction(AptOfflineMain)
        self.menuInstall.setIcon(icon2)
        self.menuInstall.setObjectName("menuInstall")
        self.menuExit = QtGui.QAction(AptOfflineMain)
        self.menuExit.setIcon(icon3)
        self.menuExit.setObjectName("menuExit")
        self.menuHelp_2 = QtGui.QAction(AptOfflineMain)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/help-contents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHelp_2.setIcon(icon4)
        self.menuHelp_2.setObjectName("menuHelp_2")
        self.menuAbout = QtGui.QAction(AptOfflineMain)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/help-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAbout.setIcon(icon5)
        self.menuAbout.setObjectName("menuAbout")
        self.menuOperations.addAction(self.menuCreateProfile)
        self.menuOperations.addAction(self.menuDownload)
        self.menuOperations.addAction(self.menuInstall)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.menuExit)
        self.menuHelp.addAction(self.menuHelp_2)
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AptOfflineMain)
        QtCore.QMetaObject.connectSlotsByName(AptOfflineMain)

    def retranslateUi(self, AptOfflineMain):
        AptOfflineMain.setWindowTitle(QtGui.QApplication.translate("AptOfflineMain", "APT Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.createProfileButton.setText(QtGui.QApplication.translate("AptOfflineMain", "Create Signature", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("AptOfflineMain", "Download Packages or Upgrades", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreButton.setText(QtGui.QApplication.translate("AptOfflineMain", "Install Packages or Upgrades", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionField.setText(QtGui.QApplication.translate("AptOfflineMain", "Hover your mouse over the buttons to get the description", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("AptOfflineMain", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AptOfflineMain", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOperations.setTitle(QtGui.QApplication.translate("AptOfflineMain", "Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("AptOfflineMain", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreateProfile.setText(QtGui.QApplication.translate("AptOfflineMain", "Create Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreateProfile.setShortcut(QtGui.QApplication.translate("AptOfflineMain", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDownload.setText(QtGui.QApplication.translate("AptOfflineMain", "Fetch Packages or Upgrades", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDownload.setShortcut(QtGui.QApplication.translate("AptOfflineMain", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInstall.setText(QtGui.QApplication.translate("AptOfflineMain", "Restore Packages or Upgrades", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInstall.setShortcut(QtGui.QApplication.translate("AptOfflineMain", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setText(QtGui.QApplication.translate("AptOfflineMain", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExit.setShortcut(QtGui.QApplication.translate("AptOfflineMain", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp_2.setText(QtGui.QApplication.translate("AptOfflineMain", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp_2.setShortcut(QtGui.QApplication.translate("AptOfflineMain", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setText(QtGui.QApplication.translate("AptOfflineMain", "About apt-offline", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
