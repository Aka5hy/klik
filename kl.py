import pyautogui
import time
import random

def click_mouse(min_interval, max_interval, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        interval = random.uniform(min_interval, max_interval)
        pyautogui.click()
        print(f"Clicked! Interval: {interval:.2f} seconds")
        time.sleep(interval)

# Пример использования
min_interval = 0.001  # Минимальный интервал между кликами в секундах
max_interval = 0.005 # Максимальный интервал между кликами в секундах
duration = 300  # Общая продолжительность выполнения в секундах

click_mouse(min_interval, max_interval, duration)
