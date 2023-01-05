from datetime import date


def start_date_for_car_rental(inventory):
    start_date = inventory[0][3]
    for car in inventory:
        if car[3] < start_date:
            start_date = car[3]
    return start_date


def new_service_date(rental_date, return_date):
    year = rental_date.year
    months = [3, 9, 11]
    for month in months:
        possible_service_date = date(year, month, 1)
        if possible_service_date > rental_date:
            if possible_service_date < return_date:
                return [possible_service_date, return_date]
    return None


def all_possible_service_dates(inventory, last_date):
    dates = []
    first_year = start_date_for_car_rental(inventory).year
    last_year = last_date.year
    for yr in range (first_year, last_year + 1):
        dates.append(date(yr, 3, 1))
        dates.append(date(yr, 9, 1))
        dates.append(date(yr, 11, 1))
    return dates


def car_latest_possible_service_date(car, last_date):
    if car[2] is not None and car[4].date() < last_date:
        return car[4].date()
    else:
        return last_date


def all_cars_possible_service_dates(inventory, last_date):
    service_dates = []
    for car in inventory:
        service_dates.append([])
        latest_possible_service_date = car_latest_possible_service_date(car, last_date)
        possible_dates = all_possible_service_dates(inventory, last_date)
        for service_date in possible_dates:
            if car[3].date() < service_date < latest_possible_service_date:
                service_dates[car[0] - 1].append(service_date)
    return service_dates


def changes_creator(rentals):
    changes = []
    for rent in rentals:
        change = new_service_date(rent[1], rent[2])
        if change is not None:
            change.insert(0, rent[0])
            changes.append(change)
    return changes


def changes_executor(dates, changes):
    for change in changes:
        for d in range(len(dates[change[0] - 1])):
            if dates[change[0] - 1][d] == change[1]:
                dates[change[0] - 1][d] = change[2]
                break
    return dates
