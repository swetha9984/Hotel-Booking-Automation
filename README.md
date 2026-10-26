# Hotel Booking Automation Testing

## About the Project
A Selenium-based automation testing project developed using Python and pytest to test hotel booking website functionalities.

## Features
- Automated check-in and check-out date selection.
- Guest and room selection testing.
- Hotel search functionality validation.
- Automated test execution and XML report generation.

## Technologies Used
- Python
- Selenium WebDriver
- pytest
- Google Chrome
- HTML and CSS

## Installation
Install the required dependencies:

```bash
pip install selenium pytest
```

## Execution
Run the test cases using:

```bash
python -m pytest -v -s
```

Generate an XML test report using:

```bash
python -m pytest -v --junitxml=test-results.xml
```

## Project Objective
To automate hotel booking form testing, reduce repetitive manual testing, and verify the expected behaviour of important website features.

## Future Enhancements
- Cross-browser testing
- Screenshot capture on test failures
- GitHub Actions continuous integration
- Advanced test reporting

## License
This project is licensed under the MIT License.
