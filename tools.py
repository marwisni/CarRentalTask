from datetime import date, timedelta


def rentals_without_chains(rentals):
    new_rentals = []
    not_valid = 0
    chain_len = 1
    max_chain_len = 1
    for i in range(1, len(rentals)):
        diff_days = (rentals[i][1] - rentals[i - 1][2]).days
        if diff_days == 0:
            if chain_len == 1:
                chain_start = i - 1
            chain_len += 1
        else:
            if chain_len > 1:
                not_valid += 1
                if chain_len > 6:
                    print(f"{chain_len}: ", end="")
                    for j in range(chain_start, chain_start + chain_len):
                        print(f"{j}, {rentals[j][0]}, {rentals[j][1]}, {rentals[j][2]} | ", end="")
                    print()
                if chain_len > max_chain_len:
                    max_chain_len = chain_len
                chain_len = 1
    print(f'{not_valid}, {max_chain_len}')


def availability_day(rental_date, return_date):
    year = rental_date.year
    months = [3, 9, 11]
    for month in months:
        possible_service_date = date(year, month, 1)
        if possible_service_date >= rental_date:
            if possible_service_date <= return_date:
                return possible_service_date, return_date + timedelta(days=1)
            else:
                return None
        else:
            return None


def all_possible_service_dates(first_date):
    dates = []
    first_year = first_date.year
    last_year = date.today().year
    for yr in range (first_year, last_year + 1):
        dates.append(date(yr, 3, 1))
        dates.append(date(yr, 9, 1))
        dates.append(date(yr, 11, 1))
    return dates


def car_possible_service_dates(inventory, possible_dates, last_date):
    service_dates = []
    for car in inventory:
        if car[2] is not None and car[4].date() < last_date:
            service_last_date = car[4].date()
        else:
            service_last_date = last_date
        for service_date in possible_dates:
            if car[3].date() < service_date < service_last_date:
                service_dates.append((car[0], service_date))
    return service_dates
