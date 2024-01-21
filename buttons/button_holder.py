
from PySide6.QtWidgets import QPushButton, QMainWindow

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kevin's Application")
        button = QPushButton("Click here")
        
        self.setCentralWidget(button)
