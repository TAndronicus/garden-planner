import math

BASE_UNIT = 1


def calculate_amount(radius, x_len, y_len):
    n_y_aligned, n_x_aligned = calculate_orientation(radius, x_len, y_len), calculate_orientation(radius, y_len, x_len)
    return max(n_y_aligned, n_x_aligned)


def calculate_orientation(radius, x_len, y_len):
    h = radius * math.sqrt(3) / 2
    n_rows, n_cols = int(BASE_UNIT * x_len / h - 1), int(BASE_UNIT * y_len / radius - 1)
    return int((n_rows + 1) / 2) * n_cols + int(n_rows / 2) * (n_cols - 1)
