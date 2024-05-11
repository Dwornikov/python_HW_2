from fractions import Fraction

def calculate_sum_and_product(fraction1, fraction2):
    # Преобразуем строки в дроби
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    # Вычисляем сумму и произведение
    fraction_sum = frac1 + frac2
    fraction_product = frac1 * frac2

    return fraction_sum, fraction_product

def main():
    try:
        # Ввод первой дроби
        fraction1_str = input("Введите первую дробь в формате 'a/b': ")
        # Ввод второй дроби
        fraction2_str = input("Введите вторую дробь в формате 'a/b': ")

        # Вычисление суммы и произведения дробей
        sum_result, product_result = calculate_sum_and_product(fraction1_str, fraction2_str)

        print(f"Сумма дробей: {sum_result}")
        print(f"Произведение дробей: {product_result}")

    except ValueError:
        print("Ошибка! Введите дробь в формате 'a/b'.")

if __name__ == "__main__":
    main()
