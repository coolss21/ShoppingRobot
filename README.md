<div align="center">

# 🛒 ShoppingRobot — RPA-Powered Price Comparison Engine

**Automated web scraping and price comparison across Amazon & Flipkart using UiPath + Flask**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000.svg?logo=flask)](https://flask.palletsprojects.com/)
[![UiPath](https://img.shields.io/badge/UiPath-RPA-FA4616.svg)](https://www.uipath.com/)
[![Pandas](https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📌 Problem Statement

Manually comparing product prices across multiple e-commerce platforms is time-consuming and error-prone. **ShoppingRobot** automates this process using **Robotic Process Automation (RPA)** to scrape product data from Amazon and Flipkart, aggregate it into a structured format, and display a side-by-side comparison through a clean web interface.

---

## 🧠 System Architecture

```mermaid
graph LR
    A[User Input<br/>Search Query] --> B[UiPath RPA Bot]
    B --> C1[Amazon Scraper]
    B --> C2[Flipkart Scraper]
    C1 --> D[Excel Aggregator<br/>final_project.xlsx]
    C2 --> D
    D --> E[Flask Web Server]
    E --> F[Comparison Dashboard<br/>HTML + Bootstrap]

    style A fill:#1a1a2e,color:#fff
    style B fill:#FA4616,color:#fff
    style F fill:#16213e,color:#fff
```

---

## ✨ Key Features

- 🤖 **RPA Automation** — UiPath bot navigates Amazon & Flipkart like a human user
- 📊 **Price Comparison** — Side-by-side product comparison with direct purchase links
- 📁 **Excel Export** — Structured data stored in multi-sheet Excel workbooks
- 🌐 **Web Dashboard** — Flask-powered responsive comparison interface
- 🔗 **Clickable URLs** — Direct links to product pages for instant purchasing

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **RPA Engine** | UiPath Studio | Browser automation & web scraping |
| **Backend** | Python + Flask | Web server & data processing |
| **Data Processing** | Pandas + openpyxl | Excel read/write & data manipulation |
| **Frontend** | HTML + Bootstrap | Responsive comparison dashboard |
| **Data Store** | Excel (.xlsx) | Multi-sheet product data storage |

---

## 🚀 Quick Start

### Prerequisites

- [UiPath Studio](https://www.uipath.com/studio) installed and configured
- Python 3.8+ with pip
- Google Chrome (for RPA browser automation)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/coolss21/ShoppingRobot.git
cd ShoppingRobot

# 2. Install Python dependencies
pip install flask pandas openpyxl

# 3. Place the ShoppingRobot folder in C:\ drive
#    (Required for UiPath file path references)

# 4. Open ShoppingRobot/Main.xaml in UiPath Studio
#    Run the build to execute the RPA workflow

# 5. After scraping completes, start the Flask dashboard
cd ShoppingRobot
python app.py
# Dashboard available at http://localhost:5000
```

---

## 📂 Project Structure

```
ShoppingRobot/
├── ShoppingRobot/
│   ├── Main.xaml              # UiPath main workflow
│   ├── app.py                 # Flask web server
│   ├── final_project.xlsx     # Scraped product data
│   ├── project.json           # UiPath project config
│   └── templates/
│       └── index.html         # Comparison dashboard template
├── documentation              # Setup instructions
└── README.md                  # This file
```

---

## 🔄 Workflow

```mermaid
sequenceDiagram
    participant User
    participant UiPath
    participant Amazon
    participant Flipkart
    participant Excel
    participant Flask

    User->>UiPath: Enter search query
    UiPath->>Amazon: Navigate & scrape products
    Amazon-->>UiPath: Product data (name, price, URL)
    UiPath->>Flipkart: Navigate & scrape products
    Flipkart-->>UiPath: Product data (name, price, URL)
    UiPath->>Excel: Write to multi-sheet workbook
    User->>Flask: Open dashboard
    Flask->>Excel: Read product data
    Flask-->>User: Render comparison table
```

---

## 🧪 Usage

1. **Run the RPA Bot** — Open `Main.xaml` in UiPath Studio and execute
2. **Enter Search Term** — The bot will prompt for a product to search
3. **Wait for Scraping** — The bot navigates both platforms and extracts data
4. **View Results** — Launch the Flask app and browse the comparison dashboard

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<div align="center">
  <br/>
  <p><i>Smart shopping starts with smart automation.</i></p>
</div>
