from enum import Enum
from dataclasses import dataclass, field

PieceType = Enum("PieceType", "Pawn Rook Knight Bishop Queen King")

Color = Enum("Color", "Black White")


@dataclass
class Piece:
    piece_type: PieceType
    color: Color


def create_empty_board_grid():
    grid = [None] * 64
    grid[0] = Piece(PieceType.Rook, Color.White)
    grid[7] = Piece(PieceType.Rook, Color.White)

    grid[1] = Piece(PieceType.Knight, Color.White)
    grid[6] = Piece(PieceType.Knight, Color.White)

    grid[2] = Piece(PieceType.Bishop, Color.White)
    grid[5] = Piece(PieceType.Bishop, Color.White)

    grid[3] = Piece(PieceType.Queen, Color.White)

    grid[4] = Piece(PieceType.King, Color.White)

    grid[8 : 8 + 8] = [Piece(PieceType.Pawn, Color.White)] * 8
    return grid


@dataclass
class Board:
    grid: field(default_factory=create_empty_board_grid)
    black_victims: list
    white_victims: list


print(create_empty_board_grid())
