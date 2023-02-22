import sys

from PyQt5.QtWidgets import *

print("Hello")


class DlgMain(QDialog):
    def __int__(self):
        super().__init__()
        self.setWindowTitle("FirstApp")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
