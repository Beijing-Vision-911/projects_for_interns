from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside6 QPushButton")
        self.setGeometry(500,500,500,500)

        self.setButton_func1()
        self.setButton_func2()

    def setButton_func1(self):
        btnl=QPushButton("Quit", self)
        btnl.move(150,400)
        btnl.clicked.connect(self.quiteApp)
    
    def setButton_func2(self):
        btnl=QPushButton("Print", self)
        btnl.move(300,400)
        btnl.clicked.connect(self.printApp)

    def quiteApp(self):
        userInfo=QMessageBox.question(self, "Confirmation", "Do You Want To Quit The Application?", QMessageBox.Yes | QMessageBox.No)

        if userInfo==QMessageBox.Yes:
            myapp.quit()
        elif userInfo==QMessageBox.No:
            pass
    
    def printApp(self):
        userInfo=QMessageBox.question(self, "Confirmation", "Are You Sure You Want To Print?", QMessageBox.Yes | QMessageBox.No)

        if userInfo==QMessageBox.Yes:
            print("Printing Succeeded！")
        elif userInfo==QMessageBox.No:
            pass

if __name__=="__main__":
    myapp=QApplication(sys.argv)
    window=Window()
    window.show()

    myapp.exec()
    sys.exit()