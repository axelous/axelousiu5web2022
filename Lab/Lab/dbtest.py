import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="baumstagramdb"
)

c=db.cursor()
c.execute("INSERT INTO Users (Name, Surname, Email) VALUES (%s, %s, %s);", ('Николай', 'КнигаОписание','book@description.com'))
db.commit()
c.close()
db.close()