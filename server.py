import datetime
import smtplib
from flask import Flask, render_template, request, redirect, url_for
from models import Add_Zimmer, Delete_Zimmer, Delete_Account, Get_All_Zimmers, Login, Specific_Zimmer, Update_Zimmer
from .models.Add_Zimmer import Add_Zimmer


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')

username = "Shira Levi"

# The Home Page
@app.route('/')
def root():
    return render_template('index.html')

"""
@app.route('/index.html', methods=['POST', 'GET'])
def home():
    error = None
    if request.method == 'POST':
        global username
        username = request.form['username']
        if Login.Is_landLord(username):
            return redirect(url_for('schedule'))
        elif Login(username):
            return redirect(url_for('teacher_post_task'))
        else:
            return redirect(url_for('error_login'))
    return render_template('index.html', error=error)
"""
#The 404 page
@app.route('/404.html')
def error_login():
    return render_template('error_login.html')

#The about page
@app.route('/about.html')
def schedule():
    student_name = username
    student_class = schooluder_model.get_class_by_student(student_name)
    data = schooluder_model.get_week_schedule_by_class(student_class)
    day = datetime.datetime.today().weekday()
    hour = datetime.datetime.now().hour
    date = datetime.datetime.today().strftime('%A - %B %d:')
    return render_template('schedule.html', week_schedule=data, day=day + 1, hour=hour, date=date,
                           student_class=student_class)

#The add-Zimmer page
app = Flask(__name__)
@app.route('/add-zimmer', methods=['GET', 'POST'])
def add_zimmer():
    if request.method == 'POST':
        NameZim = request.form['NameZim']
        LocationZim = request.form['LocationZim']
        Area = request.form['Area']
        IsPool = 'IsPool' in request.form
        IsJacuzzi = 'IsJacuzzi' in request.form
        MidweekPrice = request.form['MidweekPrice']
        EndWeekPrice = request.form['EndWeekPrice']
        TypeZim = request.form['TypeZim']
        NumRoom = request.form['NumRoom']
        GeneralSpecific = request.form['GeneralSpecific']
        PhoneLand = request.form['PhoneLand']
        NameLand = request.form['NameLand']
        EmailLand = request.form['EmailLand']

        # add the variable to the def Add-Zimmer in the 'models' directory
        Add_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, PhoneLand, NameLand, EmailLand)

        return redirect(url_for('add-Zimmer.html'))

    return render_template('add-Zimmer.html')

#The contact page
@app.route('/contact.html', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        teacher_name = request.form['teacher_name']
        subject = request.form['subject']
        msg = request.form['msg']
        student_mail = request.form['student_mail']
        password = request.form['password']
        teacher_email = people_model.get_teacher_email_by_name(teacher_name)
        send_email(student_mail, password, teacher_email, subject, msg)
        return redirect(url_for('schedule'))
    return render_template('contacts.html')

#The property-agents page
@app.route('/property-agents.html')
def check():
    global username
    is_done = request.args.get("done")
    task_id = request.args.get("task_id")
    if is_done == 'on':  # mean false
        task_model.update_student_task_is_done(task_id, 0, username)
    else:  # mean true
        task_model.update_student_task_is_done(task_id, 1, username)
    return tasks()

#The property-list page
@app.route('/property-list.html', methods=['GET', 'POST'])
def teacher_post_task():
    error = None
    if request.method == 'POST':
        grade = request.form['grade']
        date = request.form['date']
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        day = date.weekday()
        hour = request.form['hour']
        subject = request.form['subject']
        descr = request.form['descr']
        upload_task_model.insert_task(grade, day, hour, date, descr)
        return redirect(url_for('teacher_post_task'))
    return render_template('teacher_task.html', error=error)

# The property-type page
@app.route('/property-type.html', methods=['GET', 'POST'])
def teacher_post_fun_task():
    error = None
    if request.method == 'POST':
        grade = request.form['grade']
        descr = request.form['descr']
        link = request.form['link']
        upload_fun_task_model.insert_fun_task(grade, descr, link)
        return redirect(url_for('teacher_post_fun_task'))
    return render_template('teacher_fun_task.html', error=error)

#The testimonial page
@app.route('/testimonial.html', methods=['GET', 'POST'])
def teacher_post_lesson():
    error = None
    if request.method == 'POST':
        grade = request.form['grade']
        day = request.form['day']
        hour = request.form['hour']
        subject = request.form['subject']
        zoom_link = request.form['zoom_link']
        schooluder_model.insert_lesson_to_schedule(grade, day, hour, subject, zoom_link)
        return redirect(url_for('teacher_post_lesson'))
    return render_template('teacher_schedule.html', error=error)


if __name__ == '__main__':
    app.run(port=2024)
