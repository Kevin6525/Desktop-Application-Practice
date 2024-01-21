
from PySide6.QtWidgets import QPushButton, QMainWindow

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kevin's Application")
        button = QPushButton("Click here")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked button!")