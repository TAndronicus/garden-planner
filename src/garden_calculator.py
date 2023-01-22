BASE_UNIT = 1


def calculate_amount(radius, x_len, y_len):
    return int(BASE_UNIT * x_len / radius - 1) * int(BASE_UNIT * y_len / radius - 1)
