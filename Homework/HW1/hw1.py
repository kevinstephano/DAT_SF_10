
import json,datetime,sqlite3

if __name__ == "__main__" :
  json_data = open( "ga_hw_logins.json" )
  login_data = json.load( json_data )

  datetime_object_list = []

  for entry in login_data:
    datetime_object_list.append( datetime.datetime.strptime( entry, "%Y-%m-%d %H:%M:%S" ) )

  conn = sqlite3.connect('login.db')

  conn.execute('''CREATE TABLE logins (date text, hour real)''')

  for obj in datetime_object_list:
    insert_str = "INSERT INTO logins VALUES ('" + obj.date().__str__() + "'," + str(obj.time().hour) + ")"
    conn.execute( insert_str )

  conn.commit()

  # Grouping by date,hour and counting up those groups.
  cursor = conn.execute( "SELECT date,hour,COUNT(hour) FROM logins GROUP BY date,hour ORDER BY COUNT(hour) ASC" )
  for row in cursor:
    print row

  conn.close()

