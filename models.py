class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        # create user table in similar fashion
        # come on give it a try it's okay if you make mistakes
        pass

    class ToDoModel:
        TABLENAME = "TODO"

        def __init__(self):
            self.conn = sqlite3.connect('todo.db')

        def create(self, text, description):
            query = f'insert into {TABLENAME} ' \
                    f'(Title, Description) ' \
                    f'values ("{text}","{description}")'

            result = self.conn.execute(query)
            return result
    # Similarly add functions to select, delete and update todo
