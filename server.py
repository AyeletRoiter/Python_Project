
from flask import Flask, render_template, request, redirect, url_for, flash, session

from models.Add_Zimmer import Add_Zimmer
from models.Get_All_Zimmers import get_all_zimers
from models.Login import Is_landLord

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='Template')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Login Page - Route and function
@app.route('/Login.html')
def login():
    return render_template('Login.html')  # Assuming you have a login.html template

# Handling Login Form Submission
@app.route('/Login.html', methods=['POST'])
def login_post():
    name_land = request.form['username']
    password = request.form['password']

    if Is_landLord(name_land, password):
        # Store the username in session
        session['User_name'] = name_land
        flash('Login successful!', 'success')
        return redirect(url_for('root'))
    else:
        flash('Invalid username or password. Please try again.', 'error')
        return render_template('Login.html')

# The Home Page
@app.route('/')
def root():
    zimers_list = get_all_zimers()  # קבלת כל הצימרים מה-DB
    user_name = session.get('User_name', 'Guest')  # מקבל את שם המשתמש מה-session או ברירת מחדל 'Guest'
    return render_template('index.html', zimers_list=zimers_list, user_name=user_name)

@app.route('/index.html')
def home():
    zimers_list = get_all_zimers()  # קבלת כל הצימרים מה-DB
    user_name = session.get('User_name', 'Guest')  # מקבל את שם המשתמש מה-session או ברירת מחדל 'Guest'
    return render_template('index.html', zimers_list=zimers_list, user_name=user_name)

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# The about page
@app.route('/about.html')
def page_about():
    return render_template('about.html')

# The add-Zimmer page
@app.route('/add-Zimmer.html', methods=['GET', 'POST'])
def add_zimmer():
    if request.method == 'POST':
        # אחסן את הפרמטרים מהבקשה
        NameZim = request.form['NameZim']
        LocationZim = request.form['LocationZim']
        Area = request.form['Area']
        IsPool = request.form['IsPool']
        IsJacuzzi = request.form['IsJacuzzi']
        MidweekPrice = request.form['MidweekPrice']
        EndWeekPrice = request.form['EndWeekPrice']
        TypeZim = request.form['TypeZim']
        NumRoom = request.form['NumRoom']
        GeneralSpecific = request.form['GeneralSpecific']
        PhoneLand = request.form['PhoneLand']
        NameLand = request.form['NameLand']
        EmailLand = request.form['EmailLand']
        ImageURL = request.form['ImageURL']

        # קרא לפונקציה להוספת זימר (עדיין לא מוגדרת)
        Add_Zimmer(NameZim, LocationZim, Area, IsPool, IsJacuzzi, MidweekPrice, EndWeekPrice, TypeZim, NumRoom, GeneralSpecific, PhoneLand, NameLand, EmailLand)

        return redirect(url_for('root'))

    return render_template('add-Zimmer.html')


 #The contact page
@app.route('/contact.html')
def contacts():
    return render_template('contact.html')

 #The property-agents page
@app.route('/property-agent.html')
def landLords():
    return render_template('property-agent.html')


# The property-list page
@app.route('/property-list.html', methods=['GET'])
def property_list():
    try:
        zimers = get_all_zimers()
        print(f"zimers: {zimers}")  # הדפסת הצימרים ללוגים
        return render_template('property-list.html', zimers_list=zimers)
    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500

 # The property-type page
@app.route('/property-type.html')
def teacher_post_fun_task():

     return render_template('property-type.html')

# #The testimonial page
# @app.route('/testimonial.html', methods=['GET', 'POST'])
# def teacher_post_lesson():
#     error = None
#     if request.method == 'POST':
#         grade = request.form['grade']
#         day = request.form['day']
#         hour = request.form['hour']
#         subject = request.form['subject']
#         zoom_link = request.form['zoom_link']
#         schooluder_model.insert_lesson_to_schedule(grade, day, hour, subject, zoom_link)
#         return redirect(url_for('teacher_post_lesson'))
#     return render_template('teacher_schedule.html', error=error)
#

if __name__ == '__main__':
    app.run(port=2024, debug=True)
