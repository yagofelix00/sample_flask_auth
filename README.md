# 🔐 sample_flask_auth  
A simple and secure authentication API built with Flask, SQLAlchemy, and MySQL.

---

## 📌 1. Project Overview

`sample_flask_auth` is a lightweight Flask-based authentication system designed to provide user login, logout, password hashing, and role-based access control.  
It serves as a base template for applications that require secure user management and permission rules.

---

## 🚀 2. Features

### 🔑 Authentication
- User login with bcrypt password validation  
- Logout and session cleanup  
- Authentication handled via **Flask-Login**

### 👤 User Management
- Create users  
- Get user by ID  
- Update password  
- Delete users  

### 🔐 Role-Based Access Control
- Each user has a role (`user` or `admin`)  
- Normal users cannot update/delete other accounts  
- Only admins can delete users  
- Users cannot delete themselves  

### 🛡 Security
- Passwords stored as bcrypt hashes  
- Protected routes using `@login_required`  
- Session-based authentication  

---

## 📁 3. Project Structure

