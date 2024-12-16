# Quiz Application

## Overview

This is a Python-based quiz application that uses various components, such as data retrieval from an API, question management, score tracking, and a graphical user interface (GUI) built with `Tkinter`. The application fetches quiz questions from an external API, presents them to the user, tracks their score, and displays the results once the quiz is completed.

## Features

- **Dynamic Question Retrieval**: Fetches quiz questions from the Open Trivia Database API, allowing for a wide variety of questions and topics.
- **Score Tracking**: Keeps track of the user's score throughout the quiz and displays the final score at the end.
- **Interactive GUI**: Built using `Tkinter`, the application offers an engaging user interface with buttons for answering questions and displaying feedback (correct or incorrect answers).
- **True/False Quiz Format**: Presents questions in a True/False format, making it simple and quick for users to participate.
- **Feedback System**: Provides real-time feedback after each question, changing the background color based on the correctness of the answer (green for correct, red for incorrect).
- **Responsive UI**: The GUI is designed to adjust to different screen sizes, ensuring a pleasant experience across various devices.

## Files and Components

### 1. `question_model.py`

This file contains the `Question` class, which defines the structure for each question, including the question text and the correct answer.

### 2. `data.py`

This file handles the logic for fetching quiz questions from the Open Trivia Database API (`https://opentdb.com/api.php`). The questions are retrieved in a random amount, focusing on Boolean-type questions from the "General Knowledge" category.

### 3. `quiz_brain.py`

The `QuizBrain` class manages the logic of the quiz. It navigates through the questions, checks the user's answers, and tracks the score.

### 4. `ui.py`

The `Screen` class is responsible for creating the GUI using `Tkinter`. It displays questions and handles user interactions (True/False answers). It also manages the display of the score and shows the results at the end of the quiz.

## Running the Application

1. Install the necessary dependencies.
2. Download the required images (`true.png` and `false.png`) for the True/False buttons.
3. Run the `main.py` or equivalent script to start the quiz.

### Requirements

- `Tkinter` (pre-installed with Python)
- `requests` (for making HTTP requests to the quiz API)

To install the necessary dependencies, run:

```bash
pip install requests
