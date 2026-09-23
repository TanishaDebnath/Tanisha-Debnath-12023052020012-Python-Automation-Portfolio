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
│   └── config.ini
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