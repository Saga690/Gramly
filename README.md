# GRAMLY

## Overview

Gramly is a dynamic social media app which allows users to create, like, report, and delete posts, as well as view posts from other users.

## Features

- User authentication and profile management
- Edit your name, email, avatar or change password
- Discover suggested people
- Delve on trending topics
- Search functionality to find users and posts
- Add friends
- Create, delete, and like posts
- Option to create private posts visible only to friends
- Ability to add frineds
- Report inappropriate content
- Real-time updates for likes and post count
- Receive notifications for likes, comments, friend requests, and reports
  
## Getting Started

### Prerequisites

Ensure you have the following installed on your local development machine:

- Python 3.8+
- Node.js 12+
- npm or yarn

### Installation

1. Clone the repository.
   
   ```
   https://github.com/Saga690/Gramly
   ```
   
   Navigate to the cloned repository

   ```
   cd Gramly
   ```

2. Setup the backend.

   Setup a virtual environment and navigate to the backend directory

   ```
   python -m venv venv
   ```

   ```
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   ```
   cd backend
   ```

   Install the required Python packages

   ```
   pip install -r requirements.txt
   ```

   Run database migrations

   ```
   python manage.py migrate
   ```

   Start the Django development server

   ```
   python manage.py runserver
   ```

3. Frontend Setup

   Navigate to the frontend directory

   ```
   cd ../frontend
   ```

   Install the required packages

   ```
   npm install
   ```
   or
   ```
   yarn install
   ```

   Start the Vue.js development server

   ```
   npm run dev
   ```
   
   

## Usage

1. Open your browser and navigate to http://localhost:8000 to access the Django backend admin interface.
2. Navigate to http://localhost:5173 to view the Vue.js frontend.
3. Register a new user, create posts, like posts, and explore the functionalities of the app.
