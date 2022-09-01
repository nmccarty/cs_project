from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QLineEdit,
    QDialog,
    QSizePolicy,
)
from PyQt5.QtCore import pyqtSlot, Qt
import sys


def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Hello, this is a GUI application made using PyQt5.")

        self.textBox = QLineEdit()
        self.textBox.setPlaceholderText("Enter some text …")

        self.button = QPushButton("Press me!")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textBox)
        self.layout.addWidget(self.button)
        self.layoutWidget = QWidget()
        self.layoutWidget.setSizePolicy(
            QSizePolicy.Maximum, QSizePolicy.MinimumExpanding
        )
        self.layoutWidget.setMaximumWidth(700)
        self.layoutWidget.setLayout(self.layout)

        self.setCentralWidget(self.layoutWidget)

        self.button.clicked.connect(self.showDialog)

    @pyqtSlot()
    def showDialog(self):
        dialog = QDialog(parent=self)
        dialogLabel = QLabel("The button was pressed.", parent=dialog)
        dialog.exec()


main()
