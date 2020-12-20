from interface import *
from PyQt5.QtWidgets import QApplication
import sys


main_app = QApplication(sys.argv)
app = InterfaceFM()
app.show()
sys.exit(main_app.exec_())
