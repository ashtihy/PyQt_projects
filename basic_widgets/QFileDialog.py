from PyQt5.QtWidgets import *
import sys


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(200, 200)
        self.push_button = QPushButton("Open File", self)

        self.push_button.move(40, 40)
        self.push_button.clicked.connect(self.evt_button_clicked)

    def evt_button_clicked(self):
        res = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/aseif/OneDrive - SPLM/Desktop", "PNG File (*.png);;JPG FILE (*.jpg)")
        print(res)
        res = QFileDialog.getOpenFileNames(self, "Open File", "C:/Users/aseif/OneDrive - SPLM/Desktop", "PNG File (*.png);;JPG FILE (*.jpg)")
        print(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
