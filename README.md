# SauceDemo Automation with Playwright (Python)

This project contains automated UI tests for the [SauceDemo](https://www.saucedemo.com) website using **Playwright** with **Python** and **pytest**.

---

## 📂 Project Structure
saucedeomo-automation-playwright/
├── pages/ # Page Object Model classes
│ └── auth/
│ ├── login/
│ │ └── login_page.py
│ └── logout/
│ └── logout_page.py
├── tests/ # Test cases organized by feature
│ └── auth/
│ └── logout/
│ └── test_logout.py
├── conftest.py # pytest fixtures (e.g. login fixture)
├── pytest.ini # pytest configuration
├── requirements.txt # Python dependencies
└── README.md
---

## ⚙️ Setup

###. **Clone repository**

```bash
git clone <your-repo-url>
cd saucedeomo-automation-playwright
```

### Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
Install dependencies

pip install -r requirements.txt
Install Playwright browsers

playwright install

### 🚀 Running Tests
Run all tests with:
pytest

Test results and HTML report will be generated as report.html.

### 🛠️ How to Add Tests
Add new Page Object files inside pages/ following the existing structure.
Add new test files inside tests/ with filenames starting with test_.
Use fixtures defined in conftest.py for setup like login.

### 📄 Reporting
HTML test report is automatically generated after running tests.

Reports can be opened in any browser (report.html).

### 🔖 Notes
Use pytest -k <keyword> to run specific tests.

###📞 Contact
For questions or help, contact: [Lamsihar Sirait / lamsiharsrt24@gmail.com]

