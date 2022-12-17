cron_field_range = {
    "minute": [0, 59],
    "hour": [0, 23],
    "day_of_month": [1, 31],
    "month": [1, 12],
    "day_of_week": [1, 7],
}


class cron_field:
    def __init__(self, field_name, field_type, field_value):
        self.field_name = field_name
        self.field_type = field_type
        self.field_value = field_value


cron_field_position = {
    0: "minute",
    1: "hour",
    2: "day_of_month",
    3: "month",
    4: "day_of_week",
}


def get_cron_field(cron_field_name, cron):
    if cron == "*":
        return cron_field(cron_field_name, "star", "*")
    elif "/" in cron:
        return cron_field(cron_field_name, "step", cron)
    elif "," in cron:
        return cron_field(cron_field_name, "list", cron)
    elif "-" in cron:
        return cron_field(cron_field_name, "range", cron)
    elif cron.isdigit():
        return cron_field(cron_field_name, "sole", cron)
    else:
        raise ValueError(
            "Invalid cron expression for field: {}".format(cron_field_name)
        )


def is_in_range(cron_field, cron_field_range):
    return cron_field_range[0] <= cron_field <= cron_field_range[1]
