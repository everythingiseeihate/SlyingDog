def summa(complex_numbers):
    if error_handler('addition', complex_numbers): return 'error'
    real_complex_number_result = complex_numbers[0] + complex_numbers[2]
    img_complex_number_result = complex_numbers[1] + complex_numbers[3]

    return [real_complex_number_result, img_complex_number_result]


def raznost(complex_numbers):
    if error_handler('subtraction', complex_numbers): return 'error'
    real_complex_number_result = complex_numbers[0] - complex_numbers[2]
    img_complex_number_result = complex_numbers[1] - complex_numbers[3]

    return [real_complex_number_result, img_complex_number_result]


def multi(complex_numbers):
    if error_handler('multiplication', complex_numbers): return 'error'
    real_complex_number_result = float(
        complex_numbers[0] * complex_numbers[2] - complex_numbers[1] * complex_numbers[3])
    img_complex_number_result = float(complex_numbers[0] * complex_numbers[3] + complex_numbers[1] * complex_numbers[2])

    return [real_complex_number_result, img_complex_number_result]


def divide(complex_numbers):
    if error_handler('division', complex_numbers): return 'error'
    real_complex_number_result = float(
        f'{((complex_numbers[0] * complex_numbers[2] + complex_numbers[1] * complex_numbers[3]) / (complex_numbers[2] ** 2 + complex_numbers[3] ** 2)):.4f}')
    img_complex_number_result = float(
        f'{((complex_numbers[2] * complex_numbers[1] - complex_numbers[0] * complex_numbers[3]) / (complex_numbers[2] ** 2 + complex_numbers[3] ** 2)):.4f}')

    return [real_complex_number_result, img_complex_number_result]


def error_handler(mode, complex_numbers):
    if len(complex_numbers) != 4: return True
    for number in complex_numbers:
        if not isinstance(number, int): return True

    if mode == 'division':
        if complex_numbers[2] + complex_numbers[3] == 0: return True

    return False