from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(200, 200)
        self.push_button = QPushButton("Pick a font", self)

        self.push_button.move(40, 40)
        self.push_button.resize(120, 120)
        self.push_button.clicked.connect(self.evt_button_clicked)

    def evt_button_clicked(self):
        font, status = QFontDialog.getFont(QFont("Arial", 24, QFont.ExtraBold), self, "Pick a Font")
        if status:
            print(f"Font Family: {font.family()}")
            print(f"Font Italic: {font.italic()}")
            print(f"Font Bold: {font.bold()}")
            self.push_button.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
