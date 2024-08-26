# Django Blog Project

This project is a simple blog platform built using Django. It allows users to read posts, leave comments, perform searches, and carry out other functionalities.

## Installation

Follow these instructions to set up the project:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mirmakhmudoff/reader-blog-project.git
    cd djangoProject
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # MacOS/Linux
    env\Scripts\activate  # Windows
    ```

3. **Install Requirements:**

    Install the necessary libraries using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    Apply migrations to create the database structure:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser:**

    Create a superuser to access the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. **Collect Static Files:**

    Gather all static files into a single location:

    ```bash
    python manage.py collectstatic
    ```

7. **Start the Server:**

    Run the local server:

    ```bash
    python manage.py runserver
    ```

8. **Access via Browser:**

    After starting the server, navigate to the following URL in your browser:

    ```
    http://127.0.0.1:8000
    ```

## Functionality

The project includes the following main features:

- **Home Page**: Displays tags, categories, editor's picks, trending posts, popular posts, and recently posted articles.
- **Comments**: Users can leave comments on posts or reply to existing comments.
- **Search**: Allows users to search through post titles.
- **Post Details**: Individual pages for each post with detailed information.
- **Contact**: A contact form for users to send messages.
- **Authors**: Information about site authors and their posts.
