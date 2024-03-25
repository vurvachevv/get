import RPi.GPIO as GPIO
import time

# Объявление переменных с номерами GPIO-пинов
dac = [17, 18, 27, 22, 23, 24, 25, 4]
comp = 5
troyka = 6
leds = [12, 16, 20, 21, 26, 19, 13, 6]  # Пины для светодиодов

# Настройка режима обращения к GPIO
GPIO.setmode(GPIO.BCM)

# Настройка пинов на ввод/вывод
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

# Функция перевода десятичного числа в список из 0 и 1
def dec_to_bin_list(dec_number):
    binary_list = [int(x) for x in bin(dec_number)[2:].zfill(8)]
    return binary_list

# Функция для управления светодиодами
def set_leds(value):
    for i in range(8):
        if value >= (255/8)*(i+1):
            GPIO.output(leds[i], GPIO.HIGH)
        else:
            GPIO.output(leds[i], GPIO.LOW)

# Функция АЦП
def adc():
    value = 0
    for i in range(7, -1, -1):
        value |= (1 << i)
        GPIO.output(dac, dec_to_bin_list(value))
        time.sleep(0.001)  # Подождать перед считыванием результата
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            value &= ~(1 << i)
    return value

try:
    while True:
        # Использование первого АЦП
        digital_value = adc()
        voltage = (digital_value / 255) * 3.3  # Преобразование в напряжение (3.3V)
        print(f"Digital Value (1st ADC): {digital_value}, Voltage: {voltage}V")
        set_leds(digital_value)
        time.sleep(0.5)  # Пауза перед следующим измерением
        
        # Использование второго АЦП (алгоритм последовательного приближения)
        digital_value_sar = adc()
        voltage_sar = (digital_value_sar / 255) * 3.3  # Преобразование в напряжение (3.3V)
        print(f"Digital Value (2nd ADC): {digital_value_sar}, Voltage: {voltage_sar}V")
        set_leds(digital_value_sar)
        time.sleep(0.5)  # Пауза перед следующим измерением

finally:
    GPIO.output(dac, GPIO.LOW)  # Установка всех DAC пинов в LOW
    GPIO.output(leds, GPIO.LOW)  # Погасить все светодиоды
    GPIO.cleanup()  # Очистка настроек GPIO
