donor = input('Группа крови донора: ').strip().upper()
recipient = input('Группа крови рецепиента: ').strip().upper()
if donor == recipient or donor == 'I':
    print('Переливать можно')
else:
    print('Переливать нельзя') 