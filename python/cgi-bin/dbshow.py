import mysql.connector


print ("Connecting to MySQL....");

try:
  cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='3semi2022')
except mysql.connector.Error as err:
  print("DB connection error {}".format(err) )

cur = cnx.cursor(dictionary=True)

cur.execute("SELECT sentence, posinega, score FROM sentiment")

for row in cur:
    print(row["sentence"], row["posinega"], row["score"])

cur.close()

cnx.close()

print("Exit.")