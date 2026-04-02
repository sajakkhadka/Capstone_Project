# Smart Attendance System — Backend

Flask-based REST API backend for the Mobile Facial Recognition Attendance System (Group 29).

## Current Status
- [x] Project structure initialized
- [x] Technology stack finalized
- [x] Database schema designed
- [x] API endpoints planned
- [ ] Database implementation (in progress)
- [ ] Authentication routes (upcoming)
- [ ] Core API routes (upcoming)
- [ ] Firebase integration (upcoming)

## Tech Stack
- Python + Flask
- SQLite (local storage)
- Firebase Realtime Database (session sync)
- Firebase Authentication

## Planned API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/login | User login |
| POST | /auth/logout | User logout |
| POST | /session/start | Teacher starts class |
| POST | /session/end | Teacher ends class |
| POST | /attendance/mark | Mark student attendance |
| GET | /attendance/report | Get attendance report |
| POST | /admin/excuse | Submit excuse request |
| GET | /admin/students | Get all students |

## Database Tables Planned
- users (admin, teacher, student)
- sessions (class sessions)
- attendance_logs (entry/exit timestamps)
- excuse_requests

## Project Structure
smart-attendance-backend/
├── app/
│   ├── routes/       # API route handlers
│   ├── models/       # Database models
│   └── utils/        # Helper functions
├── config.py         # App configuration
└── run.py            # Entry point
```

---

