# Selenium Python Automation Framework

## Capstone Assignment 2

### Selenium Python Framework Development
**Unittest + PyTest + Page Object Model**

---

## 1. Project Overview

This project implements a Selenium Python automation framework for testing an e-commerce web application.

The framework automates:

- Valid Login
- Invalid Login
- Product Search
- Data-driven Product Search

The project uses the Page Object Model (POM) design pattern and supports both PyTest and Python Unittest.

Additional framework features include:

- Configuration Management
- CSV Test Data
- PyTest Fixtures
- Utility Classes
- Screenshot on Failure
- HTML Reporting

---

## 2. Application Under Test

**Application:** TutorialsNinja Demo

**URL:** https://tutorialsninja.com/demo/

The application is an e-commerce demonstration website containing products, account management, shopping cart and search functionality.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium | Web browser automation |
| PyTest | Test framework |
| Unittest | Python unit testing framework |
| CSV | Test data management |
| ConfigParser | Configuration management |
| pytest-html | HTML reporting |
| Chrome | Web browser |
| VS Code | Development environment |

---

## 4. Project Structure

```text
Wipro_Selenium_Capstone/
│
├── config/
│   └── config.example.ini
│
├── data/
│   └── test_data.csv
│
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_unittest_login.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot_util.py
│
├── screenshots/
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
````

---

## 5. Project Demonstration & Documentation

### Demonstration Video

The project demonstration video covers the framework structure, Selenium automation, Login and Product Search test cases, PyTest execution, Unittest execution, screenshots, and HTML reporting.

**Demonstration Link:**

[https://drive.google.com/file/d/1ZLhgYpztNgWftxizWz7cw2sLJJtqEcGh/view?usp=sharing](https://drive.google.com/file/d/1ZLhgYpztNgWftxizWz7cw2sLJJtqEcGh/view?usp=sharing)

### Project Report

The detailed project report contains the project objective, problem statement, framework design, implementation details, test cases, results, screenshots, and conclusion.

**Report Link:**

[https://docs.google.com/document/d/1P9l25bn6hhuC3FEEnXIgkodjsyxnkx-c/edit?usp=sharing&ouid=108701656685506271417&rtpof=true&sd=true](https://docs.google.com/document/d/1P9l25bn6hhuC3FEEnXIgkodjsyxnkx-c/edit?usp=sharing&ouid=108701656685506271417&rtpof=true&sd=true)

### GitHub Repository

The complete source code and project files are available in the GitHub repository.

**GitHub Link:**

[https://github.com/TanishaDebnath/Tanisha-Debnath-12023052020012-Python-Automation-Portfolio/tree/main/Folder-2-Capstone-Project](https://github.com/TanishaDebnath/Tanisha-Debnath-12023052020012-Python-Automation-Portfolio/tree/main/Folder-2-Capstone-Project)

---

## 6. Test Scenarios

| Test Case                | Description                                        |
| ------------------------ | -------------------------------------------------- |
| Valid Login              | Verifies successful login using valid credentials  |
| Invalid Login            | Verifies warning message for invalid credentials   |
| Product Search – MacBook | Verifies search functionality for MacBook          |
| Product Search – iPhone  | Verifies search functionality for iPhone           |
| Product Search – Canon   | Verifies search functionality for Canon            |
| Unittest Login           | Verifies login functionality using Python Unittest |

---

## 7. Framework Features

### Page Object Model

The application pages are separated into individual page classes:

* `HomePage`
* `LoginPage`
* `SearchPage`

This keeps locators and page actions separate from the test cases.

### Configuration Management

`config.example.ini` provides the configuration structure for:

* Application URL
* Browser
* Login credentials

The actual `config.ini` file should contain the user's local credentials and should not be committed to GitHub.

### Data-Driven Testing

Product search data is stored in:

```text
data/test_data.csv
```

The CSV file contains:

```text
product
MacBook
iPhone
Canon
```

PyTest parameterization executes the same product search test for each product.

### PyTest Fixtures

The `conftest.py` file provides a reusable WebDriver fixture.

The fixture:

1. Creates the browser driver.
2. Provides the driver to the test.
3. Closes the browser after test execution.

### Utility Classes

The framework includes reusable utility classes for:

* Configuration reading
* CSV data reading
* WebDriver creation
* Screenshot capture

### Screenshot on Failure

The framework automatically captures a screenshot when a PyTest test fails.

Screenshots are stored in:

```text
screenshots/
```

### HTML Reporting

The project uses `pytest-html` to generate an HTML test report.

Command:

```powershell
pytest -v --html=reports/report.html --self-contained-html
```

The report contains:

* Test cases
* Pass/Fail status
* Execution details
* Environment information
* Failure information

---

## 8. How to Run the Project

### Step 1: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 2: Activate the Virtual Environment

```powershell
venv\Scripts\activate
```

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Configure the Application

Create a local file:

```text
config/config.ini
```

using `config.example.ini` as a template.

Add the required:

* Application URL
* Browser
* Email
* Password

Do not commit `config.ini` containing real credentials to GitHub.

### Step 5: Run All PyTest Tests

```powershell
pytest -v
```

### Step 6: Generate HTML Report

```powershell
pytest -v --html=reports/report.html --self-contained-html
```

### Step 7: Run the Unittest Test Separately

```powershell
python -m unittest tests.test_unittest_login -v
```

---

## 9. Expected Test Result

The framework contains 6 test executions:

* 2 Login tests
* 3 Data-driven Product Search tests
* 1 Unittest Login test

```text
Total: 6 Tests
```

A successful PyTest execution should display:

```text
6 passed
```

The HTML report is generated at:

```text
reports/report.html
```

---

## 10. Conclusion

The Selenium Python automation framework successfully demonstrates automated testing of the Login and Product Search functionalities of the TutorialsNinja e-commerce application.

The framework combines PyTest, Unittest, Page Object Model, configuration management, CSV-based test data, reusable utility classes, screenshot capture, and HTML reporting.

The modular structure separates test cases, page interactions, configuration, test data, and utilities, making the framework easier to maintain and extend. Data-driven testing also allows multiple product search scenarios to be executed without duplicating test code.

The project demonstrates the practical implementation of a structured Selenium automation framework for web application testing.

---

## Author

**TANISHA DEBNATH**

**Enrollment No.:** 12023052020012

**Department:** CSE AI

**Institute:** Institute of Engineering and Management

**Course:** Python Automation

**Assignment:** Capstone Assignment 2

```
```
