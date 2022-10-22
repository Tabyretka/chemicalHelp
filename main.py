import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.Ui_MainWindow import Ui_MainWindow
from ChemicalSearch import ChemicalSearch


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if os.path.exists("geckodriver"):
            self.driverPathLineEdit.setText(os.path.abspath("geckodriver"))

        self.startTaskButton.clicked.connect(self.doTask)

    def doTask(self):
        path = self.driverPathLineEdit.text()
        if path == "":
            self.statusbar.showMessage("enter the path to the driver!")
            return
        chain = self.ChainOfEquationsLineEdit.toPlainText()
        if chain == "":
            self.statusbar.showMessage("enter a chain of equations!")
            return
        ch = ChemicalSearch(chain=chain, GeckoDriveFullrPath=path)
        message = ch.open_pages()
        self.statusbar.showMessage(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
