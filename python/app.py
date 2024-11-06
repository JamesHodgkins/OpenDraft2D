# from PySide6 import QtWidgets

# import sys

# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Hello World")
#         l = QtWidgets.QLabel("My simple app V3.")
#         l.setMargin(10)
#         self.setCentralWidget(l)
#         self.show()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     w = MainWindow()
#     app.exec()


from PySide6 import QtWidgets
import sys
from test import Ui_MainWindow  # Import the generated UI class

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        # Set up the UI layout from the .ui file
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI for the main window

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
