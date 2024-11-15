# warmups/tests.py
from django.test import SimpleTestCase

class TestFrontTimes(SimpleTestCase):
    def test_front_times_boo(self):
        response = self.client.get('/front-times/?csrfmiddlewaretoken=eCTJUQtmkn2JHg1l03dZIB86ByLFxVMCa992sLu9cG4bxzWLXcdapa40GtX1opDT&text=boo&n=2')
        self.assertContains(response, 'Result: booboo')

    def test_front_times_Abc(self):
        response = self.client.get('/front-times/?csrfmiddlewaretoken=eCTJUQtmkn2JHg1l03dZIB86ByLFxVMCa992sLu9cG4bxzWLXcdapa40GtX1opDT&text=Abc&n=3')
        self.assertContains(response, 'Result: AbcAbcAbc')

    def test_front_times_Chocolate(self):
        response = self.client.get('/front-times/?csrfmiddlewaretoken=eCTJUQtmkn2JHg1l03dZIB86ByLFxVMCa992sLu9cG4bxzWLXcdapa40GtX1opDT&text=Chocolate&n=3')
        self.assertContains(response, 'Result: ChoChoCho')

class TestNoTeenSums(SimpleTestCase):
    def test_no_teen_sums_1_2_3(self):
        response = self.client.get('/no-teen-sums/?csrfmiddlewaretoken=dn5hAnXW8CaKZPlNqfiIF5UPAJOiFkOJ9UlA8iYJ0VccP8gdnoiTmEQJFE0EwOF0&a=1&b=2&c=3')
        self.assertContains(response, 'Result: 6')

    def test_no_teen_sums_2_13_1(self):
        response = self.client.get('/no-teen-sums/?csrfmiddlewaretoken=dn5hAnXW8CaKZPlNqfiIF5UPAJOiFkOJ9UlA8iYJ0VccP8gdnoiTmEQJFE0EwOF0&a=2&b=13&c=1')
        self.assertContains(response, 'Result: 3')

    def test_no_teen_sums_2_1_14(self):
        response = self.client.get('/no-teen-sums/?csrfmiddlewaretoken=dn5hAnXW8CaKZPlNqfiIF5UPAJOiFkOJ9UlA8iYJ0VccP8gdnoiTmEQJFE0EwOF0&a=2&b=1&c=14')
        self.assertContains(response, 'Result: 3')

class TestXyzThere(SimpleTestCase):
    def test_xyz_there_abcxyz(self):
        response = self.client.get('/xyz-there/?csrfmiddlewaretoken=NQaHjiyq4fAeAzFLOqErjjzKU6byWmQjJnq0RdzdWyCGqSAbLzEC0SvEZ1nUNQHA&text=abcxyz')
        self.assertContains(response, 'Result: True')

    def test_xyz_there_abc_xyz(self):
        response = self.client.get('/xyz-there/?csrfmiddlewaretoken=NQaHjiyq4fAeAzFLOqErjjzKU6byWmQjJnq0RdzdWyCGqSAbLzEC0SvEZ1nUNQHA&text=abc.xyz')
        self.assertContains(response, 'Result: False')

    def test_xyz_there_xyz(self):
        response = self.client.get('/xyz-there/?csrfmiddlewaretoken=NQaHjiyq4fAeAzFLOqErjjzKU6byWmQjJnq0RdzdWyCGqSAbLzEC0SvEZ1nUNQHA&text=xyz.abc')
        self.assertContains(response, 'Result: True')

class TestCenteredAverage(SimpleTestCase):
    def test_centered_average_1_2_3_4_100(self):
        response = self.client.get('/centered-average/?csrfmiddlewaretoken=lBM1JMHOTzrqudLUtIqgFBVuS4R0V3uIh82khHIBLStSkwGkqRqrmaRoXZ3mMxlZ&numbers=1%2C+2%2C+3%2C+4%2C+100')
        self.assertContains(response, 'Result: 3')
    def test_centered_average_1_1_5_5_10_8_7(self):
        response = self.client.get('/centered-average/?csrfmiddlewaretoken=lBM1JMHOTzrqudLUtIqgFBVuS4R0V3uIh82khHIBLStSkwGkqRqrmaRoXZ3mMxlZ&numbers=1%2C+1%2C+5%2C+5%2C+10%2C+8%2C+7')
        self.assertContains(response, 'Result: 5')
    def test_centered_average_10_4_2_4_2_0(self):
        response = self.client.get('/centered-average/?csrfmiddlewaretoken=lBM1JMHOTzrqudLUtIqgFBVuS4R0V3uIh82khHIBLStSkwGkqRqrmaRoXZ3mMxlZ&numbers=-10%2C+-4%2C+-2%2C+-4%2C+-2%2C+0')
        self.assertContains(response, 'Result: -3')