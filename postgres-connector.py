import psycopg2

host = input("ssh user and host: ")
password = input("password: ")


os.system("ssh" + name+ " -fNL 5432:localhost:5432 -p" + password)

conn = psycopg2.connect(database='yourdb', user='dbuser', password='abcd1234', host='server', port='5432', sslmode='require')

cur = conn.cursor()
cur.execute("SELECT * FROM test.contacts")
for response in cur:
    print(response)
cur.close()
conn.close()

