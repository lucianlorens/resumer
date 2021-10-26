import unittest
import handler

class HandlerTest(unittest.TestCase):
    def test_process(self):
        self.assertEqual(handler.process("ayn", "haaa"), "aynhaaa")

    def test_get_text(self):
        self.assertEqual(handler.get_text("tests/mocks/get_text_file.txt"), "string_example")

    # def test_clean_previous_text_file(self):
    #     self.assertTrue()

if __name__ == '__main__':
    unittest.main()