import keyring

database_name = 'mariusz_db'
user = keyring.get_password('CarRentalTask_remote', 'user')
password = keyring.get_password('CarRentalTask_remote', user)
host = '80.211.255.121'
port = 3396
last_date = '2022-12-31'
database_put_cluster_size = 500
