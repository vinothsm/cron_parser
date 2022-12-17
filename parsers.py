from cron_field_attributes import (
    is_in_range,
    cron_field_range,
    cron_field,
    get_cron_field,
)


def sole_parser(field: cron_field):
    if is_in_range(int(field.field_value), cron_field_range[field.field_name]):
        return [int(field.field_value)]
    else:
        raise ValueError(
            "Invalid cron expression for field: {}".format(field.field_name)
        )


def range_parser(field: cron_field):
    cron_field_range_list = field.field_value.split("-")
    if len(cron_field_range_list) != 2:
        raise ValueError(
            "Invalid cron expression for field: {}".format(field.field_name)
        )
    cron_field_range_list = [
        int(cron_field_range) for cron_field_range in cron_field_range_list
    ]
    if is_in_range(
        cron_field_range_list[0], cron_field_range[field.field_name]
    ) and is_in_range(cron_field_range_list[1], cron_field_range[field.field_name]):
        return list(range(cron_field_range_list[0], cron_field_range_list[1] + 1))
    else:
        raise ValueError(
            "Invalid cron expression for field: {}".format(field.field_name)
        )


def list_parser(field: cron_field):
    cron_field_list = field.field_value.split(",")
    cron_field_list = [int(cron_field) for cron_field in cron_field_list]
    for cron_field in cron_field_list:
        if not is_in_range(cron_field, cron_field_range[field.field_name]):
            raise ValueError(
                "Invalid cron expression for field: {}".format(field.field_name)
            )
    return cron_field_list


def step_parser(field: cron_field):
    cron_field_step_list = field.field_value.split("/")
    top_range = cron_field_step_list[0]
    step = int(cron_field_step_list[1])
    top_range_field = get_cron_field(field.field_name, top_range)
    parser = get_parser(top_range_field.field_type)
    top_range_value = parser(top_range_field)
    if not is_in_range(top_range_value[0], cron_field_range[field.field_name]):
        raise ValueError(
            "Invalid cron expression for field: {}".format(field.field_name)
        )
    if not is_in_range(step, cron_field_range[field.field_name]):
        raise ValueError(
            "Invalid cron expression for field: {}".format(field.field_name)
        )
    return list(range(top_range_value[0], top_range_value[-1], step))


def star_parser(field: cron_field):
    return list(
        range(
            cron_field_range[field.field_name][0],
            cron_field_range[field.field_name][1] + 1,
        )
    )


ParserFactory = {
    "sole": sole_parser,
    "range": range_parser,
    "list": list_parser,
    "step": step_parser,
    "star": star_parser,
}


def get_parser(parser_type):
    return ParserFactory[parser_type]
