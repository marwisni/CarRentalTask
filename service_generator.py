# TYRE_CHANGE_PRICE = 150
# YOSP_PRICE_CHG = 0.05
"""Yearly Oil Service Percentage Price Change"""


def services_generator(dates, inventory, tyre_change_price, yosp_price_change):
    """
    Returns list of services for all cars in inventory which should be inserted into database.
    :param dates: list of lists of dates, list of lists of all services' dates for all cars in inventory.
    :param inventory: list of lists, list of all cars in database.
    :param tyre_change_price: float, cost of tyre change service.
    :param yosp_price_change: float, yearly oil percentage price change.
    :return: list of lists, list of generated services (inventory_id, service_type, service_date, service_cost)
    """
    def tyre_change_gen(inventory_id, tyre_change_date, price):
        """Returns tyre change service for particular car (inventory_id), date and price."""
        return inventory_id, 'tyre change', tyre_change_date, price

    def os_price(inv_id, os_counter):
        """Returns oil service price for particular car and particular oil service counter (price is going to change
        once after each two services done)."""
        def first_os_price(purchase_price):
            """Returns first oil service price depends on purchase price of car."""
            if purchase_price <= 100000:
                return 100
            if purchase_price < 165000:
                return 150
            else:
                return 200

        return int(first_os_price(inventory[inv_id - 1][1]) * (1 + yosp_price_change) ** ((os_counter - 1) // 2) + 0.5)

    def oil_service_gen(inventory_id, oil_service_date, price):
        """Returns oil service for particular car (inventory_id), date and price."""
        return inventory_id, 'oil service', oil_service_date, price

    services = []
    for car_id in range(1, len(dates) + 1):
        oil_services_counter = 1
        for date in dates[car_id - 1]:
            if date.month == 3:
                services.append(tyre_change_gen(car_id, date, tyre_change_price))
                services.append(oil_service_gen(car_id, date, os_price(car_id, oil_services_counter)))
                oil_services_counter += 1
                continue
            if date.month == 9:
                services.append(oil_service_gen(car_id, date, os_price(car_id, oil_services_counter)))
                oil_services_counter += 1
                continue
            if date.month == 11:
                services.append(tyre_change_gen(car_id, date, tyre_change_price))
    return services
