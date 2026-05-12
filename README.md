# Weather API Integration App

## Overview
This is a Python-based Weather Information Application built as part of the InternSpark internship (Task 2). The application fetches real-time weather data from the **OpenWeatherMap API** and displays it through a user-friendly Graphical User Interface (GUI) built with `Tkinter`.

## Features
- **Real-time Data**: Fetches current temperature, humidity, wind speed, and more.
- **Error Handling**: Handles invalid city names, API key issues, and connection timeouts gracefully.
- **Modern UI**: A clean, responsive interface with a "Clear" functionality.
- **Keyboard Shortcuts**: Supports `Enter` to search and `Esc` to clear.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x
- `requests` library

You can install the dependency using pip:
```bash
pip install requests
```

## How to Run
1. Obtain an API Key from [OpenWeatherMap](https://openweathermap.org/api).
2. Open `Task2.py` and replace the `API_KEY` variable with your unique key.
3. Run the script:
   ```bash
   python Task2.py
   ```
4. Enter a city name and click **"Get Weather"**.

## Project Structure
- `Task2.py`: Main Python script containing the logic and GUI.
- `Task_2.pdf`: Project documentation/requirements.
- `README.md`: This file.
- `screenshots/`: Folder containing app screenshots.

## Screenshots
Please refer to the `screenshots/` folder for visual demonstrations:
- `code_screenshot.png`: The implementation code.
- `input_screenshot.png`: The user input interface.
- `output_screenshot.png`: The weather data results.
