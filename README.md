# Playwright SauceDemo Automation Framework

## Overview

This project is a UI automation framework built with Python, Playwright, and pytest using the SauceDemo practice website.

The framework demonstrates automated testing of common e-commerce workflows using the Page Object Model (POM) design pattern, reusable pytest fixtures, parameterized tests, and GitHub Actions CI/CD integration.

---

## Features

- Automated login testing
  - Valid login scenarios
  - Invalid credential validation
  - Empty username/password validation
  - Locked-out user validation

- Product page testing
  - Verify product inventory loads correctly
  - Product sorting validation
  - Add products to cart

- Cart testing
  - Verify products are added correctly
  - Validate cart contents

- Checkout testing
  - Complete end-to-end checkout workflow
  - Verify successful order confirmation

- Page Object Model (POM) architecture
- Reusable pytest fixtures
- Parameterized test cases
- Git version control
- GitHub Actions CI/CD pipeline

---

## Technologies

- Python
- Playwright
- pytest
- Git
- GitHub
- GitHub Actions

---

## Project Structure

```
Playwright/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_overview_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py
├── requirements.txt
└── .github/
    └── workflows/
        └── test.yml
```

---

## Test Scenarios

### Login

- Valid user login
- Invalid username/password combinations
- Empty username validation
- Empty password validation
- Locked-out user validation

### Products

- Verify product inventory loads
- Sort products alphabetically
- Add Sauce Labs Backpack to cart

### Cart

- Verify added products appear in cart

### Checkout

- Complete end-to-end checkout flow
- Verify successful order confirmation

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browsers

```bash
playwright install
```

### Run tests

```bash
pytest -v
```

---

## CI/CD

This project uses GitHub Actions to automatically execute the Playwright test suite when changes are pushed to the main branch.

The CI pipeline:

- Installs Python dependencies
- Installs Playwright browsers
- Executes pytest test cases
- Reports test results

---

## Future Improvements

- Add automated screenshots on test failure
- Add Playwright trace collection
- Add HTML test reports
- Expand test coverage for additional product scenarios
- Add more checkout validation tests
- Improve test data management