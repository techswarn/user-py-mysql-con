
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
print("get_profile_data called:")
print("Current Time =", current_time)



print("got to this point, the very beginning")
import mysql.connector
import os



# print(mysql.connector.__path__())


host = "new-mysql-func-db-do-user-11648032-0.b.db.ondigitalocean.com"

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

print("connecting to DB:")
print(db_user)
print(db_pass)

# db = mysql.connector.connect(
#   host=host,
#   user=db_user,
#   passwd=db_pass,
#   db="defaultdb",
#   port="25060"
# )

db = mysql.connector.connect(
  host=host,
  user=db_user,
  password=db_pass,
  database="defaultdb",
  port=25060  
)
print(db)
print("CONNECTED TO DB THIS IS GOOD!")


def main(args):

    # print("="*50)
    print("DEBUG TIME BABY:")

    # print(db)

    # cur = db.cursor()
    # print(cur)

    # cur.execute("SELECT * FROM testusers;")
    # result = cur.fetchall()

    # username = args.get('name', None)

    # if username is None:
    #     return {"body": "you need a \'name\' parameter!"}

    # # TODO get data from DB

    # # structure messages into appropriate response
    # response = dict()

    # # data = {"followers": 1234, "following": 5678, "description": "I am an ARTC user who is cool!", "posts": 15,
    # #         "debug": result}
    # response["body"] = data

    # print("="*50)

    return {"body": "hello there"}
