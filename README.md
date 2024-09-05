# TeleTranquil Prototype Demo: Screen Break Advisor

The TeleTranquil Prototype Demo is a screen break advisor application designed to encourage users to take regular breaks while working on their computer. This simple yet effective tool helps monitor break frequency and provides feedback based on the user's working hours and breaks taken. The application uses Python's Tkinter library to create a user-friendly interface and tracks the user's screen time, promoting better mental and physical health.

## Overview

Prolonged screen time can lead to fatigue, eye strain, and reduced productivity. This application serves as a reminder for users to take regular breaks, thereby enhancing overall well-being. TeleTranquil allows users to start and end breaks, keeps track of the number of breaks taken, and provides personalized feedback based on the user's working hours and break patterns.

## Features

- **Text Editor:** A simple text area for users to note down tasks or important information during work sessions.
- **Break Management:** Allows users to start and end breaks at their convenience.
- **Break Tracking:** Keeps a count of the number of breaks taken.
- **Feedback System:** Provides feedback based on the number of breaks and hours worked.
- **Content Persistence:** Saves the text entered by the user to a file, so the content is available upon reopening the application.

## Installation

### Prerequisites

- Python 3.x
- Tkinter (comes pre-installed with Python)

### Running the Application

1. Clone the repository or download the source code.
2. Ensure that Python is installed on your system.
3. Run the following command in your terminal to start the application:

   ```bash
   python break_app.py
   ```

## How to Use

1. **Start the Application:** Run the script to launch the TeleTranquil Prototype Demo.
2. **Using the Textbox:** You can use the textbox provided to jot down notes or work-related tasks.
3. **Take a Break:** Click the "Take a Break" button to start a break when you feel the need.
4. **End Break:** Click the "Break Over" button to end your break. The application will display the duration of your break.
5. **Check Feedback:** After every three breaks, the application will prompt you to enter the number of hours worked. Based on your input, it will provide feedback on your break-taking habits.
6. **Save Your Work:** The content of the textbox is automatically saved in a file named `textbox_content.txt` upon receiving feedback, so you won't lose your work between sessions.

## Key Components

- **Break Counting:** Tracks the total number of breaks taken.
- **Timer:** Measures the duration of each break.
- **Feedback Mechanism:** Evaluates the user's break habits based on their input for hours worked and the number of breaks taken. Offers suggestions to improve screen time management.
  
## Feedback Logic

The application provides feedback to ensure that users maintain a healthy work-rest balance:

- If the user works more than 6 hours and takes more than 10 breaks, they receive positive reinforcement.
- If the user works more than 6 hours but takes fewer than 10 breaks, the app encourages them to take more breaks.
- If the user works fewer than 6 hours and takes many breaks, they are reassured about their habits.
- If the user works fewer than 6 hours and takes fewer than 3 breaks, they are advised to increase their break frequency.

## Saving Data

- The application saves the contents of the textbox into a file named `textbox_content.txt` when feedback is given, preserving the user's notes for future sessions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Moulya AS, my partner in this project.
- Inspired by best practices in ergonomics and mental health management.

---
