# Galactic-Resource-Management
​A Python-based interstellar fleet management simulation demonstrating advanced Object-Oriented Programming (OOP) concepts, secure resource tracking, and automated mission logging.

​🚀 Galactic Resource Management System

​A professional OOP-based fleet management system for interstellar exploration. 




​📌 Project Overview

​The Galactic Resource Management System is a comprehensive Python-based simulation designed to manage a fleet of spacecraft. 

Built to demonstrate advanced Object-Oriented Programming (OOP) mastery, it models real-world programmatic complexities like resource tracking, secure transactions, and mission logging. 

​This project showcases the seamless integration of all four core OOP pillars, alongside advanced Python features like custom decorators, dunder methods, and custom exception handling. 




​🏗️ System Architecture: Classes & Methods

​The codebase is structured around several distinct components to ensure modularity and fail-safe operations.


​1. SpaceAsset (ABC)

​An abstract base class that acts as a strict blueprint for all vehicles in the fleet. 

​calculate_range(self, mileage): An @abstractmethod that forces all child classes to define their own specific range-calculation logic.


​2. ShipWallet

​The core spacecraft class inheriting from SpaceAsset. It manages the primary attributes: fuel_reserves, tank_capacity, cargo_capacity, and crew_members. 

​fuel_filling(self, fuel): Handles the logic for refueling, checking for negative values, overloading limits, and triggering warnings if fuel levels are critically low.

​reserves: Utilizes @property and @reserves.setter decorators to safely encapsulate and manage the private __fuel_reserves data.

​mission_launch(self): Initiates a 10-second countdown sequence before launch.

​mission_timestamp(self): An empty method wrapped by a custom decorator to log system events.


​3. Specialized Fleet Classes (AdityaSolarProbe & DeepSpaceCargo)

​Child classes that inherit from ShipWallet and demonstrate polymorphism. 

​Overridden Methods: Both classes provide their own unique implementation of calculate_range(self, mileage) and string representation (_str_).

​_add_(self, other): A magic (dunder) method that allows two ships to combine their _cargo_capacity simply by using the + operator, returning a newly instantiated ship with the merged stats.

​_len_(self): Returns the number of crew members aboard the specific vessel.


​4. Utilities & Error Handling

​log_mission(func): A custom decorator that utilizes the datetime module to automatically log the exact timestamp a mission starts.

​LowFuelError(Exception): A custom exception class designed to be raised when fuel drops below 500,000L, preventing catastrophic failures during operations.



​✨ Key Features

​Asset Abstraction: Implements a strict SpaceAsset blueprint ensuring all fleet vehicles follow mission-critical standards.

​Secure Resource Management: Uses Encapsulation and Property Decorators to protect fuel reserves from illegal data entry.

​Polymorphic Fleet: Distinct operational logic for the AdityaSolarProbe and DeepSpaceCargo ships.

​Magic Interaction: Custom Dunder methods allowing ships to merge cargo capacities using simple arithmetic operators like addition (+).

​Mission Logging: Real-time activity tracking using custom Decorators to monitor system events.

​Fail-Safe Systems: Robust custom Exception Handling to prevent program crashes during deep-space operations.



​🛠️ Technologies Used

​Language: Python 3.12+

​Core Concepts: Abstraction, Encapsulation, Inheritance, Polymorphism

​Standard Libraries: abc (Abstract Base Classes), datetime (Mission Logging)



​📦 Installation

​Clone the repository and run the simulation locally: 
bash:
# Clone the Repo
git clone: 
https://github.com/Mitul-Beniwal/Galactic-Resource-Management.git

# Navigate and Run
cd Galactic-Resource-Management
python src/main.py



📂 File Structure

​src/: Main application logic.

​tests/: Verification scripts to ensure system reliability.
