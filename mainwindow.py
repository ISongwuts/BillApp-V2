import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from form_ui import Ui_MainWindow
from functools import partial

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path).replace("\\","/")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializedUI()
        self.declareVariables()
        self.onClickedButton()

    def initializedUI(self):
        self.current_theme = "light"
        self.load_theme(self.current_theme)
        self.setWindowTitle("BillApp")
        self.stackPages.setCurrentWidget(self.homePage)
        self.blankLineEdit.setEnabled(False)
        self.initializedTable()

    def initializedTable(self):
        model = QStandardItemModel()
        self.presetTable.setModel(model)
        self.presetTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        model.setHorizontalHeaderLabels(["Serial", "Name", "Quantity", "Price"])
        for i in range(20):
            row_items = [QStandardItem(f"Item {i}, {j}") for j in range(4)]
            for idx, item in enumerate(row_items):
                if idx == 1:
                    continue
                #item.setTextAlignment(Qt.AlignHCenter)
            model.appendRow(row_items)
        self.resizeTable(self.presetTable)

    def resizeTable(self, table_view):
        row_count = table_view.model().rowCount()
        total_height = 0
        for row in range(row_count):
            total_height += table_view.rowHeight(row)
        total_height += table_view.horizontalHeader().height()
        print(str(total_height))
        table_view.setFixedHeight(total_height)

    def declareVariables(self):
        self.button_icons = {
            'home': {'active': 'assets/icon/hover/house-solid.svg', 'inactive': 'assets/icon/light/house-solid.svg'},
            'customer': {'active': 'assets/icon/hover/users-solid.svg', 'inactive': 'assets/icon/light/users-solid.svg'},
            'product': {'active': 'assets/icon/hover/box-open-solid.svg', 'inactive': 'assets/icon/light/box-open-solid.svg'},
            'analysis': {'active': 'assets/icon/hover/chart-simple-solid.svg', 'inactive': 'assets/icon/light/chart-simple-solid.svg'},
            'history': {'active': 'assets/icon/hover/clock-rotate-left-solid.svg', 'inactive': 'assets/icon/light/clock-rotate-left-solid.svg'},
        }

    def setActiveIcons(self, button, button_key):
        if button.isChecked():
            icon_path = self.button_icons[button_key]['active']
        else:
            icon_path = self.button_icons[button_key]['inactive']

        icon = QIcon(resource_path(icon_path))
        button.setIcon(icon)

    def onClickedButton(self):
        self.homeButton.clicked.connect(partial(self.setMainMenuStackPages, self.homePage, self.homeButton))
        self.customerButton.clicked.connect(partial(self.setMainMenuStackPages, self.customerPage, self.customerButton))
        self.productButton.clicked.connect(partial(self.setMainMenuStackPages, self.productPage, self.productButton))
        self.analysisButton.clicked.connect(partial(self.setMainMenuStackPages, self.analysisPage, self.analysisButton))
        self.historyButton.clicked.connect(partial(self.setMainMenuStackPages, self.historyPage, self.historyButton))

        self.goToBillInputPage.clicked.connect(partial(self.setSubMenuStackPages, self.billInputPage, self.goToBillInputPage))
        self.goToBillPreviewPage.clicked.connect(partial(self.setSubMenuStackPages, self.billPreviewPage, self.goToBillPreviewPage))

        self.switchModeButton.clicked.connect(self.onModeChanged)

    def onModeChanged(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            icon = QIcon(resource_path("assets/icon/dark/sun-solid.svg"))
        else:
            self.current_theme = "light"
            icon = QIcon(resource_path("assets/icon/light/moon-solid.svg"))
        self.switchModeButton.setIcon(icon)
        self.load_theme(self.current_theme)
    
    def load_theme(self, theme_name):
        qss_file = resource_path(f"styles/{theme_name}_theme.qss")
        with open(qss_file, "r") as file:
            style_sheet = file.read()
        self.setStyleSheet(style_sheet)

    def setSubMenuStackPages(self, where, clicked_button):
        self.subMenuStackPages.setCurrentWidget(where)
        # Set the other buttons to be unchecked
        for button in [self.goToBillInputPage, self.goToBillPreviewPage]:
            if button != clicked_button:
                button.setChecked(False)
            else:
                # Make sure the clicked button stays active
                button.setChecked(True)

    def setMainMenuStackPages(self, where, clicked_button):
        self.stackPages.setCurrentWidget(where)
        # Set the other buttons to be unchecked
        for button_key, button in zip(self.button_icons.keys(), [self.homeButton, self.customerButton, self.productButton, self.analysisButton, self.historyButton]):
            if button != clicked_button:
                button.setChecked(False)
                self.setActiveIcons(button, button_key)
            else:
                # Make sure the clicked button stays active
                button.setChecked(True)
                self.setActiveIcons(button, button_key)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
