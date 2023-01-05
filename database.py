import mariadb
import config


class Database:
    """
    A class to manage project's database
    Attributes
    ----------
    connection:
        Object to manage connection to project's database
    cursor:
        Cursor of connection to the project's database
    """
    connection = None
    cursor = None
    user = config.user
    password = config.password
    host = config.host
    port = config.port
    name = config.database_name
    last_date = config.last_date

    def __init__(self):
        """
        Constructs all necessary attributes for the database object.
        :param name: str,
            name of database to connect with
        """
        self.connection = mariadb.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        """Closes connection to project's database"""
        self.connection.close()

    def get_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def modify_query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def put_many_query(self, sql, records_to_put, portion):
        for i in range(0, len(records_to_put), portion):
            self.cursor.executemany(sql, records_to_put[i:i + portion])
            self.connection.commit()
