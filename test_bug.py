# test_bug.py

import unittest
from log_parser import _parse_s2f49_command

class TestLogParserBugs(unittest.TestCase):

    def test_panel_count_parsing_with_variable_spacing(self):
        # This log format with `<L[24]>` (no space) fails with the old regex.
        log_block_variant = """
< S2F49
    < L [2]
        < A 'RCMD'
            < A [11] 'LOADSTART' >
        >
        < A 'PARAMETERS'
            < L [2]
                < L [2]
                    < A 'LOTID' >
                    < A [7] 'TESTLOT' >
                >
                < L [2]
                    < A 'LOTPANELS' >
                    <L[24]>
                >
            >
        >
    >
>
.
"""

        parsed_data = _parse_s2f49_command(log_block_variant)
        self.assertIn('PanelCount', parsed_data, "PanelCount should be parsed.")
        self.assertEqual(parsed_data['PanelCount'], 24, "PanelCount should be 24.")

if __name__ == '__main__':
    unittest.main()
