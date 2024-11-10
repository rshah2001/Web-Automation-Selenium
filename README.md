# Web Automation Tool GUI with Selenium

This project is a Python-based web automation tool that uses Selenium WebDriver to automate interactions with a demo website. It includes features for logging in, filling out a form, and downloading files, with a configurable GUI for user input.

## Features

- Automates login to a demo site using provided credentials.
- Fills out a sample form with user-provided details.
- Downloads files from the demo site.
- GUI for user-friendly configuration of input data.

## Requirements

- Python 3.6 or later
- Google Chrome (installed and up to date)
- ChromeDriver (matching your version of Chrome)
- Selenium library for Python

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/rshah2001/Web-Automation-Tool-GUI-with-Selenium.git
cd Web-Automation-Tool-GUI-with-Selenium
```

### 2. Install Required Packages

Install Selenium:
```bash
pip install selenium
```

### 3. Download ChromeDriver

1. Download the ChromeDriver that matches your Chrome browser version from the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
2. Place the `chromedriver` file in the `chromedriver-mac-arm64` folder within this project directory.

### 4. Configure Download Path

The script automatically sets the default download path to the current working directory, so any files downloaded will be saved there.

## Usage

### 1. Set Up Environment

Activate your virtual environment if you’re using one:
```bash
# On MacOS/Linux
source venv/bin/activate

# On Windows
.\venv\Scripts\activate
```

### 2. Run the Script

Run the `WebAutomation` script:
```bash
python main.py
```

### 3. Customize the Script

To log in with different credentials or form data, update the `login` and `fill_form` method parameters in the script, or pass them directly if you modify the script.

## Code Overview

- **`__init__`**: Initializes Chrome options, sets download path, and opens ChromeDriver.
- **`login`**: Logs into the demo site with specified username and password.
- **`fill_form`**: Fills a sample form with full name, email, current address, and permanent address.
- **`download`**: Initiates a file download from the website.
- **`close`**: Closes the browser window.

## Example Usage

This example shows how to use `WebAutomation`:

```python
if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('username', 'password')
    webautomation.fill_form('Full Name', 'email@example.com', 'Current Address', 'Permanent Address')
    webautomation.download()
    webautomation.close()
```

## Notes

- Make sure ChromeDriver is compatible with your current Chrome version.
- Ensure all required fields are correctly mapped to the elements on the page.

## Troubleshooting

- **Error: `Message: no such element`** - Ensure the website structure hasn’t changed, as this may cause element locators to fail.
- **Error: `SessionNotCreatedException`** - Update ChromeDriver to match the installed version of Chrome.
