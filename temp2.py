# Импортируем необходимые библиотеки
import argparse  # Для обработки аргументов командной строки
import csv  # Для работы с CSV-файлами
import pandas as pd  # Для обработки данных
import matplotlib.pyplot as plt  # Для создания графиков
import math  # Для математических операций

# Функция для генерации CSV-файла с данными о температуре
def generate_csv(filename, duration_seconds=200, sample_rate=0.05):
    # Открываем файл CSV для записи с заданной кодировкой и указанием newline=''
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # Записываем заголовки в CSV-файл
        writer.writerow(['Время', 'Датчик 1 (°C)', 'Датчик 2 (°C)'])

        # Начальные температуры для двух датчиков
        initial_temperature_sensor1 = 45.0
        initial_temperature_sensor2 = 50.0

        # Время в секундах и общая длительность (200 секунд)
        current_time = 0
        total_duration = duration_seconds

        data = []
        while current_time <= total_duration:
            # Рассчитываем температуры с плавными изменениями
            temperature_sensor1 = initial_temperature_sensor1 + 25.0 * math.sin(2 * math.pi * current_time / total_duration)
            temperature_sensor2 = initial_temperature_sensor2 + 20.0 * math.sin(2 * math.pi * current_time / total_duration)
            
            # Добавляем данные в список
            data.append([current_time, temperature_sensor1, temperature_sensor2])
            current_time += sample_rate

        # Записываем данные в CSV-файл
        writer.writerows(data)

# Функция для создания и отображения графика на основе данных из CSV-файла
def plot_temperature_data(csv_filename, title, sensor1_label, sensor2_label):
    # Считываем данные из CSV-файла с использованием pandas
    data = pd.read_csv(csv_filename)

    # Создаем новое окно для графика
    fig, ax = plt.subplots()
    
    # Строим графики для двух датчиков
    ax.plot(data['Время'], data['Датчик 1 (°C)'], label=sensor1_label, color='blue')
    ax.plot(data['Время'], data['Датчик 2 (°C)'], label=sensor2_label, color='red')
    
    # Настройка меток осей и диапазонов значений
    ax.set_xlabel('Время (сек)')
    ax.set_ylabel('Температура (°C)')
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 100)
    
    # Заголовок и легенда
    ax.set_title(title)
    ax.legend(loc='upper right')  # Местоположение легенды

    # Сохраняем график в файл формата png
    plt.savefig('temperature_plot.png')
    
    # Отображаем график
    plt.show()

if __name__ == "__main__":
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Генерация и визуализация данных о температуре.')
    
    # Определяем аргументы командной строки, которые можно передать при запуске скрипта
    parser.add_argument('--csv_filename', default='temperature_data.csv', help='Имя файла CSV')
    parser.add_argument('--title', default='Изменение температуры', help='Заголовок графика')
    parser.add_argument('--sensor1_label', default='Датчик 1', help='Название датчика 1')
    parser.add_argument('--sensor2_label', default='Датчик 2', help='Название датчика 2')
    
    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Генерируем CSV-файл с данными о температуре
    generate_csv(args.csv_filename)
    
    # Строим и отображаем график на основе данных из CSV-файла
    plot_temperature_data(args.csv_filename, args.title, args.sensor1_label, args.sensor2_label)