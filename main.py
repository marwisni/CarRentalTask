from database import Database
from datetime import datetime, timedelta, date
from timeit import default_timer
import tools


myDateString = "2022-06-28"
myDate = datetime.strptime(myDateString, "%Y-%m-%d")

# Today's Date is 2022-06-27
todayDate = datetime.now()

if myDate.date() > todayDate.date():
    print("Date is Greater than Today")
else:
    print("Date is not Greater than Today")

db = Database()

last_date = datetime.strptime(db.last_date, "%Y-%m-%d").date()
# rental = db.get_and_print('inventory_id, rental_date, return_date', rental,)

# table = db.get('*', 'inventory', 'inventory_id = 11')
# print (type(table))
# if isinstance(table, tuple):
#     for row in table:
#         print(type(row))
#         if isinstance(row, tuple):
#             for item in row:
#                 print(item, end=' | ')
#             print()

# total_car_amount = db.get('COUNT(*)', 'inventory')
# print(f'Total car amount = {total_car_amount}')
# db.cursor.execute("SELECT inventory_id FROM inventory WHERE inventory_id='1'")
# for (inventory_id) in db.cursor:
#     print(f'in:{inventory_id}')


i = 1
not_valid = 0
# rental = db.get('inventory_id, rental_date, return_date', 'rental')
# dates = all_possible_service_dates(2016, 2024)
# for date in dates:
#     print(date.isoformat())

rentals = db.query("SELECT inventory_id, rental_date, return_date FROM rental ORDER BY inventory_id, rental_date")

changes = []
for rent in rentals:
    change = tools.availability_day(rent[1], rent[2])
    diff = rent[2] - rent[1]
    if change is not None:
        print(f"{i}, {rent[0]}, {rent[1]}, {rent[2]} | {i-1}, {rentals[i - 2][0]}, {rentals[i - 2][1]}, {rentals[i - 2][2]}")
        not_valid += 1
        print(f'Old date: {change[0]}, new date: {change[1]}, {diff}')
        changes.append(change)
    i += 1
print(not_valid)
print(len(changes))
print(type(rentals[113556][2]))

inventory = db.get('inventory_id, purchase_price, sell_price, create_date, last_update', 'inventory')
start = default_timer()
start_date = db.get('MIN(create_date)', 'inventory')
print(f'First date: {start_date}, {(default_timer()-start) * 1000}')
start = default_timer()
start_date = inventory[0][3]
for car in inventory:
    if car[3] < start_date:
        start_date = car[3]
print(f'First date: {start_date}, {(default_timer()-start) * 1000}')

print(inventory[0])
print(inventory[1192])

service_dates = tools.car_possible_service_dates(inventory, tools.all_possible_service_dates(start_date), last_date)
i = 1
for row in service_dates:
    print(f'{i}, {row}')
    i += 1

for car in inventory:
    if (car[3].month == 3 and car[3].day == 1) or (car[4].month == 3 and car[4].day == 1):
        print(car)

tools.rentals_without_chains(rentals)
