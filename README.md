# Tournament Management Application

A comprehensive Django-based web application for organizing and managing gaming tournaments. This platform allows users to create tournaments, participate in them, and manage their gaming profiles.

## Features

- **User Authentication**: Register, login, and manage user profiles
- **Tournament Creation**: Create and manage gaming tournaments with detailed information
- **Tournament Participation**: Join tournaments as individual players or teams
- **Profile Management**: Customize user profiles with gaming information and social media links
- **Responsive Design**: Modern UI with Bootstrap 4 styling
- **PDF Generation**: Generate tournament reports and documents
- **Multi-language Support**: Arabic text support with proper text reshaping
- **Media Management**: Upload and manage profile pictures and tournament banners

## Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4
- **Forms**: Django Crispy Forms
- **PDF Generation**: Django Easy PDF, ReportLab
- **Image Processing**: Pillow
- **Phone Fields**: Django Phone Field
- **Country Selection**: Django Countries
- **Arabic Text Support**: Arabic Reshaper, Python Bidi

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd tournie-app
```

### 2. Set up a Virtual Environment (Recommended)

First, let's create and activate a virtual environment to isolate your project dependencies:

```bash
# Create a virtual environment
python -m venv myEnv

# Activate it (Windows)
myEnv\Scripts\activate

# Or if you're using Git Bash or WSL
source myEnv/Scripts/activate
```

### 3. Install Dependencies

Once your virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables

I notice your project uses environment variables for sensitive data. Create a `.env` file in your project root with:

```env
SECRET_KEY=your-secret-key-here
EMAIL=your-email@gmail.com
PASSWORD=your-app-password
```

### 5. Run Database Migrations

Set up your database by running migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

Run your Django development server:

```bash
python manage.py runserver
```

Your application should now be running at http://127.0.0.1:8000/ or http://localhost:8000/

## Project Structure

```
tournie-app/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database
├── myEnv/                   # Virtual environment
├── tournament/              # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
└── part/                    # Main Django app
    ├── models.py            # Database models
    ├── views.py             # View functions and classes
    ├── forms.py             # Django forms
    ├── admin.py             # Admin configuration
    ├── urls.py              # App URL patterns
    ├── templates/           # HTML templates
    ├── static/              # Static files (CSS, JS, images)
    └── migrations/          # Database migrations
```

## Models

### Profile
- User profile information including gaming preferences
- Social media links (YouTube, Instagram, Facebook, Twitter)
- Profile picture and achievements

### Organize
- Tournament creation and management
- Tournament details (name, organizer, discipline, size, prize pool)
- Social media links for tournaments
- Country selection and banner images

### Participating
- Tournament participation records
- Team/player registration information
- Contact details and in-game names (IGNs)
- Team logos and tournament associations

## Key Features Explained

### Tournament Management
- **Create Tournaments**: Users can create tournaments with detailed information
- **Edit/Delete**: Tournament creators can modify or delete their tournaments
- **Browse Tournaments**: View all available tournaments on the platform

### Participation System
- **Team Registration**: Register teams with multiple players
- **Individual Registration**: Register as individual players
- **Tournament Association**: Link participants to specific tournaments

### User Profiles
- **Gaming Information**: Track favorite games and achievements
- **Social Integration**: Connect gaming profiles with social media
- **Profile Customization**: Upload profile pictures and manage personal information

## Usage

1. **Register**: Create a new account or login to existing account
2. **Create Tournament**: Use the organizer section to create new tournaments
3. **Participate**: Browse available tournaments and register as a player or team
4. **Manage Profile**: Update your gaming profile and social media links
5. **Admin Panel**: Access Django admin for advanced management (if superuser)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email bakadiyayash@gmail.com or create an issue in the repository.

## Acknowledgments

- Django framework and community
- Bootstrap for UI components
- All contributors and users of this application
