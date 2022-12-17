import unittest
from cron_parser import main


class cron_parser_test(unittest.TestCase):
    def test_sole_parser(self):
        self.assertEqual(
            main("1 1 1 1 1 /usr/bin/find"),
            {
                "minute": [1],
                "hour": [1],
                "day_of_month": [1],
                "month": [1],
                "day_of_week": [1],
            },
        )

    def test_star_parser(self):
        self.assertEqual(
            main("1 1 1 * * /usr/bin/find"),
            {
                "minute": [1],
                "hour": [1],
                "day_of_month": [1],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5, 6, 7],
            },
        )

    def test_range_parser(self):
        self.assertEqual(
            main("1 1 1-4 * * /usr/bin/find"),
            {
                "minute": [1],
                "hour": [1],
                "day_of_month": [1, 2, 3, 4],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5, 6, 7],
            },
        )

    def test_list_parser(self):
        self.assertEqual(
            main("1 1 1,4 * * /usr/bin/find"),
            {
                "minute": [1],
                "hour": [1],
                "day_of_month": [1, 4],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5, 6, 7],
            },
        )

    def test_step_parser(self):
        self.assertEqual(
            main("*/15 1 1 * * /usr/bin/find"),
            {
                "minute": [0, 15, 30, 45],
                "hour": [1],
                "day_of_month": [1],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5, 6, 7],
            },
        )

    def test_success_scenarios(self):
        self.assertEqual(
            main("*/15 0 1,15 * 1-5 /usr/bin/find"),
            {
                "minute": [0, 15, 30, 45],
                "hour": [0],
                "day_of_month": [1, 15],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5],
            },
        )
        self.assertEqual(
            main("*/15 0 1,15 * 1-6 /usr/bin/find"),
            {
                "minute": [0, 15, 30, 45],
                "hour": [0],
                "day_of_month": [1, 15],
                "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                "day_of_week": [1, 2, 3, 4, 5, 6],
            },
        )

    def test_cron_missing_fields(self):
        with self.assertRaises(ValueError) as context:
            main("*/15 0 1,15 * /usr/bin/find")
        self.assertEqual(
            "Invalid cron expression: 6 fields are required", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
