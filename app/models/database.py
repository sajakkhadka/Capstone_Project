from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, teacher, student
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.email}>'


class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    room = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Session {self.subject}>'


class AttendanceLog(db.Model):
    __tablename__ = 'attendance_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
    entry_time = db.Column(db.DateTime, nullable=True)
    exit_time = db.Column(db.DateTime, nullable=True)
    total_time = db.Column(db.Integer, nullable=True)  # in minutes
    status = db.Column(db.String(20), default='absent')  # present or absent
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<AttendanceLog student:{self.student_id} session:{self.session_id}>'


class ExcuseRequest(db.Model):
    __tablename__ = 'excuse_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
    reason = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ExcuseRequest student:{self.student_id}>'


