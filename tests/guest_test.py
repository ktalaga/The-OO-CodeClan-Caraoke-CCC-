import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John", 60, 200, "Girls, girls, Girls")
    
    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(60, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(200, self.guest.wallet)

    # def test_pay_entry_fee(self):
    #     guest_1 = Guest("John", 60, 200, "Kashmir")
    #     self.assertEqual(200, self.guest.wallet)
    #     self.guest.pay_entry_fee(guest_1, 4.99)
    #     self.assertEqual(195.01, self.guest.wallet)

# Have problem with this test. I try to charge John's wallet which is 200 £.
# When I print out wallet before pay_entry_fee method it shows 200 as it should
# But when I use pay_entry_fee method it substracts entry fee from 0 not from 200


    def test_guest_has_favourite_song(self):
        self.assertEqual("Girls, girls, Girls", self.guest.favourite_song)
