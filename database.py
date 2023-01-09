import mariadb


class Database:
    """A class to manage project's database"""
    def __init__(self, init):
        """
        Connects to the database and initializes a cursor for it.

        :param init: dictionary, which contains:
            host: str, host address to connect with;
            port: int, port number to connect with;
            database_name: str, name of database to connect with;
            user: str, username to log in with to the database;
            password: str, password to log in with to the database.
        """
        self.connection = mariadb.connect(host=init['host'],
                                          port=init['port'],
                                          database=init['database_name'],
                                          user=init['user'],
                                          password=init['password'])
        self.cursor = self.connection.cursor()

    def __del__(self):
        """Closes connection to project's database"""
        self.connection.close()

    def get_query(self, sql):
        """
        Execute sql query to get data from the database and return this data.
        :param sql: str, sql query to execute.
        :return: tuple with data obtained from the database
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def modify_query(self, sql):
        """
        Executes sql query to modify data in the database.
        :param sql: str, sql query to execute.
        :return: None
        """
        self.cursor.execute(sql)
        self.connection.commit()

    def put_many_query(self, sql, records_to_put, portion):
        """
        Inserts provided data in to the database in the chunks.
        :param sql: str, sql query to execute.
        :param records_to_put: tuple/list to be inserted into database.
        :param portion: size of chunks for which data will be divided.
        :return: None
        """
        for i in range(0, len(records_to_put), portion):
            self.cursor.executemany(sql, records_to_put[i:i + portion])
            self.connection.commit()
