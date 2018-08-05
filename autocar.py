#Программа "Автодилер"
#Позволит пользователю узнать конечную стоимость автомобиля
car = int(input("Введите цену выброного вами авто: "))
tax = car/100*15
regist_tax = car/100*20
agent_tax = 200
delivery = 150
print("Налоговый сбор 15% - ", tax)
print("Регистрационный сбор 20% - ",regist_tax )
print("Агенсткий сбор 200 $")
print("Доставка 150$")
total = car+tax+regist_tax+agent_tax+delivery
print("\n\nОкончательная цена вашего автомобиля составит: $", total)


input("\n\nНажмите Enter, чтобы выйти") 
