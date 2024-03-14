import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]


def dec_to_bin_list(dec_number):
    return [int(bit) for bit in bin(dec_number)[2:].zfill(8)]


try:
    while True:
        # Просим пользователя вводить число от 0 до 255 и приводим введённое значение к целому числу
        user_input = input("Введите число от 0 до 255 (или 'q' для выхода): ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            dec_number = int(user_input)
            
            if dec_number < 0:
                print("Введите неотрицательное число.")
                continue
            elif dec_number > 255:
                print("Число превышает максимальное значение 255.")
                continue
            
            # Подаем на выход GPIO-пинов из списка dac двоичное представление введенного пользователем числа
            bin_list = dec_to_bin_list(dec_number)
            GPIO.output(dac, bin_list)
            
            # Расчет и вывод в терминал предполагаемого значения напряжения на выходе ЦАП
            voltage = dec_number / 255 * 3.3  # Предполагаемый диапазон напряжений на выходе ЦАП: 0-3.3 Вольта
            print(f"Предполагаемое напряжение на ЦАП: {voltage:.2f} Вольт")
        
        except ValueError:
            print("Ошибка: Введите числовое значение.")
        
except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    # Подаем 0 на все пины dac и очищаем настройки GPIO
    GPIO.output(dac, 0)
    GPIO.cleanup()
