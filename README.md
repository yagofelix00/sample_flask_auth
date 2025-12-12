




# 🔐 sample_flask_auth  
A simple and secure authentication API built with Flask, SQLAlchemy, and MySQL.

---

## 📌 1. Project Overview

`sample_flask_auth` is a lightweight Flask-based authentication system designed to provide user login, logout, password hashing, and role-based access control.  
It serves as a base template for applications that require secure user management and permission rules.

---

## 🚀 2. Features

## 🚀 2. Features

### 🔑 Authentication

- Login with username + password

- Password hashing and validation using bcrypt

- Session management with Flask-Login

- Logout and session cleanup

### 👤 User Management (CRUD)

- Create new users

- Read user info by ID

- Update user password

- Delete users (admin only)

### 🔐 Role-Based Access Control

- Each user has a role: user or admin

- Users cannot update or delete other accounts

- Only admin can delete users

- Prevention of self-deletion for safety

### 🛡️ Security

- Passwords stored as bcrypt hashes

- Auth-protected endpoints using @login_required

- Session-based authentication (secure cookies)

- Restricted admin-only operations

---

## 📁 3. Project Structure

```

sample_flask_auth/
│
├── models/
│   └── user.py
│
├── database.py
├── app.py
├── docker-compose.yml
├── requirements.txt
└── README.md

````

---

## 🖼️ 4. Output Example

You may add an image of a terminal request or API response here.

Example placeholder:

![API Example](./assets/api_example.png)

*(Replace with your own screenshot.)*

---

## ⚙️ 5. How to Run

### **1. Clone the repository**
```bash
git clone https://github.com/your-username/sample_flask_auth.git
cd sample_flask_auth
````

### **2. Start MySQL using Docker**

```bash
docker-compose up -d
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the application**

```bash
python app.py
```

The server will be available at:
📍 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ 6. Technologies Used

* **Python 3.11+**
* **Flask**
* **Flask-Login**
* **SQLAlchemy**
* **MySQL / PyMySQL**
* **bcrypt**
* **Docker & Docker Compose**

---

## 📝 7. Notes

* Make sure Docker is running before starting the application.
* The default MySQL credentials are located inside `docker-compose.yml`.
* The `SECRET_KEY` should be changed before deploying to production.
* This project is intended for learning and prototyping.

---

## 🔮 8. Future Improvements

* JWT token authentication
* Password reset flow
* Email verification
* Logging and audit trail
* Two-factor authentication (2FA)
* CI/CD pipeline
* Rate limiting for login attempts
* Admin dashboard
* Unit tests + integration tests

---

## 💼 9. Business Impact (Optional)

This authentication module can serve as a reusable foundation for larger systems that require secure user handling.
By centralizing authentication logic, teams can:

* Reduce development time for new applications
* Standardize security practices
* Improve maintainability of user-related features
* Scale easily by integrating JWT or microservices


---

## 👨‍💻 10. Author

**Yago Félix**
Junior Python Backend Developer
GitHub: [https://github.com/yagofelix00](https://github.com/yagofelix00)

---

