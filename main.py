import config
import service_generator
from database import Database
from datetime import datetime
import dates_generator

db = Database()

last_date = datetime.strptime(db.last_date, "%Y-%m-%d").date()
inventory = db.get_query('SELECT inventory_id, purchase_price, sell_price, create_date, last_update FROM inventory')
rentals = db.get_query('SELECT inventory_id, rental_date, return_date FROM rental ORDER BY inventory_id, rental_date')

possible_service_dates_for_all_cars = dates_generator.all_cars_possible_service_dates(inventory, last_date)
changes = dates_generator.changes_creator(rentals)
service_dates = dates_generator.changes_executor(possible_service_dates_for_all_cars, changes)
services = service_generator.services_generator(service_dates, inventory)

sql_delete = 'DELETE FROM service'
db.modify_query(sql_delete)
sql = 'INSERT INTO service (inventory_id, service_type, service_date, service_cost) VALUES (?, ?, ?, ?)'
db.put_many_query(sql, services, config.database_put_cluster_size)

