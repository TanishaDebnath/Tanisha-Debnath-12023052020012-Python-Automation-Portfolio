```markdown
# 🎯 CSS Selector Challenge: Handling Dynamic & Varying Attributes

Automating modern web applications with Selenium WebDriver often runs into brittle tests when element attributes (such as `id`, `name`, or `for`) contain dynamic or auto-generated values[cite: 1.3]. This module demonstrates how to write robust, resilient CSS selectors using **wildcard attribute matching operators**[cite: 1.3].

---

## 📺 Demonstration Video
[![Watch CSS Selector Challenge Demo](https://img.shields.io/badge/Google%20Drive-Watch%20Demonstration-blue?style=for-the-badge&logo=google-drive&logoColor=white)](https://drive.google.com/file/d/1cbPsDE44vQHj-iy98aT9cQGk8u5Wlycc/view?usp=sharing)

> **Link:** [CSS Selector Demonstration (Google Drive)](https://drive.google.com/file/d/1cbPsDE44vQHj-iy98aT9cQGk8u5Wlycc/view?usp=sharing)

---

## 📌 Problem Statement
In real-world web applications, IDs and classes frequently shift (e.g., `radio_109283`, `btn_submit_x7f2`)[cite: 1.3]. Hardcoding the entire attribute value creates fragile tests that break whenever dynamic portions update[cite: 1.3].

Instead of targeting full attribute values, we target **stable substrings** using CSS wildcard operators[cite: 1.3].

---

## 🔍 CSS Wildcard Operators Cheat Sheet

| Operator | Meaning | CSS Syntax Example | Description |
| :---: | :--- | :--- | :--- |
| `^=` | **Starts with** | `[for^='radio']` | Matches elements whose attribute begins with the specified prefix[cite: 1.3]. |
| `$=` | **Ends with** | `[for$='1']` | Matches elements whose attribute terminates with the specified suffix[cite: 1.3]. |
| `*=` | **Contains** | `[for*='adi']` | Matches elements whose attribute contains the substring anywhere within the value[cite: 1.3]. |

---

## 🧪 Console Validation (DevTools)
Before writing automated tests, test the expressions directly inside the browser's Developer Tools Console (`Ctrl + Shift + I` or `F12`)[cite: 1.2, 1.3]:

```javascript
// 1. Matches all labels whose 'for' attribute starts with 'radio'
document.querySelectorAll("[for^='radio']");

// 2. Matches single element whose 'for' attribute ends with '1'
document.querySelector("[for$='1']");

// 3. Matches all elements containing the substring 'adi'
document.querySelectorAll("[for*='adi']");

```

---

## 💻 Python & Selenium Implementation

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to Rahul Shetty Academy Practice Page
    driver.get("[https://rahulshettyacademy.com/AutomationPractice/](https://rahulshettyacademy.com/AutomationPractice/)")

    # -------------------------------------------------------------
    # 1. STARTS WITH (^=)
    # Matches: radio1, radio2, radio3
    # -------------------------------------------------------------
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, "[for^='radio']")
    print(f"Total elements matching starts-with 'radio': {len(radio_buttons)}")

    # -------------------------------------------------------------
    # 2. ENDS WITH ($=)
    # Targets specific item ending with '1' (radio1)
    # -------------------------------------------------------------
    radio_one = driver.find_element(By.CSS_SELECTOR, "[for$='1']")
    radio_one.click()
    print("Successfully clicked radio button ending with '1'")

    # -------------------------------------------------------------
    # 3. CONTAINS (*=)
    # Matches substring anywhere inside the value
    # -------------------------------------------------------------
    containing_adi = driver.find_elements(By.CSS_SELECTOR, "[for*='adi']")
    print(f"Total elements containing substring 'adi': {len(containing_adi)}")

    # -------------------------------------------------------------
    # 4. REUSABLE DYNAMIC SELECTOR GENERATOR
    # -------------------------------------------------------------
    def get_elements_by_wildcard(driver, attribute: str, operator: str, value: str):
        """
        Dynamically constructs a wildcard CSS selector and returns matching elements.
        Operators: '^=' (starts with), '$=' (ends with), '*=' (contains)
        """
        selector = f"[{attribute}{operator}'{value}']"
        return driver.find_elements(By.CSS_SELECTOR, selector)

    # Example using the helper function
    dynamic_radios = get_elements_by_wildcard(driver, "for", "^=", "radio")
    print(f"Dynamically generated selector found: {len(dynamic_radios)} elements")

    time.sleep(2)

finally:
    driver.quit()

```

---

## 💡 Best Practices

* **Keep selectors short & meaningful:** Anchor to stable prefixes or suffixes rather than lengthy DOM paths.


* **Pair with tag names where necessary:** e.g., `input[name*='btn']` or `label[for^='radio']` to avoid matching unintended tags across larger DOMs.


* **Avoid auto-generated hashes:** Look for human-readable semantic stems (e.g., `user-name-`, `submit_`).



```

```
