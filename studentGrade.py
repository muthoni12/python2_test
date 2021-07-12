class studentGrades:
    import sqlite3
    import pandas as pd



    def __init__():
        connection = sqlite3.connect('computer-pride.db')

        return "Wrong credentials"+ str(studentName)

    def createTables():
        c = connection.cursor()
        c.execute(
            '''
                CREATE TABLE IF NOT EXIST studentGrades(
                    studentName string PRIMARY KEY,
                    subject text,
                    scores text,
                    dateTaken text
                )
            '''
        )

        tables = pd.read_sql("select * FROM sqlite_master where type='tables';", connection)
        print(tables)


    def create(studentGrades):
        sql = '''
            INSERT INTO studentGrades(studentName, subject, scores, dateTaken) VALUES(?,?,?,?)
        '''
            
        cur = connection.cursor()
        cur.execute(sql, studentGrades)
        connection.commit()

        results = pd.read_sql("SELECT * FROM studentGrades", connection)
        print(results)

    def retrieveAll():
        pass

    def retrieveByStudentName(studentName):
        cur = connection.cursor()
        cur.execute("SELECT studentName FROM studentGrades WHERE studentName="+str(studentName))

        results = cur.fetchall()

        for x in results:
            print(x)

                
    def update(studentName, data):
        sql = 'UPDATE studentGrades SET subject = ?, scores = ?, dateTaken = ? where studentName = '+str(studentName)
        cur = connection.cursor()
        cur.execute(sql, data)
        connection.commit()

        results = pd.read_sql("SELECT * FROM studentGrades", connection)
        print(results)

    def delete(studentName):
        sql = 'DELETE FROM studentGrades where studentName = '+str(studentName)
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()

        results = pd.read_sql("SELECT * FROM studentGrades", connection)
        print(results)


    create(('Muthoni Ngarachu','Python', '80/100', '14/06/2019'))

    update('Muthoni Ngarachu', ("C#", "89/100", "15/06/2019"))

    delete('Muthoni Ngarachu')

    retrieveAll('Muthoni Ngarachu')


