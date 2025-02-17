import math
import random
from collections import Counter

def get_file_bytes(filename):
    try:
        with open(filename, 'rb') as f:
            return f.read()
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None

def compute_frequencies(data: bytes):
    total = len(data)
    counter = Counter(data)
    frequencies = {byte: count / total for byte, count in counter.items()}
    return frequencies

def compute_entropy(frequencies: dict):
    entropy = -sum(p * math.log2(p) for p in frequencies.values() if p > 0)
    return entropy

def print_frequencies(frequencies: dict):
    print("Символ\tЧастота")
    for byte, freq in sorted(frequencies.items()):
        if 32 <= byte < 127:
            char_repr = chr(byte)
        else:
            char_repr = f"0x{byte:02x}"
        print(f"{char_repr}\t{freq:.4f}")

def generate_identical_file(filename: str, symbol: int, length: int):
    data = bytes([symbol]) * length
    with open(filename, 'wb') as f:
        f.write(data)

def generate_binary_file(filename: str, length: int):
    data = bytes([random.choice([48, 49]) for _ in range(length)])
    with open(filename, 'wb') as f:
        f.write(data)

def generate_random_file(filename: str, length: int):
    data = bytes([random.randint(0, 255) for _ in range(length)])
    with open(filename, 'wb') as f:
        f.write(data)

def analyze_file(filename: str):
    data = get_file_bytes(filename)
    if data is None:
        return
    frequencies = compute_frequencies(data)
    entropy = compute_entropy(frequencies)
    print("\nЧастоты символов:")
    print_frequencies(frequencies)
    print(f"\nИнформационная энтропия файла: {entropy:.4f} бит на символ")

def main():
    while True:
        print("\n=== Меню ===")
        print("1. Проанализировать существующий файл")
        print("2. Сгенерировать файл и проанализировать его")
        print("3. Выход")
        choice = input("Выберите опцию (1-3): ").strip()

        if choice == "1":
            filename = input("Введите путь к файлу: ").strip()
            analyze_file(filename)

        elif choice == "2":
            print("\nВыберите тип генерируемого файла:")
            print("a. Файл, состоящий из одинаковых символов")
            print("b. Файл, состоящий из случайных символов '0' и '1'")
            print("c. Файл, состоящий из случайных байт (от 0 до 255)")
            sub_choice = input("Выберите опцию (a-c): ").strip().lower()
            try:
                length = int(input("Введите количество символов (длина файла): ").strip())
            except ValueError:
                print("Неверное значение длины!")
                continue
            filename = input("Введите имя для файла: ").strip()
            if sub_choice == "a":
                symbol_input = input("Введите символ: ").strip()
                if not symbol_input:
                    print("Символ не задан!")
                    continue
                generate_identical_file(filename, ord(symbol_input[0]), length)
            elif sub_choice == "b":
                generate_binary_file(filename, length)
            elif sub_choice == "c":
                generate_random_file(filename, length)
            else:
                print("Неверный выбор!")
                continue
            print(f"Файл '{filename}' сгенерирован.")
            analyze_file(filename)

        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()
