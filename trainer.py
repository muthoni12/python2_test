from flask import Flask, render_template
class Trainers:
    import sqlite3
    import pandas as pd

    app = Flask(__name__)

    def __init__():
        connection = sqlite3.connect('computer-pride.db')

        return "Wrong credentials"+ str(username)

    @app.route('/studentGrades')
    def newStudentScores():
        return render_template('studentGrades.html')


    @app.route('/trainerDashboard')
    def new_studentGrades():
        return render_template('trainerDashboard.html')

    def createTables():
        c = connection.cursor()
        c.execute(
            '''
                CREATE TABLE IF NOT EXIST trainers(
                    username string PRIMARY KEY,
                    trainerName text,
                    password text
                )
            '''
        )
 

        tables = pd.read_sql("select * FROM sqlite_master where type='tables';", connection)
        print(tables)

    def create(trainers):
        sql = '''
            INSERT INTO trainers(username, trainerName, password) VALUES(?,?,?)
        '''
        
        cur = connection.cursor()
        cur.execute(sql, trainers)
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection)
        print(results)

    def retrieveAll():
        pass

    def retrieveByUsername(username):
        cur = connection.cursor()
        cur.execute("SELECT username FROM trainers WHERE username="+str(username))

        results = cur.fetchall()

        for x in results:
            print(x)

            
    def update(username, data):
        sql = 'UPDATE trainers SET trainerName = ?, password = ? where username = '+str(username)
        cur = connection.cursor()
        cur.execute(sql, data)
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection)
        print(results)

    def delete(username):
        sql = 'DELETE FROM trainers where username = '+str(username)
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection)
        print(results)


    create(('s.tomashi','Sam Tomashi', '1234'))

    update('s.tomashi', ("Samuel Tomashi", "12@34"))

    delete('s.tomashi')

    retrieveAll('s.tomashi')