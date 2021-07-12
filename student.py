from flask import Flask, render_template
class Students:
    import sqlite3
    import pandas as pd

    app = Flask(__name__)

    def __init__():
        connection = sqlite3.connect('computer-pride.db')

        return "Wrong credentials"+ str(username)

    @app.route('/students')
    def registerStudent():
        return render_template('students.html')


    def createTables():
        c = connection.cursor()
        c.execute(
            '''
                CREATE TABLE IF NOT EXIST students(
                    username string PRIMARY KEY,
                    fullName text,
                    gender text,
                    password text
                )
            '''
        )

        tables = pd.read_sql("select * FROM sqlite_master where type='tables';", connection)
        print(tables)


    def create(students):
        sql = '''
            INSERT INTO students(username, fullName, gender, password) VALUES(?,?,?,?)
        '''
        
        cur = connection.cursor()
        cur.execute(sql, students)
        connection.commit()

        results = pd.read_sql("SELECT * FROM students", connection)
        print(results)

    def retrieveAll():
        pass

    def retrieveByUsername(username):
        cur = connection.cursor()
        cur.execute("SELECT username FROM students WHERE username="+str(username))

        results = cur.fetchall()

        for x in results:
            print(x)

            
    def update(username, data):
        sql = 'UPDATE students SET fullName = ?, gender = ?, password = ? where username = '+str(username)
        cur = connection.cursor()
        cur.execute(sql, data)
        connection.commit()

        results = pd.read_sql("SELECT * FROM students", connection)
        print(results)

    def delete(username):
        sql = 'DELETE FROM students where username = '+str(username)
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()

        results = pd.read_sql("SELECT * FROM students", connection)
        print(results)


    create(('muth_oni','Muthoni Ngara', 'M', 'abcd'))

    update('muth_oni', ("Muthoni Ngarachu", "F", "ab-cd"))

    delete('muth_oni')

    retrieveAll('muth_oni')
