from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL




app=Flask(__name__)

app.secret_key='india' # write as secreat password
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='hr_erp_db'

mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

# admin_dashboard_route

@app.route('/admin_home', methods=['GET', 'POST'])
def admin_home():
    # If POST, process login
    if request.method == 'POST':
        i = request.form.get('txtUsername')
        p = request.form.get('txtPassword')
        # simple hard-coded check (you can replace with DB check)
        if i == 'shreyansh' and p == '12345':
            session['Name'] = 'Shreyansh'
            # session['username'] = i
            return render_template('admin_home.html')
        else:
            msg = 'incorrect username and password'
            return render_template('adminlogin.html', msg=msg)
    elif request.method == 'GET':
        session['Name']='Shreyansh'
        return render_template('admin_home.html')




@app.route('/admin_addemployee')
def admin_addemploy():
    return render_template('admin_addemployee.html')


@app.route('/admin_showemployee')
def admin_showemploy():
    cur=mysql.connection.cursor()
    cur.execute('select empid,empname,designation,salary from registration')
    emplist=cur.fetchall()
    return render_template('admin_showemployee.html',emplist=emplist)

@app.route('/admin_searchemployee')
def admin_searchemploy():
    return render_template('admin_searchemployee.html')

@app.route('/admin_logout')
def admin_logout():
    session['Name']=None
    return render_template('adminlogin.html')

@app.route('/save' ,methods=['post'])
def save():
    i=request.form['txtempid']
    n=request.form['txtname']
    e=request.form['txtemail']
    m=request.form['txtmobile']  # fixed from extmobile to txtmobile
    d=request.form['txtdesignation']
    s=request.form['txtsalary']

    #database connection
    cur=mysql.connection.cursor()
    #quary specification\
    cur.execute('insert into registration(empid,empname,email,mobile,designation,salary) values(%s,%s,%s,%s,%s,%s)',(i,n,e,m,d,s))
    #transiction save and commit
    mysql.connection.commit()
    #database connection close
    cur.close()

    return render_template('admin_addemployee_success.html')


@app.route('/admin_emp_profile')
def admin_emp_profile():
    eid=request.args.get('eid')
    cur=mysql.connection.cursor()   
    cur.execute("select* from registration where empid=%s",(eid,)) 
    empdetails=cur.fetchone()
    return render_template('admin_emp_profile.html',empdetails=empdetails)

@app.route('/admin_emp_update', methods=['post'])
def admin_emp_update():
    i=request.form['txtempid']
    n=request.form['txtname']
    e=request.form['txtemail']
    m=request.form['txtmobile']  # fixed from extmobile to txtmobile
    d=request.form['txtdesignation']
    s=request.form['txtsalary']

    #database connection
    cur=mysql.connection.cursor()
    #quary specification\
    cur.execute('update registration set empname=%s,email=%s,mobile=%s,designation=%s,salary=%s where empid=%s',(n,e,m,d,s,i))
    #transiction save and commit
    mysql.connection.commit()
    #database connection close
    cur.close()
    return render_template('admin_emp_update_success.html')


@app.route('/admin_employ_delete')
def admin_emp_delete():
    eid=request.args.get('eid')
    cur=mysql.connection.cursor()
    cur.execute("delete from registration where empid=%s",(eid,))
    mysql.connection.commit()
    cur.close()    
    return render_template('admin_emp_delete_success.html')


@app.route('/admin_emp_search_result' ,methods=['post'])
def admin_emp_search_result():
    ename=request.form['txtname']
    cur=mysql.connection.cursor()
    cur.execute('select * from registration where empname like %s',("%" + ename + "%",))
    empdetails=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('admin_emp_search_result.html',empdetails=empdetails)

app.run(debug=True, port=5000)
