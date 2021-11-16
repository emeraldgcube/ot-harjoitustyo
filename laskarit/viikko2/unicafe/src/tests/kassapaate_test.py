import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa=Kassapaate()

    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_myytyjen_maara_oikea(self):
        myydyt=self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)