
# RV Maintenance Tracker

A Flask backend API for tracking RV maintenance records.


## Setup (Windows / PowerShell)

1. Clone the repository from GitHub and open the project folder.

   ```powershell
   git clone https://github.com/AnadiaDragoste/rv-backend.git
   cd rv-backend
   ```

2. Create a virtual environment for the project.

   ```powershell
   python -m venv .venv
   ```

3. Activate the virtual environment. If PowerShell blocks the script, temporarily allow it for the current terminal session.

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the project dependencies from requirements.txt.

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create a local `.env` file using `.env.example` as a starting point and replace the placeholder JWT secret with your own secret.

   ```powershell
   Copy-Item .env.example .env
   ```

6. Start the Flask development server.

   ```powershell
   python -m flask --app "rv_tracker:create_app('development')" run
   ```


## Environment variables

Before running the app, copy `.env.example` to `.env` and update the values for your local setup.

```powershell
Copy-Item .env.example .env
```

The project uses these environment variables:

- `DATABASE_URL`: The database connection used during development. It currently uses a local SQLite database.
- `TEST_DATABASE_URL`: The database connection used for testing. It uses an in-memory SQLite database.
- `PRODUCTION_DATABASE_URL`: The database connection used when the app runs in production. Replace the placeholder with the actual production database URL.
- `JWT_SECRET_KEY`: A long, random secret string used to sign authentication tokens. Replace the placeholder with your own secret and keep it private.

The `.env` file is ignored by Git so private settings and secrets aren't uploaded to GitHub.


## Database migrations

This project uses Flask-Migrate to manage changes to the database structure.

I haven't created any database models or migrations yet. Once models are added, I'll use these commands in PowerShell to manage database changes.

1. Initialize the migrations folder. This only needs to be done once for the project.

   ```powershell
   python -m flask --app "rv_tracker:create_app('development')" db init
   ```

2. Generate a new migration after adding or changing database models.

   ```powershell
   python -m flask --app "rv_tracker:create_app('development')" db migrate -m "Add maintenance records table"
   ```

3. Apply the migration to update the database.

   ```powershell
   python -m flask --app "rv_tracker:create_app('development')" db upgrade
   ```

After the migrations folder has been initialized, I only need to generate and apply new migrations when the database models change.
