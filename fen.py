import re
from model import Color, Square, CastlingRight

class Fen:
    @staticmethod
    def parse(fenString):
       parts = re.split('\s+', fenString.strip())
       position = {}

       if len(parts) != 6:
           raise Exception("Invalid fen string")

       position["PiecePlacement"] = Fen.__parse_piece_placement(parts[0])
       position["Turn"] = Fen.__parse_turn(parts[1])
       position["CastlingRights"] = Fen.__parse_castling_rights(parts[2])
       position["EnPassantSquare"] = Fen.__parse_en_passant_square(parts[3])
       position["FiftyMove"] = Fen.__parse_fifty_move(parts[4])
       position["FullMove"] = Fen.__parse_full_move(parts[5])
       
       return position

    @staticmethod
    def __parse_piece_placement(s):
        rankStrings = re.split('/', s)
        rankStrings.reverse()

        if len(rankStrings) != 8:
           raise Exception('Invalid fen string: Piece placement description \'{0}\' not valid'.format(s))

        boardString = "".join(rankStrings)

    @staticmethod
    def __parse_en_passant_square(s):
        try:
            return Square[s.upper()]
        except:
            raise Exception('Invalid fen string: En passant square \'{0}\' not valid'.format(s))

    @staticmethod
    def __parse_fifty_move(s):
        try:
            value = int(s)
            if value < 0:
                raise Exception('Invalid fen string: Fifty move numer \'{0}\' is a negative number'.format(s))
            else:
                return value
        except:
            raise Exception('Invalid fen string: Fifty move numer \'{0}\' not valid'.format(s))

    @staticmethod
    def __parse_full_move(s):
        try:
            value = int(s)
            if value < 0:
                raise Exception('Invalid fen string: Fifty move numer \'{0}\' is a negative number'.format(s))
            else:
                return value
        except:
            raise Exception('Invalid fen string: Fifty move numer \'{0}\' not valid'.format(s))

    @staticmethod
    def __parse_turn(s):
        if s == 'w':
            return Color.White
        elif s == 'b':
            return Color.Black
        else:
            raise Exception('Invalid fen string: Turn \'{0}\' not valid'.format(s))

    @staticmethod
    def __parse_castling_rights(s):
         isMatch = re.match('^(-|((?P<castlingRight>[KQkq])(?!.*(?P=castlingRight)))+)$', s)
         if(not isMatch):
            raise Exception('Invalid castling rights string: Turn \'{0}\' not valid'.format(s))
         else:
            rights = []
            if "k" in s:
                rights.append(CastlingRight.ShortBlack)
            if "K" in s:
                rights.append(CastlingRight.ShortWhite)
            if "q" in s:
                rights.append(CastlingRight.LongBlack)
            if "Q" in s:
                rights.append(CastlingRight.LongWhite)

            return rights