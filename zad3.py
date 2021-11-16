import unittest

text = {
1: "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
2: "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
3: "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
4: "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
5: "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
6: "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
7: "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
8: "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
9: "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
10:"On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
11:"On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
12:"On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
}

class song:
    def verse(num):
        if num>12:
            raise Exception("The song has only 12 verses")
        if num<1:
            raise Exception("A verse number cannot be negative")
        return text[num]









class songtest(unittest.TestCase):

    def test_one_verse(self):
        self.assertEqual(song.verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_exception_too_many_verses(self):
        self.assertRaises(Exception, song.verse, 13)

    def test_exception_negative_verses(self):
        self.assertRaises(Exception, song.verse, -5)

    @unittest.skip
    def test_float_verse(self):
        self.assertEqual(song.verse(2.0), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_str_float_verse(self):
        self.assertEqual(song.verse("3.0"), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    @unittest.skip
    def test_str_letters_verse(self):
        self.assertRaises(Exception, song.verse, "abc")
