from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
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


PlayerType = Enum("PlayerType", "Human Computer")


@dataclass
class GameState:
    board: chess.Board = field(init=False)

    def construct_widget(self, parent):
        pass


@dataclass
class StartState:
    def construct_widget(self, parent):
        container_a = QWidget()
        container_b = QWidget()
        container_a_layout = QHBoxLayout()
        container_a_layout.addWidget(container_b)
        container_a.setLayout(container_a_layout)

        container_b_layout = QVBoxLayout()
        container_b.setLayout(container_b_layout)
        return container_a


StageTag = Enum("StageTag", "Start Game")


@dataclass
class State:
    tag: StageTag = field(default=StageTag.Start)
    inner: any = field(default_factory=StartState)

    def construct_widget(self, parent):
        return self.inner.construct_widget(parent)


@dataclass
class MainWindow:
    qwindow: QMainWindow = field(default_factory=QMainWindow)
    state: State = field(default_factory=State)

    def start(self):
        self.qwindow = self.state.construct_widget(None)
        self.qwindow.show()


main()
