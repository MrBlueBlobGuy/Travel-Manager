from TravelManage.user import login, User
import unittest


class LoginTestCase(unittest.TestCase):
    def test_login(self):
        self.assertEqual(login('mrblue', 'debo3157').userid, User('mrblue').userid)

if __name__ == '__main__':
    unittest.main()
