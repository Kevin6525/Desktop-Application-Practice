from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class SampleWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample Widget")

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        
        self.setLayout(button_layout)