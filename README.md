# HR ERP System

A simple **Human Resource Employee Management System** built with **Flask** and **MySQL**.  
This web application enables an admin to manage employee records — including adding, updating, viewing, searching, and deleting employee details.

---

## 🚀 Features

- 🔐 **Admin Login** – Basic authentication for admin access.
- 👨‍💼 **Employee Management**
  - Add new employees
  - Update employee details
  - Delete employee records
  - Search employees by name
  - View all employees
- 📜 **Dynamic Templates** – Uses Flask Jinja2 templates for rendering UI.
- 🧩 **Database Integration** – MySQL backend for storing employee data.
- 🧰 **Session Management** – Flask session used for simple authentication control.

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | Flask (Python) |
| Database | MySQL |
| Frontend | HTML, CSS, Jinja2 Templates |
| Server | Flask Development Server |

---

## ⚙️ Installation & Setup

Follow these steps to set up and run the HR ERP System on your local machine.

---

### **2️⃣ Create and activate a virtual environment**

Create an isolated Python environment to manage project dependencies.

#### 🪟 For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 For Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3️⃣ Install dependencies**

Install all the required Python packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

#### 📦 Example `requirements.txt` content:
```
blinker==1.9.0
click==8.3.0
colorama==0.4.6
Flask==3.1.2
Flask-MySQLdb==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
mysql==0.0.3
mysqlclient==2.2.7
Werkzeug==3.1.3
```

---

### **4️⃣ Configure the MySQL database**

1. Open MySQL command line or MySQL Workbench.  
2. Create a new database:
   ```sql
   CREATE DATABASE hr_erp_db;
   ```
3. Then create a table called `registration`:
   ```sql
   CREATE TABLE registration (
     empid VARCHAR(10) PRIMARY KEY,
     empname VARCHAR(100),
     email VARCHAR(100),
     mobile VARCHAR(15),
     designation VARCHAR(100),
     salary DECIMAL(10,2)
   );
   ```

---

### **5️⃣ Update the Flask database configuration**

Open your main Flask app file (`main.py`) and verify these settings:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hr_erp_db'
```

> ⚠️ **Security Tip:**  
> Do not hardcode credentials in production. Use environment variables or a `.venv` file for sensitive data.

---

### **6️⃣ Run the Flask application**

Start the Flask development server with:
```bash
python main.py
```

Now, open your browser and visit:
```
http://127.0.0.1:5000/
```

If everything is configured correctly, you’ll see the **HR ERP System** homepage running successfully 🎉.

---

## 🧑‍💻 Default Admin Login

| Field | Value |
|--------|--------|
| Username | shreyansh |
| Password | 12345 |

---

## 📂 Project Structure

```
hr_erp_system/
│
├── templates/
│   ├── index.html
│   ├── adminlogin.html
│   ├── admin_home.html
│   ├── admin_addemployee.html
│   ├── admin_showemployee.html
│   ├── admin_emp_profile.html
│   ├── admin_emp_search_result.html
│   ├── admin_emp_update_success.html
│   ├── admin_emp_delete_success.html
│   └── ...
│
├── static/
│   ├── css/style.css
│   
│
├── python.py   # Main Flask app
├── requirements.txt
└── README.md
```

---

## 🧠 Application Flow (Routes Summary)

| Route | Method | Description |
|-------|---------|-------------|
| `/` | GET | Home page |
| `/adminlogin` | GET | Admin login page |
| `/admin_home` | GET/POST | Admin dashboard (after login) |
| `/admin_addemployee` | GET | Add new employee |
| `/save` | POST | Save new employee data |
| `/admin_showemployee` | GET | Show all employees |
| `/admin_emp_profile` | GET | Display employee details |
| `/admin_emp_update` | POST | Update employee information |
| `/admin_employ_delete` | GET | Delete employee record |
| `/admin_searchemployee` | GET | Search employee form |
| `/admin_emp_search_result` | POST | Display search results |
| `/admin_logout` | GET | Log out admin |

---

## 🛡️ Security Notes

- Replace hardcoded admin credentials with a secure login system.
- Use hashed passwords in your database.
- Hide sensitive data (DB password, secret key) in environment variables:
  ```bash
  set FLASK_SECRET_KEY=your_secret_key
  set MYSQL_PASSWORD=your_password
  ```
- Always sanitize user inputs to avoid SQL injection or XSS.

---

## 🧠 Future Enhancements

- Add employee photo uploads.
- Implement role-based access control (HR, Manager, Employee).
- Add employee attendance & payroll modules.
- Build RESTful APIs for external integration.

---

## 👤 Author

**Shreyansh Kandu**  
📧 [shreyansh kandu](mailto:shreyanshkandu@gmail.com)

---


