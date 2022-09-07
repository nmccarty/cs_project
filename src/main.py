from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
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

    def construct_widget(self):
        pass


@dataclass
class StartState:
    def construct_widget(self):
        container_a = QWidget()

        layout_a = QHBoxLayout()
        container_a.setLayout(layout_a)

        layout_b = QVBoxLayout()
        layout_b.setSizeConstraint(QLayout.SetMinAndMaxSize)
        layout_a.addLayout(layout_b)
        layout_a.setAlignment(layout_b, Qt.AlignCenter)

        new_game_button = QPushButton("New game", container_a)
        load_existing_game_button = QPushButton("Load existing game", container_a)
        load_statistics_button = QPushButton("Load statistics", container_a)
        settings_button = QPushButton("Settings", container_a)
        layout_b.addWidget(new_game_button)
        layout_b.addWidget(load_existing_game_button)
        layout_b.addWidget(load_statistics_button)
        layout_b.addWidget(settings_button)

        return container_a


StageTag = Enum("StageTag", "Start Game")


@dataclass
class State:
    tag: StageTag = field(default=StageTag.Start)
    inner: any = field(default_factory=StartState)

    def construct_widget(self):
        return self.inner.construct_widget()


@dataclass
class MainWindow:
    qwindow: QMainWindow = field(default_factory=QMainWindow)
    state: State = field(default_factory=State)

    def start(self):
        self.qwindow = self.state.construct_widget()
        self.qwindow.show()


main()
