import sys
from parsers import get_cron_field, get_parser
from cron_field_attributes import cron_field_position


def main(cron):
    cron_list = cron.split()
    if len(cron_list) != 6:
        raise ValueError("Invalid cron expression: 6 fields are required")
    cron_field_list = []
    command = cron_list[5]
    cron_list = cron_list[:5]
    for idx, cron in enumerate(cron_list):
        cron_field_list.append(get_cron_field(cron_field_position[idx], cron))
    result = {}
    for cron_field in cron_field_list:
        parser = get_parser(cron_field.field_type)
        value = parser(cron_field)
        result[cron_field.field_name] = value
    print_results(result, command)
    return result


def print_results(d, command):
    for key, value in d.items():
        print("{0: <14}".format(key), *value)
    print("{0: <14}".format("command"), command)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python cron_parser.py "valid cron expression"')
        sys.exit(1)
    main(sys.argv[1])
