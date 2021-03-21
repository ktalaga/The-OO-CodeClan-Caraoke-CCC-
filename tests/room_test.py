import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock", [], 4.99)
    
    def test_room_has_music_type(self):
        self.assertEqual("Rock", self.room.music_type)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room.guest_list)

    def test_check_in(self):
        guest_1 = Guest("John", 60, 200, "Kashmir")
        guest_2 = Guest("Susan", 44, 100, "Layla")
        guest_3 = Guest("Mark", 25, 400, "Tears in Heaven")
        guest_4 = Guest("Alan", 34, 1100, "Poor Boy Blues")
        guest_5 = Guest("Alan", 17, 1100, "Africa")
        guest_6 = Guest("Mike", 60, 200, "Lay down Sally")
        guest_7 = Guest("Alex", 44, 100, "Black Moon")
        guest_8 = Guest("David", 25, 400, "Beat It")
        guest_9 = Guest("Ally", 34, 1100, "Tush")
        guest_10 = Guest("Anne", 17, 1100, "Cocaine")
        guest_11 = Guest("Jim", 60, 200, "Mean Bone")
        guest_12 = Guest("Barry", 44, 100, "Red, red wine")
        guest_13 = Guest("Charlie", 25, 400, "One")
        guest_14 = Guest("Dan", 34, 1100, "Master of Puppets")
        guest_15 = Guest("Frank", 17, 1100, "Vultures")
        guests = (guest_1, guest_2,guest_3, guest_4, guest_5,guest_6, guest_7,guest_8, guest_9, guest_10, guest_11, guest_12,guest_13, guest_14, guest_15)
        self.room.check_in(guests)
        self.room.charge_guest(self.room.guest_list)
        self.assertEqual(10, len(self.room.guest_list))
        self.assertEqual(49.9, round(self.room.room_revenue, 2))

    def test_check_out(self):
        guest_1 = Guest("John", 60, 200, "Kashmir")
        guest_2 = Guest("Susan", 44, 100, "Layla")
        guests = (guest_1, guest_2)
        self.room.check_out(guests)
        self.assertEqual(2, len(self.room.guest_list))

    def test_room_has_songs_list(self):
        self.assertEqual([], self.room.songs_list)
    
    def test_add_songs(self):
        song_1 = Song("Legs", "ZZ Top", "Rock")
        song_2 = Song("Eric Clapton", "Cocaine", "Blues")
        song_3 = Song("Stevie Ray Vaughan", "Change It", "Blues")
        song_4 = Song("BB King", "Rock Me Baby", "Blues")
        song_5 = Song("Slash", "Mean Bone", "Rock")
        song_6 = Song("Led Zeppelin", "Kashmir", "Rock")
        songs = [song_1, song_2, song_3, song_4, song_5, song_6]
        self.room.add_songs(songs)
        self.assertEqual(3, len(self.room.songs_list))

    def test_room_has_entry_fee(self):
        self.assertEqual(4.99, self.room.entry_fee)

    def test_charge_guest(self):
        guest_1 = Guest("John", 60, 200, "Kashmir")
        guests = [guest_1]
        self.room.charge_guest(guests)
        self.assertEqual(4.99, self.room.room_revenue)

    def test_check_if_favourtite_song_in_room(self):
        song_1 = Song("Legs", "ZZ Top", "Rock")
        song_2 = Song("Eric Clapton", "Cocaine", "Blues")
        song_3 = Song("Stevie Ray Vaughan", "Change It", "Blues")
        song_4 = Song("BB King", "Rock Me Baby", "Blues")
        song_5 = Song("Slash", "Mean Bone", "Rock")
        song_6 = Song("Kashmir", "Kashmir", "Rock")
        songs = [song_1, song_2, song_3, song_4, song_5, song_6]
        self.room.add_songs(songs)
        guest = Guest("John", 60, 200, "Kashmir")
        self.assertEqual(3, len(self.room.songs_list))
        # for song in self.room.songs_list:
        #     print(song.title)
        self.assertEqual("Whoo!", self.room.check_if_favourite_song_in_room(guest))


