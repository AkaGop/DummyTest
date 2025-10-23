# test_s6f11_bug.py

import unittest
from log_parser import _parse_s6f11_report

class TestS6F11Parser(unittest.TestCase):

    def test_s6f11_parsing_with_binary_type(self):
        # This S6F11 message contains a `<B [1] 1>` type, which the current
        # tokenizer does not support, causing a silent parsing failure.
        log_text = """
< L [2]
    < U4 [1] 26955 >
    < L [3]
        < U4 [1] 0 >
        < U4 [1] 101 >
        < L [1]
            < L [2]
                < U4 [1] 1001 >
                < L [2]
                    < B [1] 1 >
                    < A [9] 'OPERATOR' >
                >
            >
        >
    >
>
        """
        parsed_data = _parse_s6f11_report(log_text)
        self.assertTrue(parsed_data, "The S6F11 message should be parsed.")
        self.assertEqual(parsed_data.get('CEID'), 101)
        self.assertEqual(parsed_data.get('RPTID'), 1001)
        self.assertEqual(parsed_data.get('PortStatus'), '1')
        self.assertEqual(parsed_data.get('OperatorID'), 'OPERATOR')

if __name__ == '__main__':
    unittest.main()
