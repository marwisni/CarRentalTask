from datetime import date, datetime


def start_date_for_car_rental(inventory):
    """Returns purchase date of first bought car in the inventory."""
    start_date = inventory[0][3]
    for car in inventory:
        if car[3] < start_date:
            start_date = car[3]
    return start_date


def change_for_single_rent(rental_date, return_date):
    """
    Returns change of service's date for rents that have impact on some service date and None for those rents that does
    have no impact on any service date.
    :param rental_date: date, begin date for rent.
    :param return_date: date, end date for rent.
    :return: tuple[previous_service_date, new_service_date], for rents that ave impact on some service date and None
    for others.
    """
    year = rental_date.year
    months = [3, 9, 11]
    for month in months:
        possible_service_date = date(year, month, 1)
        if possible_service_date > rental_date:
            if possible_service_date < return_date:
                return [possible_service_date, return_date]
    return None


def all_possible_service_dates(inventory, last_date):
    """Returns all possible services' dates for inventory until "LAST_DATE" date."""
    dates = []
    first_year = start_date_for_car_rental(inventory).year
    last_year = last_date.year
    for yr in range (first_year, last_year + 1):
        dates.append(date(yr, 3, 1))
        dates.append(date(yr, 9, 1))
        dates.append(date(yr, 11, 1))
    return dates


def car_latest_possible_service_date(car, last_date):
    """Returns the latest possible service date for particular car until "LAST_DATE" date."""
    if car[2] is not None and car[4].date() < last_date:
        return car[4].date()
    else:
        return last_date


def all_cars_possible_service_dates(inventory, last_date):
    """Returns list of lists of possible services' dates for all cars in inventory until 'LAST_DATE' date."""
    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
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
    """Returns list of all necessary changes of services' dates that should be done for tuple of rents"""
    changes = []
    for rent in rentals:
        change = change_for_single_rent(rent[1], rent[2])
        if change is not None:
            change.insert(0, rent[0])
            changes.append(change)
    return changes


def changes_executor(dates, changes):
    """
    Applies changes for list of dates.
    :param dates: list of lists of dates, list of lists of all potential dates for which changes can be applied.
    :param changes: list of lists of two dates, list of changes that should be applied to the dates.
    :return: list of lists of dates, list of updated (if necessary) services' dates.
    """
    for change in changes:
        for d in range(len(dates[change[0] - 1])):
            if dates[change[0] - 1][d] == change[1]:
                dates[change[0] - 1][d] = change[2]
                break
    return dates
