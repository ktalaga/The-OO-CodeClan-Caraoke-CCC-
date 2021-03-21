
class Guest:
    def __init__(self, name, age, wallet, favourite_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_entry_fee(self, guest, entry_fee):
            self.wallet =- entry_fee

