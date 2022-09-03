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

@dataclass
class GameState:
    pass

@dataclass
class StartState:
    pass

@tagged_union
class State:
    Start = StartState
    Game = GameState

@dataclass
class MainWindow:
    qwindow: QMainWindow = field(default=QMainWindow())
    state: State = field(default=State.StartState)

    def start(self):
        qwindow.show()


main()
