import RPi.GPIO as GPIO
import time

# Объявление переменных с номерами GPIO-пинов
dac = [17, 18, 27, 22, 23, 24, 25, 4]
comp = 5
troyka = 6

# Настройка режима обращения к GPIO
GPIO.setmode(GPIO.BCM)

# Настройка пинов на ввод/вывод
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

# Функция перевода десятичного числа в список из 0 и 1
def dec_to_bin_list(dec_number):
    binary_list = [int(x) for x in bin(dec_number)[2:].zfill(8)]
    return binary_list

# Функция АЦП
def adc():
    for value in range(256):
        binary_value = dec_to_bin_list(value)
        GPIO.output(dac, binary_value)
        time.sleep(0.01)  # Подождать перед считыванием результата
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            return value

try:
    while True:
        digital_value = adc()
        voltage = (digital_value / 255) * 3.3  # Преобразование в напряжение (3.3V)
        print(f"Digital Value: {digital_value}, Voltage: {voltage}V")
        time.sleep(0.5)  # Пауза перед следующим измерением

finally:
    GPIO.output(dac, GPIO.LOW)  # Установка всех DAC пинов в LOW
    GPIO.cleanup()  # Очистка настроек GPIO
