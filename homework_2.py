# Практическое задание 2

print('Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), '
      'которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. '
      'Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. '
      'Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). '
      'Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, '
      'как, например, у операции умножения.')


def print_operation_table(operation, num_rows, num_cols):
    for r in range(1, num_rows + 1):
        for c in range(1, num_cols + 1):
            print('''{:<5}'''.format(operation(r, c)), end=' ' if c < num_cols else '\n')


def input_num(name):
    while True:
        try:
            num = int(input(f'Введите {name}: '))
            if num < 1:
                raise ValueError
            return num
        except ValueError:
            print('Допустимые значение: любое натуральное число')


def input_operation():
    allowed_operations = ['*', '+', '-', '**']
    while True:
        try:
            operation = input(f'Введите операцию: ')
            if operation not in allowed_operations:
                raise ValueError
            return operation
        except ValueError:
            print(f'Допустимые значение: {allowed_operations}')


def main():
    num_rows = input_num('количество строк')
    num_cols = input_num('количество столбцов')
    operation = input_operation()
    print_operation_table(lambda x, y: eval(f'{x} {operation} {y}'), num_rows, num_cols)


if __name__ == '__main__':
    main()
