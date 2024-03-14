import RPi.GPIO as GPIO
import time
# Настраиваем режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

# Настраиваем все пины из списка dac на выход
GPIO.setup(dac, GPIO.OUT)

# Объявляем переменную dac - список номеров GPIO-пинов в области DAC
dac = [26, 19, 13, 6, 5, 11, 9, 10]

#Функция для перевода десятичного числа в список из 0 и 1
def dec2bin(dec_number):
    return [int(bit) for bit in bin(dec_number)[2:].zfill(8)]


try:
    # Запрашиваем период треугольного сигнала у пользователя
    period = float(input("Введите период треугольного сигнала (в секундах): "))
    
    while True:
        # Генерируем треугольный сигнал
        for value in range(0, 256):
            # Подаем двоичное представление значения на выход ЦАП
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 256)
        for value in range(255, -1, -1):
            # Подаем двоичное представление значения на выход ЦАП
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 256)
            
except KeyboardInterrupt:
    print("Программа завершена.")
finally:
    # Подаем 0 на все пины dac и очищаем настройки GPIO
    GPIO.output(dac, 0)
    GPIO.cleanup()
