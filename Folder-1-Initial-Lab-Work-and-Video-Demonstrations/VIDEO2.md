# 🎯 CSS Selector Challenge: Handling Dynamic & Varying Attributes

Automating modern web applications with Selenium WebDriver often runs into brittle tests when element attributes (such as `id`, `name`, or `for`) contain dynamic or auto-generated values. This module demonstrates how to write robust, resilient CSS selectors using **wildcard attribute matching operators**.

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
Before writing automated tests, test the expressions directly inside the browser's Developer Tools Console (`Ctrl + Shift + I` or `F12`):

```javascript
// 1. Matches all labels whose 'for' attribute starts with 'radio'
document.querySelectorAll("[for^='radio']");

// 2. Matches single element whose 'for' attribute ends with '1'
document.querySelector("[for$='1']");

// 3. Matches all elements containing the substring 'adi'
document.querySelectorAll("[for*='adi']");

# 🎯 CSS Selector Challenge: Handling Dynamic & Varying Attributes

Automating modern web applications with Selenium WebDriver often runs into brittle tests when element attributes (such as `id`, `name`, or `for`) contain dynamic or auto-generated values. This module demonstrates how to write robust, resilient CSS selectors using **wildcard attribute matching operators**.

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
Before writing automated tests, test the expressions directly inside the browser's Developer Tools Console (`Ctrl + Shift + I` or `F12`):

```javascript
// 1. Matches all labels whose 'for' attribute starts with 'radio'
document.querySelectorAll("[for^='radio']");

// 2. Matches single element whose 'for' attribute ends with '1'
document.querySelector("[for$='1']");

// 3. Matches all elements containing the substring 'adi'
document.querySelectorAll("[for*='adi']");
