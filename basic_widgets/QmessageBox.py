from PyQt5.QtWidgets import *
import sys


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.push_button = QPushButton(parent=self, text="Press Me")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
