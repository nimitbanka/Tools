from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/index', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/index')
        except:
            return 'There was a issue'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/index')

    except:
        return 'There was a problem'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/index')
        except:
            return 'there was an issue'
    else:
        return render_template("update.html", task= task)

@app.route('/')
def mainpage():
    return render_template("main.html")

@app.route('/index')
def taskmanager():
    return render_template("index.html")
@app.route('/calculator')
def calculator():
    return render_template("calc.html")
@app.route('/conversion')
def conversion():
    return render_template("conversion.html")
@app.route('/length')
def length():
    return render_template("length.html")
@app.route('/miles', methods=['POST','GET'])
def miles():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('miles') !=''):
            Miles = float(request.form.get("miles"))
            answer1=Miles
            answer2=round(Miles/0.62137,2)
            answer3=round(Miles/0.00062137)
            answer4=round(Miles*5280.0,2)
            answer5=round(Miles* 63360,2)
            answer6=round(Miles/0.0000062137,2)
            answer7=round(Miles/0.00000062137,2)
            answer8=round(Miles* 1760.0,2)
    return render_template("miles.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)
    
@app.route('/kilometer', methods=['POST','GET'])
def kilometer():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('kilometer') !=''):
            Kilometer = float(request.form.get("kilometer"))
            answer1= round(Kilometer*0.621371,2)
            answer2= Kilometer
            answer3=round(Kilometer*1000,2)
            answer4=round(Kilometer* 3280.8,2)
            answer5=round(Kilometer* 39370.1 ,2)
            answer6=round(Kilometer*100000,2)
            answer7=round(Kilometer*1000000,2)
            answer8=round(Kilometer*1093.61,2)
    return render_template("kilometer.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/meter', methods=['POST','GET'])
def meter():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('meter') !=''):
            Meter = float(request.form.get("meter"))
            answer1= round(Meter*0.000621371,2)
            answer2= round(Meter*0.001,2)
            answer3=Meter
            answer4=round(Meter* 3.28084,2)
            answer5=round(Meter* 39.3701 ,2)
            answer6=round(Meter*100.000,2)
            answer7=round(Meter*1000.000,2)
            answer8=round(Meter*1.09361,2)
    return render_template("meter.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/foot', methods=['POST','GET'])
def foot():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('foot') !=''):
            Feet = float(request.form.get("foot"))
            answer1= round(Feet*0.000189394,2)
            answer2= round(Feet*0.0003048,2)
            answer3=round(Feet*0.3048,2)
            answer4= Feet
            answer5=round(Feet* 12 ,2)
            answer6=round(Feet*30.48,2)
            answer7=round(Feet*304.8,2)
            answer8=round(Feet*0.333333,2)
    return render_template("foot.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/inches', methods=['POST','GET'])
def inches():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('inches') !=''):
            inches = float(request.form.get("inches"))
            answer1= round(inches/63360,2)
            answer2= round(inches/39370,2)
            answer3=round(inches*0.0254,2)
            answer4= round(inches/12,2)
            answer5=inches
            answer6=round(inches*2.54,2)
            answer7=round(inches*25.4,2)
            answer8=round(inches/36,2)
    return render_template("inches.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/centi', methods=['POST','GET'])
def centi():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('centi') !=''):
            centi = float(request.form.get("centi"))
            answer1= round(centi/160934,2)
            answer2= round(centi/100000,2)
            answer3=round(centi*0.01,2)
            answer4= round(centi/30.48,2)
            answer5=round(centi/2.54,2)
            answer6=centi
            answer7=round(centi*10,2)
            answer8=round(centi/91.44,2)
    return render_template("centi.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/mili', methods=['POST','GET'])
def mili():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('mili') !=''):
            mili = float(request.form.get("mili"))
            answer1= round(mili/1609340,2)
            answer2= round(mili/1000000,2)
            answer3=round(mili*0.001,2)
            answer4= round(mili/304.8,2)
            answer5=round(mili/25.4,2)
            answer6=round(mili/10,2)
            answer7=mili
            answer8=round(mili/914.4,2)
    return render_template("mili.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/yard', methods=['POST','GET'])
def yard():
    answer1=''
    answer2=''
    answer3=''
    answer4=''
    answer5=''
    answer6=''
    answer7=''
    answer8=''
    if request.method=="POST":
        if(request.form.get('yard') !=''):
            yard = float(request.form.get("yard"))
            answer1= round(yard/1760,2)
            answer2= round(yard/1094,2)
            answer3=round(yard*0.9144,2)
            answer4= round(yard*3,2)
            answer5=round(yard*36,2)
            answer6=round(yard*91.44,2)
            answer7=round(yard*914.4,2)
            answer8=yard
    return render_template("yard.html",answer1=answer1, answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8)

@app.route('/weight', methods=['POST','GET'])
def weight():
    answer1 =''
    answer2 =''
    if request.method=="POST":
        if(request.form.get('Kg') != ''):
            Kg = float(request.form.get('Kg'))
            answer1 = Kg
            answer2 = Kg * 2.2046bbb
        elif(request.form.get('pound')!=''):
            Pound = float(request.form.get('pound'))
            answer1 = Pound/2.2046
            answer2 = Pound
        else:
            answer1 = 'none'
            answer2 = 'none'
    return render_template("weight.html",answer1=answer1, answer2=answer2)


@app.route('/area')
def area():
    return render_template("area.html")


@app.route('/temperature', methods=['POST','GET'])
def temperature():
    answer1 =''
    answer2 =''
    answer3 =''
    if request.method=="POST":
        if (request.form.get('celsius') !=''):
            Celsius = float(request.form.get('celsius'))
            answer1 = Celsius
            answer2 = (Celsius * (9/5))+32
            answer3 = Celsius + 273.15
        elif(request.form.get('fahrenheit') !=''):
            Fahrenheit = float(request.form.get('fahrenheit'))
            answer1 = (Fahrenheit - 32)*(5/9)
            answer2 = Fahrenheit
            answer3 = ((Fahrenheit - 32)*(5/9)) +273.15
        elif(request.form.get('kelvin') !=''):
            Kelvin = float(request.form.get('kelvin'))
            answer1 = Kelvin - 273.15
            answer2 = ((Kelvin - 273.15)*(9/5))+32
            answer3 = Kelvin
        else:
            answer1 = 'none'
            answer2 = 'none'
            answer3 = 'none'
    return render_template("temperature.html",answer1=answer1, answer2=answer2, answer3=answer3)

@app.route('/bmi', methods=['POST', 'GET'])
def cal_bmi():
    bmi=''
    type=''
    none=''
    if request.method=="POST" and 'weight' in request.form and 'height' in request.form:
        try:
            Weight = float(request.form.get('weight'))
            Height = float(request.form.get('height'))
            bmi = round(Weight/((Height/100)**2),2)
            if(bmi<18.5):
                type='UNDERWEIGHT'
            elif(bmi<24.9):
                type='Normal'
            elif(bmi<29.9):
                type='OVERWEIGHT'
            else:type='OBESE'
        except:
            none='Value is not inserted'
    return render_template("BMICalculation.html",bmi=bmi,type=type,none=none)
    
if __name__ == "__main__":
    app.run(debug=True) 