# Playwright SauceDemo Automation Framework

## Overview

This project is an automated UI testing framework built using Python, Playwright, and pytest.

The framework automates common user workflows on the SauceDemo website using the Page Object Model (POM) design pattern and reusable pytest fixtures.

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

## Current Test Coverage

- User login
- Add backpack to cart
- Complete checkout flow

---

## Running the Tests

```bash
python -m pytest -v
```

---

## Future Improvements

- Invalid login tests
- Checkout validation tests
- Product sorting tests
- Parameterized test cases
- GitHub Actions CI