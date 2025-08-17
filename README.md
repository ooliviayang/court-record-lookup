# Wisconsin Court Case Search Automation

This Python script automates searching the [Wisconsin Circuit Court Access (CCAP)](https://wcca.wicourts.gov) website using Selenium. It fills out the search form with a first name, last name, optional middle name, and optional date of birth.

> ⚠️ Note: This script is intended for personal, lawful use and respects CCAP website's terms of service. Inspired by an episode of Armchair Anonymous, automates case lookup by name for women using dating apps (only customized to the Wisconsin court website) or whatever other use cases!

---

## Features

- Automatically opens Chrome and navigates to the CCAP website
- Clicks the "I Agree" button on the disclaimer
- Fills in:
  - First name
  - Middle name (optional)
  - Last name
  - Date of Birth (optional, format: MM-DD-YYYY)
- Browser stays open for manual inspection after the script finishes

---

## Prerequisites

- Python 3.8 or higher
- [Selenium](https://pypi.org/project/selenium/)
- Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version

Install Selenium via pip:

```bash
pip install selenium
