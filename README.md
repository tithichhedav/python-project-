 Project Description: IndiStay
IndiStay is a high-end, full-stack web portal designed to redefine the domestic travel experience in India. Moving away from cluttered traditional booking sites, IndiStay focuses on a minimalist, immersive UI and a seamless user journey.

Core Concept
The application serves as a bridge between travelers and luxury accommodations. It categorizes premium stays across five iconic Indian regions: Goa, Jaipur, Mumbai, Kerala, and Delhi. Each listing is designed to provide a "vibe-first" approach, using high-quality dynamic imagery and clean typography.

Key Features
Immersive Glassmorphism UI: A modern homepage featuring a transparent navigation bar that reacts to scrolling, and a "blurred glass" search interface.

Curated Database: Unlike basic projects, this includes a robust catalog of 35 unique hotels, each with specific pricing and descriptions.

Secure User Ecosystem: A full authentication flow (Signup/Login) ensuring that only registered users can book stays.

Personalized Experience: A custom dashboard that greets users by name and displays their booking history as a visual itinerary.

Dynamic Image Logic: Uses a "seeded" image system so every hotel in the database displays a unique, professional architectural photo without needing local storage.

 Steps to Run the Project
To get the project live on your local machine, follow these steps exactly:

1. Set Up Your Environment
Open your terminal (in VS Code, press Ctrl + ` ) and install the necessary Python libraries:

Bash
pip install flask flask-sqlalchemy
2. Prepare the Data
If you have been testing and have an existing database.db file in your folder:

Right-click and Delete database.db.

This is necessary because the code is programmed to "Seed" (auto-fill) the 35 hotels only if the database is empty.

3. Execute the Application
Run the main Python file:

Bash
python app.py
You should see a message in the terminal saying: * Running on http://127.0.0.1:5000.

4. View the Website
Open your web browser (Chrome or Edge recommended).

Type localhost:5000 in the address bar and hit Enter.

5. Test the Flow
Search: Select a city (like Jaipur) on the homepage.

Signup: Create a new account for Tithi, Dishita, or Adhishree.

Book: Click on a hotel, select dates, and hit "Book Now."

Verify: Check the My Bookings dashboard to see your confirmed stay and the SweetAlert popup.

Tithi: Data Architect & Content Specialist (Database & Models).

Dishita: Frontend Lead & UI Designer (Glassmorphism & Navbar Logic).

Adhishree: Full-Stack Engineer & Logic Lead (Auth, Sessions & Dashboard).

Video Link:
https://drive.google.com/drive/folders/1nMKUW7VZy5stXavRkM7Hubd_IQLUKfz_
