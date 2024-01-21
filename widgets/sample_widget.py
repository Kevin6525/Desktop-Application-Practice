from PySide6.QtWidgets import QWidget, QPushButton

class SampleWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample Widget")