import RPi.GPIO as GPIO

# Устанавливаем номер GPIO-пина, который будет использоваться для ШИМ
pwm_pin = 18

# Настраиваем режим обращения к GPIO
GPIO.setmode(GPIO.BCM)
# Настраиваем выбранный пин на выход
GPIO.setup(pwm_pin, GPIO.OUT)

# Создаем объект управления ШИМ на выбранном GPIO-пине
pwm = GPIO.PWM(pwm_pin, 100)  # Частота ШИМ - 100 Гц

try:
    # Запускаем ШИМ с коэффициентом заполнения (duty cycle) 0
    pwm.start(0)

    while True:
        # Запрашиваем у пользователя коэффициент заполнения (от 0 до 100)
        duty_cycle = float(input("Введите коэффициент заполнения (от 0 до 100): "))
        
        # Ограничиваем введенное значение от 0 до 100
        duty_cycle = max(0, min(100, duty_cycle))
        
        # Устанавливаем введенный коэффициент заполнения
        pwm.ChangeDutyCycle(duty_cycle)
        
        # Расчет и вывод в терминал предполагаемого значения напряжения на выходе RC-цепи
        voltage = duty_cycle / 100 * 3.3  # Предполагаемое напряжение на выходе RC-цепи
        print(f"Предполагаемое напряжение на выходе RC-цепи: {voltage:.2f} Вольт")

except KeyboardInterrupt:
    print("\nПрограмма завершена.")
finally:
    # Очищаем настройки GPIO
    pwm.stop()
    GPIO.cleanup()
