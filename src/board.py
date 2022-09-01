from enum import Enum
from dataclasses import dataclass, field

PieceType = Enum("PieceType", "Pawn Rook Knight Bishop Queen King")

Color = Enum("Color", "Black White")


@dataclass
class Piece:
    piece_type: PieceType
    color: Color


@dataclass
class Grid:
    inner: list = field(init=false, default=[None] * 64)

    def __post_init__(self):
        self[0, 0] = Piece(PieceType.Rook, Color.White)
        self[0, 7] = Piece(PieceType.Rook, Color.White)

        self[0, 1] = Piece(PieceType.Knight, Color.White)
        self[0, 6] = Piece(PieceType.Knight, Color.White)

        self[0, 2] = Piece(PieceType.Bishop, Color.White)
        self[0, 5] = Piece(PieceType.Bishop, Color.White)

        self[0, 3] = Piece(PieceType.Queen, Color.White)

        self[0, 4] = Piece(PieceType.King, Color.White)

        self[7, 0] = Piece(PieceType.Rook, Color.Black)
        self[7, 7] = Piece(PieceType.Rook, Color.Black)

        self[7, 1] = Piece(PieceType.Knight, Color.Black)
        self[7, 6] = Piece(PieceType.Knight, Color.Black)

        self[7, 2] = Piece(PieceType.Bishop, Color.Black)
        self[7, 5] = Piece(PieceType.Bishop, Color.Black)

        self[7, 3] = Piece(PieceType.Queen, Color.Black)

        self[7, 4] = Piece(PieceType.King, Color.Black)

        for i in range(8):
            self[1, i] = Piece(PieceType.Pawn, Color.White)
            self[6, i] = Piece(PieceType.Pawn, Color.Black)

    def __getitem__(self, i):
        return self.inner[self.__index_to_num(i)]

    def __setitem__(self, i, data):
        self.inner[self.__index_to_num(i)] = data

    def __index_to_num(i):
        if type(i) is tuple:
            r, c = i
            return r * 8 + c
        elif type(i) is str:
            return (int(i[1]) - 1) * 8 + ord(i[0]) - ord("a")
        else:
            return None


@dataclass
class Board:
    grid: Grid
    black_victims: list
    white_victims: list


print(Board())
