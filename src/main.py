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
from tagged_union import tagged_union, Unit
from dataclasses import dataclass, field
import sys


def main():
    app = QApplication([])

    window = MainWindow()
    window.start()

    sys.exit(app.exec())

@tagged_union
class State:
    Start = StartState
    Game = GameState

@dataclass
class MainWindow:
    qwindow: QMainWindow
    state: State

    def start(self):
        qwindow.show()


main()
