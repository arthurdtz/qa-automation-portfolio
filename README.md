# QA Automation Portfolio

[![tests](https://github.com/arthurdtz/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/arthurdtz/qa-automation-portfolio/actions/workflows/tests.yml)

API and UI test automation suite built with **Python**, **pytest**, and **Selenium** — a hands-on portfolio project demonstrating test design, automation, and CI practices for QA Automation / SDET roles.

---

## 🎯 About

This project simulates a real-world QA automation workflow: testing a live, authenticated REST API and a web UI, with proper project structure, environment handling, and version control practices used in professional QA teams.

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Test Framework:** pytest
- **HTTP Client:** Requests
- **Environment Management:** python-dotenv
- **UI Automation:** Selenium (headless Chrome on CI)
- **Reporting:** pytest-html
- **CI:** GitHub Actions

## 📁 Project Structure

```
qa-automation-portfolio/
├── .github/workflows/
│   └── tests.yml
├── api_tests/
│   ├── conftest.py
│   └── test_users.py
├── ui_tests/
│   ├── pages/
│   │   └── login_page.py
│   ├── conftest.py
│   └── test_login.py
├── requirements.txt
└── .env
```

## ✅ What's Tested

**API — `/users` endpoint (reqres.in)**
- GET existing user → `200 OK` with correct payload
- GET non-existent user → `404 Not Found`
- POST create user → `201 Created` with submitted data returned
- PUT update user → `200 OK`
- DELETE user → `204 No Content`

**UI — Login page (the-internet.herokuapp.com)**
- Successful login → validates success message
- Invalid username → validates error message
- Invalid password → validates error message

Tests validate both **happy paths** and **error handling**, using a real authenticated API (`x-api-key`) rather than an open, no-auth mock — closer to how APIs behave in production.

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/arthurdtz/qa-automation-portfolio.git
cd qa-automation-portfolio

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Add your own API key
# Create a .env file in the project root:
# REQRES_API_KEY=your_key_here
# Get a free key at https://reqres.in/signup
```

## ▶️ Running the Tests

```bash
# API tests
pytest api_tests/ -v

# UI tests (opens Chrome; set HEADLESS=1 to run without a window)
pytest ui_tests/ -v

# Any suite with an HTML report
pytest api_tests/ -v --html=reports/api-report.html --self-contained-html
```

## ⚙️ Continuous Integration

Every push to `main` and every pull request runs both suites on GitHub Actions ([`tests.yml`](.github/workflows/tests.yml)):

- **API tests** use the `REQRES_API_KEY` repository secret
- **UI tests** run in headless Chrome
- Each job publishes its **HTML report** as a downloadable artifact on the run page

## 🗺️ Roadmap

- [x] API test suite (CRUD + error handling)
- [x] UI test suite with Selenium (Page Object Model)
- [x] GitHub Actions CI pipeline
- [x] HTML test reports

## 👤 Author

**Arthur Meneses**
Software Engineering Student | Aspiring QA Automation Engineer
[LinkedIn](https://www.linkedin.com/in/arthurdtz) · [GitHub](https://github.com/arthurdtz)
