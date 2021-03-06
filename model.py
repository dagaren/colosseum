from enum import IntEnum

class CastlingRight(IntEnum):
    LongWhite = 0
    ShortWhite = 1
    LongBlack = 2
    ShortBlack = 3

class Piece(IntEnum):
    WhiteKing = 0
    WhiteQueen = 1
    WhiteBishop = 2
    WhiteKnight = 3
    WhiteRook = 4
    WhitePawn = 5
    BlackKing = 6
    BlackQueen = 7
    BlackBishop = 8
    BlackKnight = 9
    BlackRook = 10
    BlackPawn = 11

class GenericPiece(IntEnum):
    King = 0
    Queen = 1
    Bishop = 2
    Knight = 3
    Rook = 4
    Pawn = 5

class File(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

class Rank(IntEnum):
    _1 = 0
    _2 = 1
    _3 = 2
    _4 = 3
    _5 = 4
    _6 = 5
    _7 = 6
    _8 = 7

class Color(IntEnum):
    White = 0
    Black = 1

class Square(IntEnum):
    A1 = 0
    A2 = 1
    A3 = 2
    A4 = 3
    A5 = 4
    A6 = 5
    A7 = 6
    A8 = 7
    B1 = 8
    B2 = 9
    B3 = 10
    B4 = 11
    B5 = 12
    B6 = 13
    B7 = 14
    B8 = 15
    C1 = 16
    C2 = 17
    C3 = 18
    C4 = 19
    C5 = 20
    C6 = 21
    C7 = 22
    C8 = 23
    D1 = 24
    D2 = 25
    D3 = 26
    D4 = 27
    D5 = 28
    D6 = 29
    D7 = 30
    D8 = 31
    E1 = 32
    E2 = 33
    E3 = 34
    E4 = 35
    E5 = 36
    E6 = 37
    E7 = 38
    E8 = 39
    F1 = 40
    F2 = 41
    F3 = 42
    F4 = 43
    F5 = 44
    F6 = 45
    F7 = 46
    F8 = 47
    G1 = 48
    G2 = 49
    G3 = 50
    G4 = 51
    G5 = 52
    G6 = 53
    G7 = 54
    G8 = 55
    H1 = 56
    H2 = 57
    H3 = 58
    H4 = 59
    H5 = 60
    H6 = 61
    H7 = 62
    H8 = 63

    @staticmethod
    def get_square(file, rank):
        squareName = "{0}{1}".format(file.name, rank.name[1:])
        return Square[squareName]

    def get_file(self):
        return File(int((self - (self % 8)) / 8))

    def get_rank(self):
        return Rank(int(self % 8))