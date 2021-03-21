from src.song import Song
class Room:
    def __init__(self, music_type, guest_list, entry_fee):
        self.music_type = music_type
        self.guest_list = guest_list
        self.songs_list = []
        self.entry_fee = entry_fee
        self.room_revenue = 0


    def check_in(self, guests):
        for guest in guests:
            if guest.age >= 18:
                self.guest_list.append(guest)
                if len(self.guest_list) == 10:
                    return "Sorry, this room is for 10 people only"
            
    def check_out(self, guests):
        for guest in guests:
            self.guest_list.append(guest)

    def add_songs(self, songs):
        for song in songs:
            if song.type == self.music_type:
                self.songs_list.append(song)

    def charge_guest(self, guests):
        for guest in guests:
            self.room_revenue += self.entry_fee

    def check_if_favourite_song_in_room(self, guest):
        for song in self.songs_list:
            if song.title == guest.favourite_song:
                return "Whoo!"

    
