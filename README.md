<div align="center">
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/logo.png" alt="VolleySeats Logo" width="400" height="240">

  <h1>VolleySeats</h1>
  
  <h3>  Reserve → Watch → Enjoy 🍿 <br>
  A user-friendly system for volleyball fans to easily book and secure their seats. Watch your favorite team with just one tap. 
  
 </br>[Marianito F. Frane](https://github.com/itsianfrane) <br> 
  IT 2104
  <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

## 📚 Table of Contents  
1. [🔎 Project Overview](#-project-overview)  
2. [💻 Features](#-features)  
3. [🧠 Python Concepts Applied](#-python-concepts-applied)  
4. [👪 Integration of SDG 11: Sustainable Cities and Communities](#-integration-of-sdg-11-sustainable-cities-and-communities)  
5. [⚙️ System Requirements](#%EF%B8%8F-system-requirements)  
6. [🛠️ Installation and Setup](#%EF%B8%8F-installation-and-setup)  
7. [❓ How to Run the Program](#-how-to-run-the-program)  
8. [🗺️ Usage Instructions](#%EF%B8%8F-usage-instructions)    
9. [🔜 Future Improvements](#-future-improvements)  
10. [❤️ Acknowledgement](#%EF%B8%8F-acknowledgement)


## 🔎 Project Overview
> VolleySeats is a Python-based reservation system designed for booking seats at volleyball matches. Users can interact with the system to view match schedules, check available seats, make seat reservations, and confirm bookings. This system was developed with the goal of providing a seamless and efficient way for volleyball fans to secure their seats for upcoming matches, helping to simplify the ticketing process and improve the user experience. The application is particularly aimed at users who wish to attend volleyball games, either for leisure or as part of a larger sports event, offering them a convenient platform to manage their seat reservations. This program simulates a real-life seat reservation experience while demonstrating core programming concepts in Python.

## 💻 Features
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/features.png" alt="Progam Features" width="1000" height="400"> 
</div>

- **View Upcoming Matches**: Displays a comprehensive list of volleyball matches with relevant details.
- **Check Available Seats**: Users can see the seats available for any selected match.
- **Make Reservations**: Users can reserve seats by providing specific match and seat IDs.
- **User-Friendly Interface**: Clear prompts and structured menu options for seamless navigation.

## 🧠 Python Concepts Applied
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/oop.png" alt="OOP Principles" width="1000" height="400"> 
</div>

- The VolleySeats Reservation System demonstrates the application of several core Object-Oriented Programming (OOP) principles. Below is a breakdown of how these concepts were applied throughout the project:
## Classes and Objects
  - In Python, classes are blueprints for creating objects. An object is an instance of a class, and it can store both data (attributes) and methods (functions). The project uses multiple classes to represent key entities in the reservation system, such as users, seats, matches, and the reservation system itself.
  - Person Class: Represents a person with attributes like `first_name`, `last_name`, and `contact_number`. This class serves as a base class for the `User` class.
  - User Class: Inherits from the `Person` class. It extends the functionality of the `Person` class by adding a `reserved_seats` list to store all the seats reserved by the user.
  - Match Class: Represents a volleyball match with details such as `match_id`, `teams`, `date`, and `location`. This class contains a method `display_match_details` that encapsulates how match information is displayed to the user.
  - Seat Class: Represents individual seats in the stadium. Each seat has a unique `seat_id`, is associated with a specific `match_id`, and has a price and availability status. The reserve method allows users to reserve the seat.
## Encapsulation
  - Encapsulation refers to bundling data (attributes) and methods that operate on the data into a single unit (class). It also helps in restricting direct access to some of the object's components, which is a mechanism for data protection.
  - In this project, the Match class hides its internal representation of match details by defining a method `display_match_details`. The actual attributes of the match, such as `match_id`, `teams`, `date`, and `location`, are not directly accessed by external code. Instead, the method `display_match_details` provides a controlled way to display this information.
    
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/encapsulation.png" alt="encapsulation" width="1000" height="300"> 

</div>

## Polymorphism
  - Polymorphism allows objects of different classes to be treated as objects of a common superclass, particularly through method overriding. It enables the same method or function to behave differently based on the object it is acting upon.
  - In this project, polymorphism is demonstrated by the `__str__` method in the `Seat` class. This method is overridden to provide a custom string representation of seat objects, which is different from the default string representation. The output varies depending on whether the seat is reserved or available.
    
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/polymorphism.png" alt="polymorphism" width="700" height="300"> 

</div>

## Inheritance
  - Inheritance is a fundamental OOP concept that allows one class to inherit the attributes and methods of another class. This helps in reusing code and creating a hierarchy of classes.
  - In this project, the `User` class inherits from the `Person` class. The `User` class inherits basic properties like `first_name`, `last_name`, and `contact_number` from `Person`, while also adding additional functionality for managing seat reservations `(reserved_seats list)`.

<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/inheritance.png" alt="inheritance" width="700" height="300"> 

</div>

### Abstraction
  - Abstraction is the process of hiding the implementation details and exposing only the essential features of an object. This allows users of the object to interact with it without needing to understand its inner workings.
  - In this project, the `ReservationSystem` class abstracts away the complex logic of managing seats and reservations. For example, users interact with high-level methods like `reserve_seat` and `export_to_json`, without needing to understand how the underlying seat reservation logic or data export mechanism works.
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/abstraction-1.png" alt="abstraction-1" width="700" height="300"> 
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/abstraction-2.png" alt="abstraction-2" width="700" height="300"> 
</div>

##  👪 Integration of SDG 11: Sustainable Cities and Communities
<div>
  <img src="https://github.com/itsianfrane/VolleySeats/blob/main/images/sdg.png" alt="VolleySeats Logo" width="1000" height="200"> 

</div>

- The VolleySeats Reservation System aligns with **Sustainable Development Goal 11 (SDG 11): Sustainable Cities and Communities** by:
- **Supporting Inclusive Community Engagement**: The project simulates how digital tools can promote accessibility to public events, ensuring more inclusive and safe participation.
- **Encouraging Efficient Event Management**: By digitizing the reservation process, the system helps envision a more organized and efficient way to handle public gatherings, contributing to reduced physical queues and better crowd management.
- **Promoting Sustainable Practices**: Digital reservation systems contribute to environmental sustainability by reducing paper usage and enabling better resource allocation.

## ⚙️ System Requirements
- **Python Version**: Python 3 or higher
- **Libraries**: `json` (part of Python's standard library)

## 🛠️ Installation and Setup
1. **Download Python**: Ensure that Python 3 is installed on your system. Download it from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/itsianfrane/VolleySeats.git
   cd VolleySeats
3. **Verify Installation**: Run the following command to check that Python is installed and available:
   - `python --version`
## ❓ How to Run the Program
  - Navigate to the directory where `main.py` is located.
  - Run the script using: `python main.py`

## 🗺️ Usage Instructions
- **Viewing Matches**
  - Choose `option 1` from the main menu to see all available volleyball matches.
  - Each match displays:
  - `Match ID`: Unique identifier.
`Teams`: Competing teams.
`Date`: Scheduled match date.
`Location`: Venue of the match.
- **Viewing Reserved Seats**
  - Select `option 2` to see all reserved seats and matches associated with your account.
  - If no seats have been reserved yet, the system will notify you.
- **Reserving a Seat**
  - Choose `option 3` from the main menu.
  - Enter the `Match ID` for which you want to reserve a seat.
  - The system will show available seats for that match.
  - Enter the `Seat ID` to confirm your reservation.
- **Confirming a Reservation**
  - After reserving seats, select `option 4` to confirm and export your reservation data to a JSON file.
  - This step creates a file called `data.json` that contains all match and seat information related to the reservations.
- **Quitting the Program**
  - Choose option 5 to exit the program.
  - Exporting Data
  - The system includes functionality to export reservation data in JSON format:
File Name: `data.json`
Content: `Match` and `seat details`, including `reservation status` and `user information`.

## 🔜 Future Improvements
- **User Authentication**: Adding a login system for user accounts.
- **Dynamic Pricing**: Implementing variable seat pricing based on location and demand.
- **Real-time Updates**: Integrating APIs for live match updates and availability.

## ❤️ Acknowledgement 
> First and foremost, I would like to express my deepest gratitude to **Almighty God** for His unending guidance, wisdom, and strength throughout this project.

> To my **family** and **friends**, thank you for your unwavering support, love, and encouragement that pushed me to strive for excellence. 

> To my **crushiecakes**, thank you for being my daily source of joy and inspiration.

> A special thank you goes to my pretty professor, **Ms. Fatima Marie P. Agdon**, for her invaluable guidance, insightful feedback, and continuous encouragement. Your mentorship has been a significant part of my growth, and I am truly grateful for your dedication and support.

> To **all** who have been part of this journey, my heartfelt thanks.
