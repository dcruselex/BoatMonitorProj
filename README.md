
Boatmonitoring (boatmon.py)

This project in Phase I is being done to satisfy requirements in a Python class as a capstone project.   In Phase I the project will be focused on meeting the class requirements while demonstrating understanding of specific python areas and providing a program that can be run in other environments without specialty hardware.    In Phase II for my personal goals it will utilize specific Raspberry Pi hardware, sensors, enclosure, etc..     The objective of Phase II will be to monitor several environmental and equipment statuses in my houseboat and report exceptions via alerts and WiFi to remote locations.   I eventually will monitor shore power status, voltage for both AC and DC voltages, water status in multiple compartments, humidity, temperature in multiple locations and will continue to add other sensors to monitor additional environmental and equipment status/metrics and alert on exceptions.

Phase I:

1.	Requirement for this README file that explains:

1.1	A brief description of what the project is about.   Note:  See 1st Paragraph above.
1.2	Which 3+ features I have included from the requirements list to meet the requirements.    Note:  See Section 2 below - 2.3 through 2.6
1.3	Any special instruction required for the reviewer and testers to run the project.

2.	The 3+ features I have included from the requirements list to meet the requirements:

2.1 Project has been uploaded to my GitHub repository 5+ separate commits via Git.

2.2 Project includes this README File that explains the following: 
2.2.1 One paragraph or longer description of what m project is. (See above)  
2.2.2 This section 2 lists the 3+ features I have included from the Python Project Requirements list to meet the requirements. (See 2.3 - 2.6)
2.2.3 Section 3 includes any special instructions required for the reviewer to run my project.

2.3. Feature:  Implemented a “master loop” console application where the user can repeatedly enter command/perform actions, including to exit the program.

2.4. Feature:  Created a class, then created at least one object of that class and populated it with data.   The value of at least one object must be used somewhere in your code.

2.5. Feature:  Created and called at least 3 functions or methods, at least one of which must return a value that is used somewhere else in our code.   To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code.  

2.6. Feature: Build a conversion tool that converts user input to another type and displays it.   Note:  English to Metric conversion tool on temperature.

3.  The following are the specific and special instructions required for the reviewed and testers to run the program.
3.1 The user will need to run the program using Python3.
    Before running program, you will need to "pip install termcolor"
3.2 The user will need to run the program using Python3.
    Note:  > python3 boatmon.py
3.3 The user will have the following choices:
(Q) = Quit:  This will quit the program and return you to terminal
(S) = Scan: This will run the program
(R) = Reboot:  This will reboot and rerun the program
(M) = Mode:  This will change mode, default mode is English, changing mode will put it in metric mode and change the temperature to Celsius.  Changing mode again will put it back in English mode. 
Note:  Since I had to simulate the input
