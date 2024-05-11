def integer_to_hexadecimal(num):
    hexadecimal_string = hex(num)
    return hexadecimal_string

def main():
    try:
        number = int(input("Введите целое число: "))
        hexadecimal_result = integer_to_hexadecimal(number)
        print(f"Шестнадцатеричное представление числа {number}: {hexadecimal_result}")
    except ValueError:
        print("Ошибка! Введите целое число.")

if __name__ == "__main__":
    main()
