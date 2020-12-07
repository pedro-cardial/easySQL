import sqlite3

class Database:
    def __init__(self, file_):
        self.conn = sqlite3.connect(file_)
        self.cursor = self.conn.cursor()

    def create_table(self, name, values):
        names = [i[0] for i in values]
        types = [i[1].upper() for i in values]
        final = ""
        for i in range(len(names)):
            if i != len(names) - 1:
                final += f"{names[i]} {types[i]}, "
            else:
                final += f"{names[i]} {types[i]}"
        print(final)
        self.cursor.execute(f"CREATE TABLE {name} ({final})")
        self.conn.commit()

    def insert(self, table, values):
        for i in range(len(values)):
            try:
                values[i] = str(int(values[i]))
            except:
                values[i] = f"\"{values[i]}\""
        print(f"INSERT INTO {table} VALUES ({', '.join(values)})")
        self.cursor.execute(f"INSERT INTO {table} VALUES ({', '.join(values)})")
        self.conn.commit()

    def get(self, columns, table):
        return self.cursor.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall()

    def delete(self, table, column, value):
        try:
            int(value)
        except:
            value = f"\"{value}\""
        print(f"DELETE FROM {table} WHERE {column} = {value}")
        self.cursor.execute(f"DELETE FROM {table} WHERE {column} = {value}")
        self.conn.commit()

    def clear(self, table):
        self.cursor.execute(f"DELETE FROM {table}")
        self.conn.commit()

    def drop(self, table):
        self.cursor.execute(f"DROP TABLE {table}")
        self.conn.commit()