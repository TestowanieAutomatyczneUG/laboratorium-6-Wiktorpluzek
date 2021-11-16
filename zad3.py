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
        if type(num)!=int:
            if type(num)==float:
                num=int(num)
            if type(num)==str:
                num=float(num)
                num=int(num)
        if num>12:
            raise Exception("The song has only 12 verses")
        if num<1:
            raise Exception("A verse number cannot be negative")
        return text[num]

    def verses(start, stop):
        if type(start)!=int:
            if type(start)==float:
                start=int(start)
            if type(start)==str:
                start=float(start)
                start=int(start)
        if type(stop)!=int:
            if type(stop)==float:
                stop=int(stop)
            if type(stop)==str:
                stop=float(stop)
                stop=int(stop)
        if start>12 or stop>12:
            raise Exception("The song has only 12 verses")
        if start<1 or stop <1:
            raise Exception("A verse number cannot be negative")
        if stop<start:
            raise Exception("Ending verse cannot be before the starting one")
        lyrics = ""
        for i in range(start, stop):
            lyrics += text[i] + '\n'
        lyrics+= text[stop]
        return lyrics












class songtest(unittest.TestCase):

    def test_one_verse(self):
        self.assertEqual(song.verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_exception_too_many_verses(self):
        self.assertRaises(Exception, song.verse, 13)

    def test_exception_negative_verse(self):
        self.assertRaises(Exception, song.verse, -5)

    def test_float_verse(self):
        self.assertEqual(song.verse(2.0), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_str_float_verse(self):
        self.assertEqual(song.verse("3.0"), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_str_letters_verse(self):
        self.assertRaises(Exception, song.verse, "abc")

    def test_1_to_5_verses(self):
        self.assertEqual(song.verses(1,5), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_exception_wrong_order_verses(self):
        self.assertRaises(Exception, song.verse, (5,1))

    def test_2_to_2_verses(self):
        self.assertEqual(song.verses(2,2),
                         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")