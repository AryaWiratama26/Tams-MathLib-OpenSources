import unittest
import Tams.matematika as math

class TestingTambah(unittest.TestCase):
    def test_operasi(self):
        aktual = math.tambah(3,5,5)
        ekspektasi = 13
        self.assertEqual(aktual, ekspektasi)

class TestingKurang(unittest.TestCase):
    def test_operasi(self):
        aktual = math.kurang(6,5)
        ekspektasi = 1
        self.assertEqual(aktual, ekspektasi)

class TestingKali(unittest.TestCase):
    def test_operasi(self):
        aktual = math.kali(2,4)
        ekspektasi = 8
        self.assertEqual(aktual, ekspektasi)

class TestingBagi(unittest.TestCase):
    def test_operasi(self):
        aktual = math.bagi(8,2)
        ekspektasi = 4
        self.assertEqual(aktual, ekspektasi)

class TestingPangkat(unittest.TestCase):
    def test_operasi(self):
        aktual = math.pangkat(2,2)
        ekspektasi = 4
        self.assertEqual(aktual, ekspektasi)

class TestingFaktorial(unittest.TestCase):
    def test_operasi(self):
        aktual = math.faktorial(3)
        ekspektasi = 6
        self.assertEqual(aktual, ekspektasi)

class TestingFibonacci(unittest.TestCase):
    def test_operasi(self):
        aktual = math.fibbonaci(10)
        ekspektasi = 55
        self.assertEqual(aktual, ekspektasi)