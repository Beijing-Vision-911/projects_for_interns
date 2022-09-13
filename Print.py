from PySide6.QtWidgets import QApplication,  QWidget ,  QTextEdit, QVBoxLayout , QPushButton
import sys  
 
class TextEdit(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Pyside6 QPushButton")
		self.resize(500, 400)    

		self.textEdit = QTextEdit( )      
		self.btnPress1 = QPushButton("Quit")
		self.btnPress2 = QPushButton("Print")   
     
		layout = QVBoxLayout()
		layout.addWidget(self.textEdit)
		layout.addWidget(self.btnPress1)   
		layout.addWidget(self.btnPress2)   	
	
		self.setLayout(layout)
		self.btnPress1.clicked.connect(self.btnPress1_Clicked)
		self.btnPress2.clicked.connect(self.btnPress2_Clicked)
		
	def btnPress1_Clicked(self):
		self.textEdit.setPlainText("Exit succceeded!")
 
	def btnPress2_Clicked(self):
		self.textEdit.setHtml("Printing succeeded!")
		
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	window = TextEdit()	
	window.show()	
	app.exec()
	sys.exit()