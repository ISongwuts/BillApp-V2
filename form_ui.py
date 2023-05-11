# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 582)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.mainContainer)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenuContainer = QWidget(self.mainContainer)
        self.sideMenuContainer.setObjectName(u"sideMenuContainer")
        self.sideMenuContainer.setMinimumSize(QSize(50, 0))
        self.sideMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.sideMenuContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.sideMenuContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setSpacing(25)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(50, 60))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"assets/logo/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_10.addWidget(self.widget, 0, Qt.AlignTop)

        self.upperMenuWrapper = QWidget(self.widget_2)
        self.upperMenuWrapper.setObjectName(u"upperMenuWrapper")
        self.verticalLayout_4 = QVBoxLayout(self.upperMenuWrapper)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.upperMenuWrapper)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame_5)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(0, 30))
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"assets/icon/hover/house-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(18, 18))
        self.homeButton.setCheckable(True)
        self.homeButton.setChecked(True)

        self.verticalLayout_6.addWidget(self.homeButton)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame = QFrame(self.upperMenuWrapper)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.databaseButton = QPushButton(self.frame)
        self.databaseButton.setObjectName(u"databaseButton")
        self.databaseButton.setMinimumSize(QSize(0, 30))
        self.databaseButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"assets/icon/light/database-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseButton.setIcon(icon1)
        self.databaseButton.setIconSize(QSize(18, 18))
        self.databaseButton.setCheckable(True)
        self.databaseButton.setChecked(False)

        self.verticalLayout_5.addWidget(self.databaseButton)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.upperMenuWrapper)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.productButton = QPushButton(self.frame_2)
        self.productButton.setObjectName(u"productButton")
        self.productButton.setMinimumSize(QSize(0, 30))
        self.productButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"assets/icon/light/box-open-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.productButton.setIcon(icon2)
        self.productButton.setIconSize(QSize(18, 18))
        self.productButton.setCheckable(True)
        self.productButton.setChecked(False)

        self.verticalLayout_7.addWidget(self.productButton)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.upperMenuWrapper)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.analysisButton = QPushButton(self.frame_3)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setMinimumSize(QSize(0, 30))
        self.analysisButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"assets/icon/light/chart-simple-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analysisButton.setIcon(icon3)
        self.analysisButton.setIconSize(QSize(18, 18))
        self.analysisButton.setCheckable(True)
        self.analysisButton.setChecked(False)

        self.verticalLayout_8.addWidget(self.analysisButton)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.upperMenuWrapper)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.historyButton = QPushButton(self.frame_4)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setMinimumSize(QSize(0, 30))
        self.historyButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"assets/icon/light/clock-rotate-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.historyButton.setIcon(icon4)
        self.historyButton.setIconSize(QSize(18, 18))
        self.historyButton.setCheckable(True)
        self.historyButton.setChecked(False)

        self.verticalLayout_9.addWidget(self.historyButton)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_10.addWidget(self.upperMenuWrapper, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.sideMenuContainer)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_24 = QVBoxLayout(self.widget_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 25)
        self.lowerMenuWrapper = QWidget(self.widget_11)
        self.lowerMenuWrapper.setObjectName(u"lowerMenuWrapper")
        self.verticalLayout_25 = QVBoxLayout(self.lowerMenuWrapper)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.lowerMenuWrapper)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_10)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.switchModeButton = QPushButton(self.frame_10)
        self.switchModeButton.setObjectName(u"switchModeButton")
        self.switchModeButton.setMinimumSize(QSize(0, 30))
        self.switchModeButton.setMaximumSize(QSize(16777215, 30))
        self.switchModeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"assets/icon/light/moon-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.switchModeButton.setIcon(icon5)
        self.switchModeButton.setIconSize(QSize(18, 18))

        self.verticalLayout_26.addWidget(self.switchModeButton)


        self.verticalLayout_25.addWidget(self.frame_10)


        self.verticalLayout_24.addWidget(self.lowerMenuWrapper, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.horizontalLayout.addWidget(self.sideMenuContainer)

        self.contentWrapper = QWidget(self.mainContainer)
        self.contentWrapper.setObjectName(u"contentWrapper")
        self.verticalLayout_2 = QVBoxLayout(self.contentWrapper)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.stackPages = QStackedWidget(self.contentWrapper)
        self.stackPages.setObjectName(u"stackPages")
        self.stackPages.setMinimumSize(QSize(1000, 562))
        self.analysisPage = QWidget()
        self.analysisPage.setObjectName(u"analysisPage")
        self.stackPages.addWidget(self.analysisPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.homePage)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.billMenuSection = QWidget(self.homePage)
        self.billMenuSection.setObjectName(u"billMenuSection")
        self.billMenuSection.setMinimumSize(QSize(0, 60))
        self.billMenuSection.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_13 = QVBoxLayout(self.billMenuSection)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.billMenuSection)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.goToBillInputPage = QPushButton(self.frame_6)
        self.goToBillInputPage.setObjectName(u"goToBillInputPage")
        self.goToBillInputPage.setMinimumSize(QSize(75, 50))
        self.goToBillInputPage.setMaximumSize(QSize(16777215, 50))
        self.goToBillInputPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToBillInputPage.setCheckable(True)
        self.goToBillInputPage.setChecked(True)

        self.verticalLayout_14.addWidget(self.goToBillInputPage)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.goToBillPreviewPage = QPushButton(self.frame_7)
        self.goToBillPreviewPage.setObjectName(u"goToBillPreviewPage")
        self.goToBillPreviewPage.setMinimumSize(QSize(75, 50))
        self.goToBillPreviewPage.setMaximumSize(QSize(16777215, 50))
        self.goToBillPreviewPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToBillPreviewPage.setCheckable(True)

        self.verticalLayout_15.addWidget(self.goToBillPreviewPage)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_13.addWidget(self.widget_3, 0, Qt.AlignLeft)


        self.verticalLayout_11.addWidget(self.billMenuSection)

        self.billInputSection = QWidget(self.homePage)
        self.billInputSection.setObjectName(u"billInputSection")
        self.verticalLayout_12 = QVBoxLayout(self.billInputSection)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.subMenuStackPages = QStackedWidget(self.billInputSection)
        self.subMenuStackPages.setObjectName(u"subMenuStackPages")
        self.billInputPage = QWidget()
        self.billInputPage.setObjectName(u"billInputPage")
        self.verticalLayout_16 = QVBoxLayout(self.billInputPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.billInputPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 986, 605))
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_18 = QVBoxLayout(self.widget_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.billHeaderContainer = QWidget(self.widget_4)
        self.billHeaderContainer.setObjectName(u"billHeaderContainer")
        self.billHeaderContainer.setMinimumSize(QSize(0, 75))
        self.billHeaderContainer.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_5 = QHBoxLayout(self.billHeaderContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.billHeaderContainer)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, -1, -1, -1)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.widget_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.statusIcon = QPushButton(self.frame_8)
        self.statusIcon.setObjectName(u"statusIcon")
        icon6 = QIcon()
        icon6.addFile(u"assets/icon/special/circle-check-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statusIcon.setIcon(icon6)
        self.statusIcon.setIconSize(QSize(25, 25))

        self.verticalLayout_22.addWidget(self.statusIcon)


        self.verticalLayout_21.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.widget_9, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_20 = QVBoxLayout(self.widget_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.statusTitle = QLabel(self.widget_7)
        self.statusTitle.setObjectName(u"statusTitle")
        font = QFont()
        font.setFamilies([u"Prompt"])
        font.setPointSize(12)
        font.setBold(True)
        self.statusTitle.setFont(font)

        self.verticalLayout_20.addWidget(self.statusTitle)

        self.subStatusTitle = QLabel(self.widget_7)
        self.subStatusTitle.setObjectName(u"subStatusTitle")
        font1 = QFont()
        font1.setFamilies([u"Prompt"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.subStatusTitle.setFont(font1)
        self.subStatusTitle.setWordWrap(False)

        self.verticalLayout_20.addWidget(self.subStatusTitle)


        self.horizontalLayout_4.addWidget(self.widget_7, 0, Qt.AlignVCenter)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")

        self.horizontalLayout_4.addWidget(self.widget_8)


        self.horizontalLayout_5.addWidget(self.widget_6, 0, Qt.AlignLeft)

        self.widget_10 = QWidget(self.billHeaderContainer)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_19 = QVBoxLayout(self.widget_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, 25, -1)
        self.frame_9 = QFrame(self.widget_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, 0, -1)
        self.checkStatusButton = QPushButton(self.frame_9)
        self.checkStatusButton.setObjectName(u"checkStatusButton")
        self.checkStatusButton.setMinimumSize(QSize(75, 30))
        self.checkStatusButton.setMaximumSize(QSize(90, 30))
        self.checkStatusButton.setFont(font1)
        self.checkStatusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkStatusButton.setIconSize(QSize(20, 20))

        self.verticalLayout_23.addWidget(self.checkStatusButton)


        self.verticalLayout_19.addWidget(self.frame_9, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.widget_10)


        self.verticalLayout_18.addWidget(self.billHeaderContainer)

        self.billInputContainer = QWidget(self.widget_4)
        self.billInputContainer.setObjectName(u"billInputContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.billInputContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.customerInputContainer = QWidget(self.billInputContainer)
        self.customerInputContainer.setObjectName(u"customerInputContainer")
        self.customerInputContainer.setMinimumSize(QSize(0, 225))
        self.customerInputContainer.setMaximumSize(QSize(16777215, 225))
        self.verticalLayout_27 = QVBoxLayout(self.customerInputContainer)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.customerInputContainer)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 0))
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_28 = QVBoxLayout(self.widget_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(25, -1, 25, -1)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.widget_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_11)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        icon7 = QIcon()
        icon7.addFile(u"assets/icon/special/circle-solid-blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(12, 12))

        self.verticalLayout_29.addWidget(self.pushButton_2)


        self.horizontalLayout_7.addWidget(self.frame_11, 0, Qt.AlignVCenter)

        self.frame_12 = QFrame(self.widget_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_12)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(13, 0, 0, 0)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Prompt"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.verticalLayout_30.addWidget(self.label_2)


        self.horizontalLayout_7.addWidget(self.frame_12, 0, Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.widget_13, 0, Qt.AlignLeft)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setBaseSize(QSize(0, 0))
        self.verticalLayout_31 = QVBoxLayout(self.widget_14)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_13)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Prompt"])
        self.label_3.setFont(font3)

        self.verticalLayout_32.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame_13)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font3)

        self.verticalLayout_32.addWidget(self.lineEdit)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.widget_16)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_14)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.frame_14)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font3)

        self.verticalLayout_33.addWidget(self.lineEdit_2)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.widget_16)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_34.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.frame_15)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font3)

        self.verticalLayout_34.addWidget(self.lineEdit_3)


        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_31.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_14)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_16)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_35.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.frame_16)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font3)

        self.verticalLayout_35.addWidget(self.lineEdit_4)


        self.horizontalLayout_9.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.widget_17)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_17)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_7)

        self.dateEdit = QDateEdit(self.frame_17)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font3)

        self.verticalLayout_36.addWidget(self.dateEdit)


        self.horizontalLayout_9.addWidget(self.frame_17)


        self.verticalLayout_31.addWidget(self.widget_17)


        self.verticalLayout_28.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.widget_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_18)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 20, 0, 0)
        self.addCustomerDataToPreset = QPushButton(self.frame_18)
        self.addCustomerDataToPreset.setObjectName(u"addCustomerDataToPreset")
        self.addCustomerDataToPreset.setMinimumSize(QSize(75, 30))
        self.addCustomerDataToPreset.setMaximumSize(QSize(75, 30))
        font4 = QFont()
        font4.setFamilies([u"Prompt"])
        font4.setBold(True)
        self.addCustomerDataToPreset.setFont(font4)
        self.addCustomerDataToPreset.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"assets/icon/light/plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCustomerDataToPreset.setIcon(icon8)

        self.verticalLayout_37.addWidget(self.addCustomerDataToPreset)


        self.horizontalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_28.addWidget(self.widget_15, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.widget_12, 0, Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.customerInputContainer)

        self.productInputContainer = QWidget(self.billInputContainer)
        self.productInputContainer.setObjectName(u"productInputContainer")
        self.productInputContainer.setMinimumSize(QSize(0, 225))
        self.productInputContainer.setMaximumSize(QSize(16777215, 225))
        self.verticalLayout_38 = QVBoxLayout(self.productInputContainer)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.productInputContainer)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.verticalLayout_39 = QVBoxLayout(self.widget_18)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(25, -1, 25, -1)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.widget_19)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_19)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_19)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        icon9 = QIcon()
        icon9.addFile(u"assets/icon/special/circle-solid-green.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(12, 12))

        self.verticalLayout_40.addWidget(self.pushButton_3)


        self.horizontalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.widget_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_20)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(13, 0, 0, 0)
        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.verticalLayout_41.addWidget(self.label_8)


        self.horizontalLayout_11.addWidget(self.frame_20)


        self.verticalLayout_39.addWidget(self.widget_19, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.verticalLayout_42 = QVBoxLayout(self.widget_20)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.widget_22)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_21)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamilies([u"Prompt"])
        font5.setBold(False)
        self.label_9.setFont(font5)

        self.verticalLayout_43.addWidget(self.label_9)

        self.comboBox = QComboBox(self.frame_21)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setFont(font3)

        self.verticalLayout_43.addWidget(self.comboBox)


        self.horizontalLayout_12.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.widget_22)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_22)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_22)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font3)

        self.verticalLayout_44.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.frame_22)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setFont(font3)

        self.verticalLayout_44.addWidget(self.comboBox_2)


        self.horizontalLayout_12.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.widget_22)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_23)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_23)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_45.addWidget(self.label_11)

        self.lineEdit_6 = QLineEdit(self.frame_23)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font3)

        self.verticalLayout_45.addWidget(self.lineEdit_6)


        self.horizontalLayout_12.addWidget(self.frame_23)


        self.verticalLayout_42.addWidget(self.widget_22, 0, Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.widget_20, 0, Qt.AlignTop)

        self.blankArea = QWidget(self.widget_18)
        self.blankArea.setObjectName(u"blankArea")
        self.verticalLayout_49 = QVBoxLayout(self.blankArea)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.blankArea)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_25)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.blankLineEdit = QLineEdit(self.frame_25)
        self.blankLineEdit.setObjectName(u"blankLineEdit")
        self.blankLineEdit.setFont(font3)
        self.blankLineEdit.setMouseTracking(False)
        self.blankLineEdit.setAcceptDrops(False)
        self.blankLineEdit.setFrame(False)
        self.blankLineEdit.setReadOnly(True)
        self.blankLineEdit.setClearButtonEnabled(False)

        self.verticalLayout_50.addWidget(self.blankLineEdit)

        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_50.addWidget(self.label_12)


        self.verticalLayout_49.addWidget(self.frame_25)


        self.verticalLayout_39.addWidget(self.blankArea)

        self.widget_21 = QWidget(self.widget_18)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_46 = QVBoxLayout(self.widget_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 21, 0, 0)
        self.frame_24 = QFrame(self.widget_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_24)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.addProductDataToPreset = QPushButton(self.frame_24)
        self.addProductDataToPreset.setObjectName(u"addProductDataToPreset")
        self.addProductDataToPreset.setMinimumSize(QSize(75, 30))
        self.addProductDataToPreset.setMaximumSize(QSize(75, 30))
        self.addProductDataToPreset.setFont(font4)
        self.addProductDataToPreset.setCursor(QCursor(Qt.PointingHandCursor))
        self.addProductDataToPreset.setIcon(icon8)

        self.verticalLayout_47.addWidget(self.addProductDataToPreset)


        self.verticalLayout_46.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.widget_21, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_38.addWidget(self.widget_18, 0, Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.productInputContainer)


        self.verticalLayout_18.addWidget(self.billInputContainer)

        self.billProductContainer = QWidget(self.widget_4)
        self.billProductContainer.setObjectName(u"billProductContainer")
        self.billProductContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_51 = QVBoxLayout(self.billProductContainer)
        self.verticalLayout_51.setSpacing(6)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.billProductContainer)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_61 = QVBoxLayout(self.widget_23)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.wrapPresetHeader = QWidget(self.widget_23)
        self.wrapPresetHeader.setObjectName(u"wrapPresetHeader")
        self.verticalLayout_52 = QVBoxLayout(self.wrapPresetHeader)
        self.verticalLayout_52.setSpacing(6)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(25, 9, 25, 9)
        self.widget_24 = QWidget(self.wrapPresetHeader)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_24)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.widget_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_29)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_29)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u"assets/icon/special/file-invoice-dollar-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_56.addWidget(self.pushButton_4)


        self.horizontalLayout_15.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.widget_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_30)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_30)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_57.addWidget(self.label_13)


        self.horizontalLayout_15.addWidget(self.frame_30)


        self.horizontalLayout_13.addWidget(self.widget_28, 0, Qt.AlignLeft)

        self.widget_27 = QWidget(self.widget_24)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.widget_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_26)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.editProductPresetButton = QPushButton(self.frame_26)
        self.editProductPresetButton.setObjectName(u"editProductPresetButton")
        self.editProductPresetButton.setMinimumSize(QSize(75, 30))
        self.editProductPresetButton.setMaximumSize(QSize(75, 30))
        self.editProductPresetButton.setFont(font4)
        self.editProductPresetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_53.addWidget(self.editProductPresetButton)


        self.horizontalLayout_14.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.widget_27)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_27)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.clearProductPresetButton = QPushButton(self.frame_27)
        self.clearProductPresetButton.setObjectName(u"clearProductPresetButton")
        self.clearProductPresetButton.setMinimumSize(QSize(75, 30))
        self.clearProductPresetButton.setMaximumSize(QSize(75, 30))
        self.clearProductPresetButton.setFont(font4)
        self.clearProductPresetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_54.addWidget(self.clearProductPresetButton)


        self.horizontalLayout_14.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.widget_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_28)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.generatePresetButton = QPushButton(self.frame_28)
        self.generatePresetButton.setObjectName(u"generatePresetButton")
        self.generatePresetButton.setMinimumSize(QSize(75, 30))
        self.generatePresetButton.setMaximumSize(QSize(75, 30))
        self.generatePresetButton.setFont(font4)
        self.generatePresetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_55.addWidget(self.generatePresetButton)


        self.horizontalLayout_14.addWidget(self.frame_28)


        self.horizontalLayout_13.addWidget(self.widget_27, 0, Qt.AlignRight)


        self.verticalLayout_52.addWidget(self.widget_24)


        self.verticalLayout_61.addWidget(self.wrapPresetHeader)

        self.wrapPresetCustomer = QWidget(self.widget_23)
        self.wrapPresetCustomer.setObjectName(u"wrapPresetCustomer")
        self.verticalLayout_58 = QVBoxLayout(self.wrapPresetCustomer)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(25, -1, 25, -1)
        self.widget_26 = QWidget(self.wrapPresetCustomer)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_59 = QVBoxLayout(self.widget_26)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_26)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_31 = QFrame(self.widget_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_31)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_14)

        self.lineEdit_5 = QLineEdit(self.frame_31)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font3)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_5)


        self.horizontalLayout_16.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.widget_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_32)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.horizontalLayout_18.addWidget(self.label_15)

        self.lineEdit_7 = QLineEdit(self.frame_32)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font3)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_7)


        self.horizontalLayout_16.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.widget_29)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_33)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.lineEdit_8 = QLineEdit(self.frame_33)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font3)
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_8)


        self.horizontalLayout_16.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.widget_29)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_34)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.horizontalLayout_20.addWidget(self.label_17)

        self.lineEdit_9 = QLineEdit(self.frame_34)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font3)
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.lineEdit_9)


        self.horizontalLayout_16.addWidget(self.frame_34)


        self.verticalLayout_59.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_26)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_60 = QVBoxLayout(self.widget_30)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_35 = QFrame(self.widget_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_35)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.lineEdit_10 = QLineEdit(self.frame_35)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font3)
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEdit_10)


        self.verticalLayout_60.addWidget(self.frame_35)


        self.verticalLayout_59.addWidget(self.widget_30)


        self.verticalLayout_58.addWidget(self.widget_26)


        self.verticalLayout_61.addWidget(self.wrapPresetCustomer)

        self.wrapPresetTable = QWidget(self.widget_23)
        self.wrapPresetTable.setObjectName(u"wrapPresetTable")
        self.verticalLayout_64 = QVBoxLayout(self.wrapPresetTable)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(25, -1, 25, -1)
        self.widget_25 = QWidget(self.wrapPresetTable)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_65 = QVBoxLayout(self.widget_25)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.presetTable = QTableView(self.widget_25)
        self.presetTable.setObjectName(u"presetTable")
        self.presetTable.setMinimumSize(QSize(0, 100))
        self.presetTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout_65.addWidget(self.presetTable)


        self.verticalLayout_64.addWidget(self.widget_25)


        self.verticalLayout_61.addWidget(self.wrapPresetTable)


        self.verticalLayout_51.addWidget(self.widget_23)


        self.verticalLayout_18.addWidget(self.billProductContainer, 0, Qt.AlignTop)


        self.verticalLayout_48.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_16.addWidget(self.scrollArea)

        self.subMenuStackPages.addWidget(self.billInputPage)
        self.billPreviewPage = QWidget()
        self.billPreviewPage.setObjectName(u"billPreviewPage")
        self.verticalLayout_17 = QVBoxLayout(self.billPreviewPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.billPreviewPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1003, 490))
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_63 = QVBoxLayout(self.widget_5)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.wrapPrintFunction = QWidget(self.widget_5)
        self.wrapPrintFunction.setObjectName(u"wrapPrintFunction")
        self.verticalLayout_66 = QVBoxLayout(self.wrapPrintFunction)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.widget_33 = QWidget(self.wrapPrintFunction)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_36 = QFrame(self.widget_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_36)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.printBillButton = QPushButton(self.frame_36)
        self.printBillButton.setObjectName(u"printBillButton")
        self.printBillButton.setMinimumSize(QSize(75, 30))
        self.printBillButton.setMaximumSize(QSize(75, 30))
        self.printBillButton.setFont(font4)
        self.printBillButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"assets/icon/light/print-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.printBillButton.setIcon(icon11)

        self.verticalLayout_67.addWidget(self.printBillButton)


        self.horizontalLayout_22.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.widget_33)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_37)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_23.addWidget(self.label_19)

        self.comboBox_3 = QComboBox(self.frame_37)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_23.addWidget(self.comboBox_3)


        self.horizontalLayout_22.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.widget_33)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_24.addWidget(self.label_20)

        self.comboBox_4 = QComboBox(self.frame_38)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_24.addWidget(self.comboBox_4)


        self.horizontalLayout_22.addWidget(self.frame_38)


        self.verticalLayout_66.addWidget(self.widget_33, 0, Qt.AlignLeft)


        self.verticalLayout_63.addWidget(self.wrapPrintFunction)

        self.wrapPreviewBill = QWidget(self.widget_5)
        self.wrapPreviewBill.setObjectName(u"wrapPreviewBill")
        self.wrapPreviewBill.setMinimumSize(QSize(0, 300))

        self.verticalLayout_63.addWidget(self.wrapPreviewBill)


        self.verticalLayout_62.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_17.addWidget(self.scrollArea_2)

        self.subMenuStackPages.addWidget(self.billPreviewPage)

        self.verticalLayout_12.addWidget(self.subMenuStackPages)


        self.verticalLayout_11.addWidget(self.billInputSection)

        self.stackPages.addWidget(self.homePage)
        self.somePage = QWidget()
        self.somePage.setObjectName(u"somePage")
        self.somePage.setStyleSheet(u"")
        self.stackPages.addWidget(self.somePage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.historyPage.setStyleSheet(u"")
        self.stackPages.addWidget(self.historyPage)
        self.databasePage = QWidget()
        self.databasePage.setObjectName(u"databasePage")
        self.databasePage.setStyleSheet(u"")
        self.verticalLayout_68 = QVBoxLayout(self.databasePage)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.databasePage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1003, 560))
        self.verticalLayout_69 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.databaseMenuSection = QWidget(self.scrollAreaWidgetContents_3)
        self.databaseMenuSection.setObjectName(u"databaseMenuSection")
        self.databaseMenuSection.setMinimumSize(QSize(0, 60))
        self.databaseMenuSection.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_70 = QVBoxLayout(self.databaseMenuSection)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.databaseMenuSection)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.widget_31)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_39)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.goToCustomerInputPage = QPushButton(self.frame_39)
        self.goToCustomerInputPage.setObjectName(u"goToCustomerInputPage")
        self.goToCustomerInputPage.setMinimumSize(QSize(75, 50))
        self.goToCustomerInputPage.setMaximumSize(QSize(16777215, 50))
        self.goToCustomerInputPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToCustomerInputPage.setCheckable(True)

        self.verticalLayout_71.addWidget(self.goToCustomerInputPage)


        self.horizontalLayout_25.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.widget_31)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_40)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.goToProductInputPage = QPushButton(self.frame_40)
        self.goToProductInputPage.setObjectName(u"goToProductInputPage")
        self.goToProductInputPage.setMinimumSize(QSize(75, 50))
        self.goToProductInputPage.setMaximumSize(QSize(16777215, 50))
        self.goToProductInputPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToProductInputPage.setCheckable(True)

        self.verticalLayout_72.addWidget(self.goToProductInputPage)


        self.horizontalLayout_25.addWidget(self.frame_40)


        self.verticalLayout_70.addWidget(self.widget_31, 0, Qt.AlignLeft)


        self.verticalLayout_69.addWidget(self.databaseMenuSection)

        self.databaseInputSection = QWidget(self.scrollAreaWidgetContents_3)
        self.databaseInputSection.setObjectName(u"databaseInputSection")
        self.verticalLayout_73 = QVBoxLayout(self.databaseInputSection)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.subMenuStackPages_2 = QStackedWidget(self.databaseInputSection)
        self.subMenuStackPages_2.setObjectName(u"subMenuStackPages_2")
        self.customerPage = QWidget()
        self.customerPage.setObjectName(u"customerPage")
        self.verticalLayout_74 = QVBoxLayout(self.customerPage)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.customerPage)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 983, 474))
        self.verticalLayout_75 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, -1)
        self.widget_32 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_32.setObjectName(u"widget_32")

        self.verticalLayout_75.addWidget(self.widget_32)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_74.addWidget(self.scrollArea_4)

        self.subMenuStackPages_2.addWidget(self.customerPage)
        self.productPage = QWidget()
        self.productPage.setObjectName(u"productPage")
        self.subMenuStackPages_2.addWidget(self.productPage)

        self.verticalLayout_73.addWidget(self.subMenuStackPages_2)


        self.verticalLayout_69.addWidget(self.databaseInputSection)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_68.addWidget(self.scrollArea_3)

        self.stackPages.addWidget(self.databasePage)

        self.verticalLayout_2.addWidget(self.stackPages)


        self.horizontalLayout.addWidget(self.contentWrapper)


        self.verticalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homeButton.setText("")
        self.databaseButton.setText("")
        self.productButton.setText("")
        self.analysisButton.setText("")
        self.historyButton.setText("")
        self.switchModeButton.setText("")
        self.goToBillInputPage.setText(QCoreApplication.translate("MainWindow", u"Generator", None))
        self.goToBillPreviewPage.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.statusIcon.setText("")
        self.statusTitle.setText(QCoreApplication.translate("MainWindow", u"Ready for Generatings", None))
        self.subStatusTitle.setText(QCoreApplication.translate("MainWindow", u"This function is now prepared to generate output.", None))
        self.checkStatusButton.setText(QCoreApplication.translate("MainWindow", u"Re-Check", None))
        self.pushButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Customer Form", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bill Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tax ID", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.addCustomerDataToPreset.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Product Form", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_12.setText("")
        self.addProductDataToPreset.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_4.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bill Information", None))
        self.editProductPresetButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.clearProductPresetButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.generatePresetButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bill Number:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Tax ID:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.printBillButton.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Bill Number:", None))
        self.goToCustomerInputPage.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.goToProductInputPage.setText(QCoreApplication.translate("MainWindow", u"Product", None))
    # retranslateUi

