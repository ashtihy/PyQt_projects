from PyQt5.QtWidgets import *
import sys


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.resize(200, 200)
        self.push_button = QPushButton("Enter Input", self)

        self.push_button.move(40, 40)
        self.push_button.clicked.connect(self.evt_button_clicked)

    def evt_button_clicked(self):
        name, name_status = QInputDialog.getText(self, "Name", "Enter your name")
        if name_status:
            QMessageBox.information(self, "Name", f"Welcome {name}")
        else:
            QMessageBox.critical(self, "Error", "Cancelled, Do not get your name!!")
        color_list = ["Red", "Green", "Blue"]
        fav_color, color_status = QInputDialog.getItem(self, "Color", "Choose your favourite color", color_list)
        if name_status:
            QMessageBox.information(self, "Color", f"Your color is {fav_color}")
        else:
            QMessageBox.critical(self, "Error", "Do not get your color!!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
