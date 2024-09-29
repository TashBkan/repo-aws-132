import pymysql

endpoint = 'database-132.c5i4oqkack3f.us-west-1.rds.amazonaws.com'
user = 'alejo'
passw = '321654+-'

def connectionSQL():
    try:
        obj_connect = pymysql.connect(
            host=endpoint,
            user=user,
            password=passw
        )
        print("Succesfull connection to a database")
        return obj_connect
    except Exception as err:
        print("Error:", err)
        obj_connect = None

def add_user(id, name, lastname, birtthday):
    try:
        instruction_sql = "INSERT INTO db_users.users (id, name, lastname, birthday) VALUES("+id+", '"+name+"','"+lastname+"','"+birtthday+"');"
        object_connect = connectionSQL()
        object_connect.cursor().execute(instruction_sql)
        object_connect.commit()
        print("The user was added")
        return True
    except Exception as err:
        print("Error:", err)
        return False
