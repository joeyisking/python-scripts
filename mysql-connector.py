import pymysql
conn = pymysql.connect(host='127.0.0.1', 
					   user='root',
                       password='',
                       db='mysql')

cur = conn.cursor()
cur.execute("SELECT * FROM test.contacts")
for response in cur:
    print(response)
cur.close()
conn.close()
