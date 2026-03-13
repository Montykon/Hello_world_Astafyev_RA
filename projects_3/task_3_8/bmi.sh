#!/bin/bash

read -p "Введите свою массу(в кг): " mass
read -p "Введите свой рост(в см): " height

bmi=$(((mass*10000)/(height * height)))
echo "Ваш индекс массы тела составляет: $bmi"
