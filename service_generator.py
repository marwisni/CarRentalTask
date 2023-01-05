TYRE_CHANGE_PRICE = 150
YOSP_PRICE_CHG = 0.05
"""Yearly Oil Service Percentage Price Change"""


def services_generator(dates, inventory):
    def tyre_change_gen(inventory_id, date):
        return inventory_id, 'tyre change', date, TYRE_CHANGE_PRICE

    def os_price(inv_id, os_counter):
        def first_os_price(purchase_price):
            if purchase_price <= 100000:
                return 100
            if purchase_price < 165000:
                return 150
            else:
                return 200

        return int(first_os_price(inventory[inv_id - 1][1]) * (1 + YOSP_PRICE_CHG) ** ((os_counter - 1) // 2) + 0.5)

    def oil_service_gen(inventory_id, date, price):
        return inventory_id, 'oil service', date, price

    services = []
    for i in range(len(dates)):
        oil_services_counter = 1
        for date in dates[i]:
            if date.month == 3:
                services.append(tyre_change_gen(i + 1, date))
                services.append(oil_service_gen(i + 1, date, os_price(i + 1, oil_services_counter)))
                oil_services_counter += 1
                continue
            if date.month == 9:
                services.append(oil_service_gen(i + 1, date, os_price(i + 1, oil_services_counter)))
                oil_services_counter += 1
                continue
            if date.month == 11:
                services.append(tyre_change_gen(i + 1, date))
    return services
