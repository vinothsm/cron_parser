# Cron parser

Cron parser is a simple application which takes a valid cron expression produces an output formatted as a table and the times as a space seperated list. It doesn't handle the special time strings such as "@yearly".

The cron expression is passed as an command line argument to the application. For Example the cron expression `*/15 0 1,15 * 1-5 /usr/bin/find` will print the following output

```
minute         0 15 30 45
hour           0
day_of_month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day_of_week    1 2 3 4 5
command        /usr/bin/find
```

## Getting Started

You should have python installed on your system and it should be added to the system's environment variable.

1. Open the command prompt.
2. Clone the repository.
3. Navigate to the repository folder in the command prompt.
4. Run the command `python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"`

The cron expression should have 6 fields seperated by space and all are mandatory

| Field        | Allowed Values | Allowed special characters |
| ------------ | -------------- | -------------------------- |
| Minutes      | `0-59`         | `*` `,` `-` `/`            |
| Hours        | `0-23`         | `*` `,` `-` `/`            |
| Day of month | `1-31`         | `*` `,` `-` `/`            |
| Month        | `1-12`         | `*` `,` `-` `/`            |
| Day of week  | `0-7`          | `*` `,` `-` `/`            |

## Tests

`tests.py` contains testcases written in python's inbuilt unittest framework. TO run the testcases please follow the below steps.

1. Open the command prompt.
2. Navigate to the repository folder in the command prompt if already cloned else clone the repository.
3. Run the command `python tests.py`
