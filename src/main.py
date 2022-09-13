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
from dataclasses import dataclass, field
from enum import Enum
from functools import partial
import chess
import sys


def main():
    app = QApplication([])
    window = MainWindow()
    window.start()
    sys.exit(app.exec())


State = Enum("State", "Start Game")


@dataclass
class MainWindow:
    qwindow: QMainWindow = field(default_factory=QMainWindow)
    state: State = field(default=State.Start)

    def start(self):
        self.build_widgets()
        self.qwindow.show()

    def build_widgets(self):
        match self.state:
            case State.Start:
                self.qwindow.setCentralWidget(self.construct_start_widget())
            case State.Game:
                self.qwindow.setCentralWidget(self.construct_game_widget())

    def switch_state(self, new_state):
        self.state = new_state
        self.build_widgets()

    def construct_start_widget(self):
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

        new_game_button.clicked.connect(partial(self.switch_state, State.Game))

        return container_a

    def construct_game_widget(self):
        container_a = QWidget()

        layout_a = QHBoxLayout()
        container_a.setLayout(layout_a)

        layout_b = QVBoxLayout()
        layout_b.setSizeConstraint(QLayout.SetMinAndMaxSize)
        layout_a.addLayout(layout_b)
        layout_a.setAlignment(layout_b, Qt.AlignCenter)

        back_button = QPushButton("←", container_a)
        layout_b.addWidget(back_button)

        back_button.clicked.connect(partial(self.switch_state, State.Start))

        return container_a


main()
