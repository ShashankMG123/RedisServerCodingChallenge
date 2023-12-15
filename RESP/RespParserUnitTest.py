from RespParser import parser, dataType
import unittest

class TestRespParse(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRespParse, self).__init__(*args, **kwargs)
        self.parserObj = parser()

    def test_string(self):
        response = self.parserObj.deSerialize("+hello world\r\n")
        self.assertEqual(response, ("hello world", dataType.STRING))

    def test_negative_num(self):
        response = self.parserObj.deSerialize(":-1000\r\n")
        self.assertEqual(response, (-1000, dataType.INTEGER))
    
    def test_positive_num(self):
        response = self.parserObj.deSerialize(":1000\r\n")
        self.assertEqual(response, (1000, dataType.INTEGER))
    
    def test_bulk_string_negative(self):
        response = self.parserObj.deSerialize("$0\r\n\r\n")
        self.assertEqual(response, ("", dataType.BULKSTRING))
    
    def test_bulk_string_positive(self):
        response = self.parserObj.deSerialize("$5\r\n\r\n")
        self.assertEqual(response, ("", dataType.BULKSTRING))


if __name__ == "__main__":
    unittest.main()