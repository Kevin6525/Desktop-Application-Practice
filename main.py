from PySide6.QtWidgets import QApplication
from widgets.sample_widget import SampleWidget
# from buttons.button_holder import ButtonHolder 

import sys

app = QApplication(sys.argv)

window = SampleWidget()

window.show()

app.exec()