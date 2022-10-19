# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1048, 751)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MyLabel = QLabel(self.centralwidget)
        self.MyLabel.setObjectName(u"MyLabel")

        self.verticalLayout.addWidget(self.MyLabel)

        self.MyGraph = PlotWidget(self.centralwidget)
        self.MyGraph.setObjectName(u"MyGraph")

        self.verticalLayout.addWidget(self.MyGraph)

        self.MyEditLine = QLineEdit(self.centralwidget)
        self.MyEditLine.setObjectName(u"MyEditLine")

        self.verticalLayout.addWidget(self.MyEditLine)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MyPushButtonAdd = QPushButton(self.frame_2)
        self.MyPushButtonAdd.setObjectName(u"MyPushButtonAdd")

        self.horizontalLayout_2.addWidget(self.MyPushButtonAdd)

        self.MyPushButtonDelete = QPushButton(self.frame_2)
        self.MyPushButtonDelete.setObjectName(u"MyPushButtonDelete")

        self.horizontalLayout_2.addWidget(self.MyPushButtonDelete)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MyTable = QTableWidget(self.frame)
        self.MyTable.setObjectName(u"MyTable")

        self.horizontalLayout.addWidget(self.MyTable)

        self.MyList = QListView(self.frame)
        self.MyList.setObjectName(u"MyList")
        self.MyList.setMouseTracking(False)
        self.MyList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.MyList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout.addWidget(self.MyList)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1048, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MyLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.MyPushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.MyPushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

