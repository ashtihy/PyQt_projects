from PyQt5.QtWidgets import *
import sys


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(200, 200)
        self.push_button = QPushButton("Show Message", self)

        self.push_button.move(40, 40)
        self.push_button.clicked.connect(self.evt_button_clicked)

    @classmethod
    def evt_button_clicked(cls):
        msg_disk_full = QMessageBox()
        msg_disk_full.setWindowTitle("Disk Full")
        msg_disk_full.setText("Your Disk Drive is almost Full")
        msg_disk_full.setDetailedText("Your Disk Drive is almost Full, it is almost 95%")
        msg_disk_full.setIcon(QMessageBox.Information)
        msg_disk_full.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        res = msg_disk_full.exec_()
        if res == QMessageBox.Ok:
            print("Ok is pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
