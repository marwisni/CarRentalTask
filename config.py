import keyring

user = keyring.get_password('CarRentalTask_remote', 'user')
"""username is stored as password for user: 'user' to not include this name in the code."""

db_init = {
    'host': '80.211.255.121',
    'port': 3396,
    'database_name': 'mariusz_db',
    'user': keyring.get_password('CarRentalTask_remote', 'user'),
    'password': keyring.get_password('CarRentalTask_remote', user)
}

LAST_DATE = '2022-12-31'
DATABASE_PUT_CLUSTER_SIZE = 3264
TYRE_CHANGE_PRICE = 150
YOSP_PRICE_CHG = 0.05
"""Yearly Oil Service Percentage Price Change"""
