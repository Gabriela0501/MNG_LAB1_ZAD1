import email
import unittest

from mail import EmailExtractor
import re

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["gabriela.pawlowska@wat.edu.pl", False, False, "Gabriela", "Pawlowska"],
            ["kornelia.fiolkowska@student.wat.edu.pl", True, False, "Kornelia", "Fiolkowska"],
            ["hanna.skwarek@student.wat.edu.pl", True, False, "Hanna", "Skwarek"],
            ["pawel.filipowski02@student.wat.edu.pl", True, True, "Pawel", "Filipowski"],
            ["aleksandra.siwiec@wat.edu.pl", False, False, "Aleksandra", "Siwiec"],
            ["wojtek.kot@wat.edu.pl", False, True, "Wojtek", "Kot"],
            ["emilia.wawer@student.wat.edu.pl", True, False, "Emilia", "Wawer"],
            ["dominik.skwarek@student.wat.edu.pl", True, True, "Dominik", "Skwarek"],
            ["renata.tomkowska@student.wat.edu.pl", True, False, "Renata", "Tomkowska"],
            ["aleksander.kozak@wat.edu.pl", False, True, "Aleksander", "Kozak"],
            ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                print(is_student)
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
            # given
                email = x[0]
                name = x[3]
                is_male = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())