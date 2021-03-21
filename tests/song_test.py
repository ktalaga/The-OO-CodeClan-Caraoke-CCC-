import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Legs", "ZZ Top", "Rock")
    
    def test_song_has_title(self):
        self.assertEqual("Legs", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("ZZ Top", self.song.artist)

    def test_song_has_type(self):
        self.assertEqual("Rock", self.song.type)