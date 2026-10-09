# SeleniumProject

A Python UI test automation project for
[SauceDemo](https://www.saucedemo.com/) using Selenium WebDriver,
pytest, the Page Object Model (POM), Allure reporting, and Faker.

## Features

-   Logs in with the SauceDemo standard test account.
-   Tests navigation to the About page.
-   Automates purchasing three sample products:
    -   Sauce Labs Backpack
    -   Sauce Labs Bike Light
    -   Sauce Labs Bolt T-Shirt
-   Uses page objects to separate page locators and actions from test
    scenarios.
-   Uses explicit waits for interactive elements.
-   Generates Allure steps and writes execution logs.
-   Takes a screenshot at the end of a successful checkout flow.

## Project structure

``` text
SeleniumProject/
├── base/
│   └── base_class.py
├── pages/
│   ├── login_page.py
│   ├── main_page.py
│   ├── cart_page.py
│   ├── client_information_page.py
│   ├── payment_page.py
│   └── finish_page.py
├── screen/
├── tests/
│   ├── test_about_link.py
│   └── test_buy_product.py
├── utilities/
│   └── logger.py
├── conftest.py
└── requirements.txt
```

## Requirements

-   Python 3.10 or newer is recommended.
-   Google Chrome installed.
-   A compatible ChromeDriver. Recent Selenium versions can manage the
    driver automatically when the environment permits it.
-   Dependencies listed in `requirements.txt`.

## Setup

1.  Clone or extract the repository.

2.  Open a terminal in the project directory.

3.  Create and activate a virtual environment:

    ``` bash
    python -m venv .venv
    ```

    Windows:

    ``` powershell
    .venv\Scripts\Activate.ps1
    ```

    macOS/Linux:

    ``` bash
    source .venv/bin/activate
    ```

4.  Install dependencies:

    ``` bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Run the tests

Run the full test suite:

``` bash
pytest
```

Run a specific test module:

``` bash
pytest tests/test_about_link.py
pytest tests/test_buy_product.py
```

The browser is configured in `conftest.py` to run in headless mode. The
fixture closes the browser after each test.

## Allure reports

The tests use `allure-pytest` to add step information. To save Allure
result files:

``` bash
pytest --alluredir=allure-results
```

If the Allure command-line tool is installed, generate and open a report
with:

``` bash
allure serve allure-results
```

## Configuration notes

-   Test credentials are defined in `pages/login_page.py` for the public
    SauceDemo test site.
-   Customer details are generated with Faker in
    `pages/client_information_page.py`.
-   `base/base_class.py` currently saves screenshots to a hard-coded
    Windows path. Update this path to a project-relative location or
    create the destination directory before running the checkout tests
    on another machine.
-   `utilities/logger.py` also uses a hard-coded Windows log path.
    Update it to a valid path for your environment and ensure the log
    directory exists.
-   The logger opens files with `encoding='utf=8'`; this appears to be a
    typo and should normally be `encoding='utf-8'`.
-   The `screen/` and `logs/` directories should exist if your local
    configuration writes files there.
-   The tests perform checkout flows on the SauceDemo demo site; they do
    not process real payments.

## Troubleshooting

-   **Chrome does not start:** Check that Chrome is installed and that
    Selenium can obtain a compatible driver.
-   **Elements time out:** Check the network connection and whether the
    SauceDemo site is available.
-   **Log or screenshot errors:** Replace hard-coded paths with paths
    that exist on your computer.
-   **Allure report is empty:** Run pytest with
    `--alluredir=allure-results` and confirm that tests completed.

## License

No license file was included with the project. Add a license if you
intend to distribute or reuse the code publicly.
