def get_valid_float(prompt):
    while True:
        try:
            value = input(prompt).replace(',', '.')
            return float(value)
        except ValueError:
            print("Ошибка: Введите действительное число, используя только цифры и точку/запятую.")


def get_valid_int(prompt):
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Ошибка: Введите действительное целое число, используя только цифры.")


def calculate_coffee_shop_profit():
    # Ввод данных с валидацией
    rent = get_valid_float("Введите ежемесячную аренду помещения ($): ")
    utilities = get_valid_float("Введите ежемесячные коммунальные услуги ($): ")
    marketing = get_valid_float("Введите ежемесячные расходы на маркетинг ($): ")
    other_expenses = get_valid_float("Введите ежемесячные прочие расходы ($): ")

    barista_salary = get_valid_float("Введите ежемесячную зарплату одного баристы ($): ")
    num_baristas = get_valid_int("Введите количество барист: ")
    other_staff_salary = get_valid_float("Введите ежемесячную зарплату одного другого сотрудника ($): ")
    num_other_staff = get_valid_int("Введите количество других сотрудников: ")

    cost_per_coffee = get_valid_float("Введите себестоимость одной чашки кофе ($): ")
    price_per_coffee = get_valid_float("Введите цену продажи одной чашки кофе ($): ")
    num_customers_per_day = get_valid_int("Введите количество посетителей в день: ")
    days_open_per_month = get_valid_int("Введите количество рабочих дней в месяц: ")

    # Расчет общих ежемесячных расходов
    total_salaries = (barista_salary * num_baristas) + (other_staff_salary * num_other_staff)
    total_expenses = rent + utilities + marketing + other_expenses + total_salaries

    # Расчет ежемесячной выручки и прибыли
    revenue_per_day = price_per_coffee * num_customers_per_day
    total_revenue = revenue_per_day * days_open_per_month
    cost_per_day = cost_per_coffee * num_customers_per_day
    total_cost = cost_per_day * days_open_per_month

    gross_profit = total_revenue - total_cost

    # Расчет налогов
    nds = total_revenue * 0.20  # НДС 20%
    social_contributions = total_salaries * 0.34  # Социальные взносы 34%
    income_tax = (gross_profit - total_expenses - nds - social_contributions) * 0.18  # Подоходный налог 18%

    # Расчет чистой прибыли
    net_profit = gross_profit - total_expenses - nds - social_contributions - income_tax

    # Вывод результатов
    print("\n--- Результаты расчета ---")
    print(f"Общие ежемесячные расходы: ${total_expenses:.2f}")
    print(f"Общая ежемесячная выручка: ${total_revenue:.2f}")
    print(f"Валовая прибыль: ${gross_profit:.2f}")
    print(f"НДС (20%): ${nds:.2f}")
    print(f"Социальные взносы (34%): ${social_contributions:.2f}")
    print(f"Подоходный налог (18%): ${income_tax:.2f}")
    print(f"Чистая прибыль: ${net_profit:.2f}")


# Вызов функции для выполнения расчета
calculate_coffee_shop_profit()

