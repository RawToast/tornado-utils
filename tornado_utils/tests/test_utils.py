import unittest


class UtilsTestCase(unittest.TestCase):

    def test_parse_datetime(self):
        from tornado_utils import parse_datetime
        from tornado_utils import DatetimeParseError

        r = parse_datetime('1285041600000')
        self.assertEqual(r.year, 2010)

        r = parse_datetime('1283140800')
        self.assertEqual(r.year, 2010)

        r = parse_datetime('1286744467.0')
        self.assertEqual(r.year, 2010)

        self.assertRaises(DatetimeParseError, parse_datetime, 'junk')


    def test_encrypt_password(self):
        from tornado_utils import encrypt_password

        p = encrypt_password('', log_rounds=12)
        p2 = encrypt_password('', log_rounds=12)
        self.assertNotEqual(p, p2)

        self.assertTrue(isinstance(p, unicode))
        self.assertTrue('$bcrypt$' in p)

        # simulate what the User class's check_password does
        import bcrypt
        p = 'secret'
        r = encrypt_password(p, log_rounds=12)
        hashed = r.split('$bcrypt$')[-1].encode('utf8')
        self.assertEqual(hashed, bcrypt.hashpw(p, hashed))

    def test_valid_email(self):
        from tornado_utils import valid_email
        self.assertTrue(valid_email('peterbe@gmail.com'))
        self.assertTrue(valid_email("peter'be@gmail.com"))

        self.assertTrue(not valid_email('peterbe @gmail.com'))
        self.assertTrue(not valid_email("peter'be@gmai"))

    def test_random_string(self):
        from tornado_utils import random_string

        x = random_string(10)
        self.assertEqual(len(x), 10)
        y = random_string(10)
        self.assertEqual(len(y), 10)
        self.assertNotEqual(x, y)
