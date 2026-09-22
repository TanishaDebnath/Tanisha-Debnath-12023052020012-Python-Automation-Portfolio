# 🎯 Selenium Automation: Handling Dynamic Web Elements with CSS Wildcard Selectors

A hands-on guide and automation test suite demonstrating how to write resilient, maintainable CSS selectors in Selenium WebDriver using wildcard matching operators (`^=`, `$=Control`, `*=`) on dynamic or varying attribute values.

---

## 📺 Demonstration Video

> **Link:** [CSS Selector Challenge Video Walkthrough (Google Drive)](https://drive.google.com/file/d/1cbPsDE44vQHj-iy98aT9cQGk8u5Wlycc/view?usp=sharing&utm_source=gemini)

---

## 📌 Problem Overview

In modern web applications (built with frameworks like React, Angular, or Vue), attributes such as `id`, `name`, `class`, or `for` are frequently generated dynamically with random suffixes, session IDs, or auto-incrementing numbers (e.g., `radio_109283`, `btn_submit_x7f2`).

Hardcoding the exact, full attribute value results in brittle automation scripts that fail across runs. Instead, robust automation identifies the **stable, invariant stems** of these values and targets them using **CSS Wildcard Attribute Selectors**.

---

## 🔍 CSS Wildcard Matching Reference

| Operator | Type | CSS Syntax | Description |
| --- | --- | --- | --- |
| `^=` | **Starts With** | `[for^='radio']` | Matches elements whose attribute begins with the specified string prefix. |
| `$=` | **Ends With** | `[for$='1']` | Matches elements whose attribute terminates with the specified string suffix. |
| `*=` | **Contains** | `[for*='adi']` | Matches elements whose attribute contains the specified substring anywhere. |

---

## 🧪 Browser Console Verification (DevTools)

Before embedding locators into production scripts, validate matching behavior directly within the Chrome/Edge Developer Tools Console (`F12` or `Ctrl + Shift + I`):

```javascript
// 1. Starts-with: selects all labels starting with 'radio'
document.querySelectorAll("[for^='radio']");

// 2. Ends-with: selects the specific element ending in '1'
document.querySelector("[for$='1']");

// 3. Contains: selects any label containing 'adi' anywhere in its attribute
document.querySelectorAll("[for*='adi']");

```

---

## ⚙️ Setup & Prerequisites

### 1. Requirements

* **Python**: 3.8 or higher
* **Google Chrome**: Latest stable version
* **Selenium**: 4.x or higher

### 2. Installation

```bash
pip install selenium

```

---

## 💻 Python Test Implementation

Save the script as `css_wildcard_automation.py` and run it:

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def run_wildcard_challenge():
    # Initialize Chrome WebDriver session
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Target sandbox practice application
        target_url = "https://rahulshettyacademy.com/AutomationPractice/"
        print(f"Navigating to {target_url}...")
        driver.get(target_url)

        # -------------------------------------------------------------
        # 1. STARTS-WITH OPERATOR (^=)
        # Matches attributes beginning with 'radio' (e.g., radio1, radio2, radio3)
        # -------------------------------------------------------------
        starts_with_selector = "[for^='radio']"
        matching_radios = driver.find_elements(By.CSS_SELECTOR, starts_with_selector)
        print(f"[STARTS-WITH] '{starts_with_selector}' matched: {len(matching_radios)} element(s)")

        # -------------------------------------------------------------
        # 2. ENDS-WITH OPERATOR ($=)
        # Matches attributes terminating with '1' (e.g., radio1)
        # -------------------------------------------------------------
        ends_with_selector = "[for$='1']"
        radio_one_label = driver.find_element(By.CSS_SELECTOR, ends_with_selector)
        radio_one_label.click()
        print(f"[ENDS-WITH] Successfully clicked element via '{ends_with_selector}'")

        # -------------------------------------------------------------
        # 3. CONTAINS OPERATOR (*=)
        # Matches attributes containing substring 'adi' anywhere in the value
        # -------------------------------------------------------------
        contains_selector = "[for*='adi']"
        contains_elements = driver.find_elements(By.CSS_SELECTOR, contains_selector)
        print(f"[CONTAINS] '{contains_selector}' matched: {len(contains_elements)} element(s)")

        # -------------------------------------------------------------
        # 4. REUSABLE FUNCTION FOR DYNAMIC PATTERN GENERATION
        # -------------------------------------------------------------
        def find_by_attribute_pattern(attr: str, op: str, value: str):
            """
            Builds a parameterized CSS wildcard selector and returns all matching WebElements.
            :param attr: Attribute name (e.g., 'for', 'id', 'class')
            :param op: Wildcard operator ('^=', '$=', '*=')
            :param value: Substring to match against
            """
            built_selector = f"[{attr}{op}'{value}']"
            return driver.find_elements(By.CSS_SELECTOR, built_selector)

        # Demonstration of reusable function
        generated_matches = find_by_attribute_pattern("for", "^=", "radio")
        print(f"[REUSABLE HELPER] Custom selector retrieved {len(generated_matches)} element(s)")

        time.sleep(2)

    finally:
        # Terminate driver process and clean up browser session
        driver.quit()
        print("Driver session closed cleanly.")


if __name__ == "__main__":
    run_wildcard_challenge()

```

---

## 🛡️ Best Practices for Dynamic Selectors

1. **Avoid Brittle Full Selectors:** Never depend on session-generated prefixes/suffixes (e.g., avoid `id="button-98234-submit"`). Target the stable stem (`button[id*='submit']`).
2. **Qualify with HTML Tag Names:** Prevent unexpected matches across global DOM trees by combining tag names with attribute filters (e.g., `input[name^='user_']` rather than `[name^='user_']`).
3. **Prioritize Semantic Fallbacks:** When attributes are completely randomized without predictable substrings, traverse using parent structural containers or standard descendant combinators (`div.container > input`).
