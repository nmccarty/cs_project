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
from enum import Enum
import chess
import sys


def main():
    app = QApplication([])
    window = MainWindow()
    window.start()
    sys.exit(app.exec())


PlayerType = enum("PlayerType", "Human Computer")


@dataclass
class GameState:
    board: chess.Board = field(init=False)

    def construct_widget(self, parent):
        pass


@dataclass
class StartState:
    def construct_widget(self, parent):
        widget = QWidget()
        container = QWidget()



StageTag = enum("StageTag", "Start Game")


@dataclass
class State:
    tag: StageTag = field(default=StageTag.Start)
    inner: Any = field(default_factory=StartState)

    def construct_widget(self, parent):
        return inner.construct_widget(parent)


@dataclass
class MainWindow:
    qwindow: QMainWindow = field(default_factory=QMainWindow)
    state: State = field(default=State.StartState())

    def start(self):
        self.qwindow = self.state.construct_widget()
        qwindow.show()


main()
