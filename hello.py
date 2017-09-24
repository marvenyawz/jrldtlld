import mysql.connector

def mydatabase():
	db = mysql.connector.connect(user='root', password = 'user', host = 'localhost')
	cur = db.cursor()
	datan = 'hello'
	cur.execute("CREATE DATABASE IF NOT EXISTS {} ".format(datan))
	cur.execute("USE {}".format(datan))
	cur.execute("""CREATE TABLE IF NOT EXISTS studentinformation
	(
	studentid varchar(9) NOT NULL,
	firstname varchar(20) NOT NULL,
	lastname varchar(20) NOT NULL,
	sex char(1) NOT NULL,
	course varchar(4) NOT NULL,
	PRIMARY KEY(studentid))""")
	cur.close()
	db.close()

class student:
    def __init__(self,firstName,lastName,idnumber,course,sex):
        self.idnumber = idnumber
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
        self.sex = sex

    def add(self):
    	db = mysql.connector.connect(user = 'root', password = 'user', host = 'localhost', database = 'hello')
    	cur = db.cursor()

    	sql = """INSERT INTO studentinformation(studentid,firstname,lastname,sex,course) \
                VALUES('%s','%s','%s','%c','%s')""" % \
                (self.idnumber,self.firstName,self.lastName,self.sex,self.course)
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()    

def update(operation,idnumber):
	db = mysql.connector.connect(user = 'root', password = 'user', host = 'localhost', database = 'hello')
	cur = db.cursor()
	if operation == 'idnumber':
		value = raw_input("Enter the new idnumber: ")
		cur.execute("""UPDATE studentinformation SET studentid = %s WHERE studentid = %s""",(value,idnumber))
		db.commit()
	elif operation == 'firstname':
		value = raw_input("Enter the new firstname: ")
		cur.execute("UPDATE studentinformation SET firstname = %s WHERE studentid = %s""",(value,idnumber))
		db.commit()
		cur.close()
		db.close()
	elif operation == 'lastname':
		value = raw_input("Enter the new lastname: ")
		cur.execute("UPDATE studentinformation SET lastname = %s WHERE studentid = %s""",(value,idnumber))
		db.commit()
		cur.close()
		db.close()
	elif operation == 'sex':
		value = raw_input("Enter the new sex: ")
		cur.execute("UPDATE studentinformation SET sex = %s WHERE studentid = %s""",(value,idnumber))
		db.commit()
		cur.close()
		db.close()
	elif operation == 'course':
		value = raw_input("Enter the new course: ")
		cur.execute("UPDATE studentinformation SET course = %s WHERE studentid = %s""",(value,idnumber))
		db.commit()
		cur.close()
		db.close()
	else:
		print("Invalid Operation!")

def delete(idnumber):
	db = mysql.connector.connect(user = 'root', password = 'user', host = 'localhost', database = 'hello')
	cur = db.cursor()
	cur.execute("DELETE FROM studentinformation WHERE studentid = %s",(idnumber,))
	db.commit()
	cur.close()
	db.close()

def search(idnumber):
	db = mysql.connector.connect(user = 'root', password = 'user', host = 'localhost', database = 'hello')
	cur = db.cursor()
	cur.execute("SELECT * FROM studentinformation WHERE studentid = %s",(idnumber,))
	result = cur.fetchall()
	return result
	
def opera ():
    print ("\nOperations:\n\nadd\nupdate\nsearch\ndelete\n")

while(True):
	opera()
	print("Basic Student Database")
	operations = raw_input ('\nselect an Operation: ')
	mydatabase()
	if (operations == 'add'):
		firstname = raw_input('Ecd C:\Python27nter firstname: ')
		lastname = raw_input('Enter lastname: ')
		idnumber = raw_input('Enter id number: ')
		sex = raw_input('Enter sex: ')
		course = raw_input ('Enter course: ')
		stud = student (firstname,lastname,idnumber,course,sex)
		stud.add()

	elif (operations == 'search'):
		searchid = raw_input ('\nEnter the id no.: ')
		print(search (searchid))

	elif(operations == 'update'):
		oper = raw_input("\nWhat do you want to update? (idnumber,firstname,lastname,sex,course): ")
		idnumber = raw_input("\nEnter the idnumber of the student: ")
		update(oper,idnumber)

	elif (operations == 'delete'):
		searchid = raw_input ('\nEnter the idnumber of the data to be deleted: ')
		delete(searchid)

	else:
		print("\nInvalid Operation!")
		print_db()

	choice = raw_input("\nWant to try again? yes or no: ")
	if (choice == "no"):
			break