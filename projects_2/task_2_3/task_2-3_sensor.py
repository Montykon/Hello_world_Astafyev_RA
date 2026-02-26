name = input('Имя оператора')
result = input('Значение прибора')
with open('C:/Users/User/Documents/astafyev_ra/projects_2/task_2_3/sensor_log.txt', 'a', encoding='utf-8') as sensor:
    sensor.write(f'{name}\t{result}')
print('Данные успешно сохранены в sensor_log.txt')