import unittest

from fen import Fen
from model import Color, Square, CastlingRight

class TestFen(unittest.TestCase):
    
    ## __parse_en_passant_square tests

    def test_parse_en_passant_square_valid(self):
        expected = Square.A4
        result = Fen._Fen__parse_en_passant_square("a4")
        self.assertEqual(result, expected)

    def test_parse_en_passant_square_invalid(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_en_passant_square("a9")

    ## __parse_turn tests

    def test_parse_turn_white(self):
        expected = Color.White
        result = Fen._Fen__parse_turn("w")
        self.assertEqual(result, expected)

    def test_parse_turn_black(self):
        expected = Color.Black
        result = Fen._Fen__parse_turn("b")
        self.assertEqual(result, expected)

    def test_parse_turn_invalid(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_turn("invalid")

    ## __parse_fifty_move tests

    def test_parse_fifty_move_valid_string(self):
        s = "20"
        expected = 20
        result = Fen._Fen__parse_fifty_move(s)

        self.assertEqual(result, expected)

    def test_parse_fifty_move_negative_number(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_fifty_move("-15")

    def test_parse_fifty_move_non_numeric_string(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_fifty_move("number")

    ## __parse_full_move tests

    def test_parse_full_move_valid_string(self):
        s = "20"
        expected = 20
        result = Fen._Fen__parse_full_move(s)

        self.assertEqual(result, expected)

    def test_parse_full_move_negative_number(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_full_move("-15")

    def test_parse_full_move_non_numeric_string(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_full_move("number")

    ## __parse_castling_rights tests

    def test_parse_castling_rights_empty_string(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_castling_rights("")

    def test_parse_castling_rights_invalid_chars(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_castling_rights("KkQqs")

    def test_parse_castling_rights_repeated_chars(self):
        with self.assertRaises(Exception):
            Fen._Fen__parse_castling_rights("KkQqk")

    def test_parse_castling_rights_valid_string(self):
        result = Fen._Fen__parse_castling_rights("KkQq")
        self.assertIn(CastlingRight.ShortBlack, result)
        self.assertIn(CastlingRight.LongBlack, result)
        self.assertIn(CastlingRight.ShortWhite, result)
        self.assertIn(CastlingRight.LongWhite, result)

    def test_parse_castling_rights_valid_string(self):
        result = Fen._Fen__parse_castling_rights("k")
        self.assertIn(CastlingRight.ShortBlack, result)
        self.assertNotIn(CastlingRight.LongBlack, result)
        self.assertNotIn(CastlingRight.ShortWhite, result)
        self.assertNotIn(CastlingRight.LongWhite, result)

    def test_parse_castling_rights_empty(self):
        result = Fen._Fen__parse_castling_rights("-")
        self.assertNotIn(CastlingRight.ShortBlack, result)
        self.assertNotIn(CastlingRight.LongBlack, result)
        self.assertNotIn(CastlingRight.ShortWhite, result)
        self.assertNotIn(CastlingRight.LongWhite, result)

if __name__ == '__main__':
    unittest.main()