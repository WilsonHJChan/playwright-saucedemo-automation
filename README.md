# Playwright SauceDemo Automation Framework

## Overview

This project is a UI automation framework built with Python, Playwright, and pytest using the SauceDemo practice website.

The project demonstrates the use of the Page Object Model (POM), reusable pytest fixtures, and end-to-end test automation for common e-commerce workflows.

---

## Features

- Automated login testing
- Product selection and cart validation
- End-to-end checkout automation
- Page Object Model architecture
- Reusable pytest fixture setup
- Git version control

---

## Technologies

- Python
- Playwright
- pytest
- Git
- GitHub

---

## Project Structure

```
pages/
    login_page.py
    login_page.py
    products_page.py
    cart_page.py
    checkout_page.py
    checkout_overview_page.py

tests/
    test_login.py
    test_products.py
    test_cart.py

conftest.py
```

---

## Test Scenarios

### Login

- Valid user login

### Products

- Add Sauce Labs Backpack to cart

### Checkout

- Complete an end-to-end checkout flow
- Verify successful order confirmation

---

## Running the Project

```bash
python -m pytest -v
```

---

## Future Improvements

- Negative login scenarios
- Checkout validation tests
- Product sorting tests
- Parameterized test data
- GitHub Actions CI/CD
- HTML test reports