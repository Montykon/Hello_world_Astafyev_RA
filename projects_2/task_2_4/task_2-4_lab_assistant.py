volume = float(input('Необходимый объём: '))
mass = volume*0.009
mass_good = round(mass, 2)
with open('C:/Users/User/Documents/astafyev_ra/projects_2/task_2_4/recipe.txt', 'w', encoding='utf-8') as recipe:
    recipe.write('ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\n')
    recipe.write(f'Общий объём: {volume} мл\nМасса соли: {mass_good} г\nОбъём воды: {volume}')
    
