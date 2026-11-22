from worker import WORKER

def main():
    current_year = 2026
    workers = []

    n = int(input("Введите количество работников: "))
    for i in range(n):
        print(f"\nРаботник #{i + 1}:")
        full_name = input("Фамилия и инициалы: ")
        position = input("Должность: ")
        salary = float(input("Зарплата: "))
        hire_year = int(input("Год поступления на работу: "))
        workers.append(WORKER.with_params(full_name, position, salary, hire_year))

    print("\n--- Список работников ---")
    for w in workers:
        w.show()

    threshold = int(input("\nВведите минимальный стаж (лет): "))

    found = [w for w in workers if w.get_experience(current_year) > threshold]

    print(f"\nРаботники со стажем более {threshold} лет:")
    if found:
        for w in found:
            print(f"  {w.full_name} — стаж {w.get_experience(current_year)} лет")
    else:
        print("  Таких работников нет.")

if __name__ == "__main__":
    main()