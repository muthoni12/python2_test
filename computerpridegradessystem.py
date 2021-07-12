from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import make_response
class computerPrideGradesSystem:
    from trainer import Trainers
    from student import Students
    from studentGrade import studentGrades

    app = Flask(__name__)

    def __init__():
        pass


    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/login', methods= ['POST'])
    def login():
        user = {
            "username": "noni",
            "password": "ab-cd"
        }

        username = request.form['username']
        password = request.form['password']
        
        if username == user['noni']:
            if password == user['ab-cd']:
                resp = make_response(redirect(url_for('studentGrades')))
                resp.set_cookie('grades_sytem_username', username)
                return resp

        return "Wrong credentials"+ str(username)


    @app.route('/studentGrades')
    def studentGrades():
        username = request.cookies.get('grades_system_username')
        if username == None:
            return redirect(url_for('index'))

        exams = [
            {
                "subject": "Python",
                "scores": "20/25",
                "dateTaken": "1-04-2021"

            },
            {
                "subject": "C#",
                "scores": "25/25",
                "dateTaken": "16-04-2021"

            },
            {
                "subject": "Java Script",
                "scores": "20/100",
                "dateTaken": "20-04-2021"

            },
        ]


    if __name__ == '__main__':
        app.run(debug = True)