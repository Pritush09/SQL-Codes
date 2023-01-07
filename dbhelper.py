import mysql.connector
import sys

class DBHelper:

    def __init__(self):
        # there are many possibillity of encountering an error while connecting to the databases so we should put it in try except
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="sql-practice")  # this return a connection object which we should store in a variable
            self.mycursor = self.conn.cursor()

        except:
            print("error in connecting with the database")
            sys.exit(0)
        else:
            print("connected")

    def Sign_Up(self,name,email,password):
        # we always use cursor to chat with the databases
        # it has the method called execute in which we pass the query
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit() # u have to do this step after performing every operations
        except:
            return -1
        else:
            return 1

    def search(self,email,password):

        # this is read query yaha par data palat karke ata he aur my cursor me save hota he
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
#hhh@gamil.com

        # here we fetch the data stored in the my coursor and store it in a variable
        data = self.mycursor.fetchall()

        return  data