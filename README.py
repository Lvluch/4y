result = []

def divider(a, b):
    if a < b:
        raise ValueError("Помилка: a має бути більше чи рівне b")
    if b > 100:
        raise IndexError("Помилка: b має бути 100 чи менше")
    return a / b

data = {(10,): 2, (2,): 5, "123": 4, (18,): 0, (8,): 4, ((),): 15}

for key in data:
    try:
        if not isinstance(key, tuple) or (len(key) != 1 and key[0] != ()):
            raise ValueError("Помилка: неправильна структура ключа")
        
        a = float(key[0]) if key[0] != () else key[0]
        if not isinstance(a, (int, float)):
            raise ValueError("Помилка: обидва аргументи повинні бути числами")

        res = divider(a, data[key])
        result.append(res)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as e:
        print(f"Помилка: {e}")

print(result)
