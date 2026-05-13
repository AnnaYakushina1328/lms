# Схема базы данных LMS

## Таблицы

### Users (Пользователи)
- id: UUID
- email: String (unique)
- password_hash: String
- full_name: String
- role: Enum (STUDENT, TEACHER, ADMIN)
- group_id: ForeignKey (Groups)

### Courses (Курсы)
- id: UUID
- title: String
- description: Text
- teacher_id: ForeignKey (Users)
- created_at: Timestamp

### Lessons (Уроки)
- id: UUID
- course_id: ForeignKey (Courses)
- title: String
- content: Text (Markdown/HTML)
- order: Integer

### Materials (Материалы)
- id: UUID
- lesson_id: ForeignKey (Lessons)
- file_url: String
- type: Enum (PDF, VIDEO, DOC)

### AI_Interactions (Логи ИИ)
- id: UUID
- user_id: ForeignKey (Users)
- lesson_id: ForeignKey (Lessons)
- query: Text
- response: Text
- context_used: Text
