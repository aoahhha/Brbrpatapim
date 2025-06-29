import unittest
from io import StringIO
from unittest.mock import patch
from holidaybrbr import Santa, JasonVoorhees, StPatrick, EasterBunny, HolidayCharacter


class TestHolidayCharacters(unittest.TestCase):
    def setUp(self):
        self.santa = Santa()
        self.jason = JasonVoorhees()
        self.st_patrick = StPatrick()
        self.easter_bunny = EasterBunny()

    def test_holiday_character_base(self):
        base_char = HolidayCharacter()
        self.assertEqual(base_char.character_name, "Holiday Character")
        self.assertEqual(base_char.relevant_months, [])
        self.assertEqual(base_char.action("anything"), "Holiday Character undefined action")

    def test_santa_lists(self):
        self.santa.nice_list = ["Alice", "Bob"]
        self.santa.naughty_list = ["Charlie"]

        self.assertEqual(self.santa.check("Alice"), "Alice is on the Nice List!🎁✨")
        self.assertEqual(self.santa.check("Charlie"), "Charlie is on the Naughty List!🎅🔥")
        self.assertEqual(self.santa.check("David"), "David is not on any list... yet.🕵️‍♂️")

    @patch('builtins.input', side_effect=["TestUser", "nice"])
    def test_santa_interact_nice(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.santa.interact()
            output = fake_out.getvalue()
            self.assertIn("TestUser is on the Nice List!🎁✨", output)
            self.assertIn("Ho ho ho! Delivering presents to you", output)
            self.assertIn("TestUser", self.santa.nice_list)

    def test_jason_victims(self):
        result = self.jason.add_victim("Victim1")
        self.assertEqual(result, "Victim1 has been added to Jason's victim list!")
        self.assertIn("Victim1", self.jason.victims)

    def test_jason_presents(self):
        present = self.jason.present[0]
        result = self.jason.check_present(present)
        self.assertEqual(result, f"Jason clenches his fists and presents a {present}🎁")

    @patch('builtins.input', return_value="BraveVisitor")
    @patch('random.choice', return_value="Blood Splatter Coffee Mug")
    def test_jason_interact(self, mock_random, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.jason.interact()
            output = fake_out.getvalue()
            self.assertIn("BraveVisitor has been added to Jason's victim list!", output)
            self.assertIn("Jason suddenly appears from the darkness!", output)
            self.assertIn("Jason clenches his fists and presents a Blood Splatter Coffee Mug🎁", output)

    def test_st_patrick_bless(self):
        self.st_patrick.irish_blessings = ["Test blessing"]
        self.assertEqual(self.st_patrick.bless(), "Test blessing")

    def test_st_patrick_shamrocks(self):
        initial = self.st_patrick.shamrocks
        result = self.st_patrick.add_shamrock()
        self.assertEqual(result, f"Snakes banished: {initial + 1}")
        self.assertEqual(self.st_patrick.shamrocks, initial + 1)

    def test_st_patrick_interact(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch.object(self.st_patrick, 'bless', return_value="Test blessing"):
                self.st_patrick.interact()
                output = fake_out.getvalue()
                self.assertIn("Using this shamrock ☘️ to explain the Holy Trinity", output)
                self.assertIn("Snakes banished:", output)
                self.assertIn("Blessing: Test blessing", output)

    def test_easter_bunny_eggs(self):
        initial = self.easter_bunny.eggs_hidden
        count = 3
        result = self.easter_bunny.hide_eggs(count)
        self.assertEqual(result, f"Hidden {count} eggs! Total hidden: {initial + count}")
        self.assertEqual(self.easter_bunny.eggs_hidden, initial + count)

    def test_easter_bunny_carrots(self):
        initial = self.easter_bunny.carrots_eaten
        result = self.easter_bunny.eat_carrot()
        self.assertEqual(result, f"Nom nom! Carrots eaten today: {initial + 1}")
        self.assertEqual(self.easter_bunny.carrots_eaten, initial + 1)

    def test_easter_bunny_basket(self):
        result = self.easter_bunny.check_basket()
        expected_items = ", ".join(self.easter_bunny.basket)
        self.assertEqual(result, f"Basket contains {expected_items}")


    @patch('random.randint', return_value=2)
    def test_easter_bunny_interact(self, mock_randint):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.easter_bunny.interact()
            output = fake_out.getvalue()
            self.assertIn("hop, hop, hop", output)
            self.assertIn("Hidden 2 eggs!", output)
            self.assertIn("Nom nom! Carrots eaten today: 1", output)
            self.assertIn("Basket contains", output)


if __name__ == "__main__":
    unittest.main()


