# Playwright SauceDemo Automation Framework

## Overview

This project is a UI automation framework built with Python, Playwright, and pytest using the SauceDemo practice website.

The framework demonstrates automated testing of common e-commerce workflows using the Page Object Model (POM) design pattern, reusable pytest fixtures, parameterized tests, failure debugging tools, HTML reporting, and GitHub Actions CI/CD integration.

The framework currently contains 12 automated test cases covering login, product, cart, and checkout workflows.

---

## Features

* Automated login testing

  * Valid login scenarios
  * Invalid credential validation
  * Empty username/password validation
  * Locked-out user validation

* Product page testing

  * Verify product inventory loads correctly
  * Product sorting validation
  * Add products to cart

* Cart testing

  * Verify products are added correctly
  * Validate cart contents

* Checkout testing

  * Complete end-to-end checkout workflow
  * Verify successful order confirmation

* Page Object Model (POM) architecture

* Reusable pytest fixtures

* Parameterized test cases

* Failure screenshots

* Playwright trace collection

* HTML test reporting

* Git version control

* GitHub Actions CI/CD pipeline

---

## Technologies

* Python
* Playwright
* pytest
* pytest-html
* Git
* GitHub
* GitHub Actions

---

## Project Structure

Playwright/

├── pages/

│   ├── login_page.py

│   ├── products_page.py

│   ├── cart_page.py

│   ├── checkout_page.py

│   └── checkout_overview_page.py

├── tests/

│   ├── test_login.py

│   ├── test_products.py

│   ├── test_cart.py

│   └── test_checkout.py

├── conftest.py

├── requirements.txt

├── .gitignore

└── .github/

```
└── workflows/

    └── test.yml
```

---

## Test Scenarios

### Login

* Valid user login
* Invalid username/password combinations
* Empty username validation
* Empty password validation
* Locked-out user validation

### Products

* Verify product inventory loads
* Sort products alphabetically
* Add Sauce Labs Backpack to cart

### Cart

* Verify added products appear in cart

### Checkout

* Complete end-to-end checkout flow
* Verify successful order confirmation

---

## Running the Project

### Create Virtual Environment

python -m venv .venv

### Activate Virtual Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

python -m pip install -r requirements.txt

### Install Playwright Browsers

playwright install

### Run Tests

pytest -v

### Generate HTML Test Report

pytest -v --html=report.html

The HTML report provides:

* Test execution summary
* Passed/failed test cases
* Test duration
* Environment information

---

## Failure Debugging

When a test fails, the framework automatically generates debugging artifacts.

### Screenshots

Screenshots are saved in:

screenshots/

They capture the browser state at the moment of failure.

### Playwright Traces

Trace files are saved in:

traces/

They provide detailed information about test execution:

* Step-by-step test execution
* Browser interactions
* DOM snapshots
* Network activity
* Screenshots during execution

Open a trace using:

playwright show-trace traces/<trace_file>.zip

---

## CI/CD

This project uses GitHub Actions to automatically execute the Playwright test suite when changes are pushed to the main branch.

The CI pipeline:

* Installs Python dependencies
* Installs Playwright browsers
* Executes pytest test cases
* Generates automated test reports
* Provides test execution feedback

---

## Future Improvements

* Integrate HTML reports into GitHub Actions artifacts
* Attach screenshots and traces directly to CI results
* Expand product test coverage
* Add more checkout validation scenarios
* Improve test data management
* Add API testing coverage
