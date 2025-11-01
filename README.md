# 🪙 API Data Fetcher & Logger (CoinGecko Version)

Fetches **live Bitcoin price data** from the **CoinGecko public API**, featuring robust **logging**, **retry logic**, and automatic **data serialization** to both **JSON** and **CSV** formats.

Ideal for developers learning API integration, error handling, and structured data storage in Python.

---

## 🚀 Features

* **Real-Time Data Fetching** – Retrieves the latest Bitcoin market data from CoinGecko.
* **Resilient Retry Logic** – Automatically retries failed API calls with configurable delay.
* **Structured Logging** – Logs each API call, success, and error using Python’s built-in `logging` module.
* **Data Serialization** – Saves fetched data as both `.json` and `.csv` for flexible use.
* **Clean Architecture** – Modular and easy-to-extend codebase.

---

## 📁 Project Structure

```
api_data_fetcher/
│
├── main.py              # Entry point for running the data fetcher
├── fetcher.py           # Core logic for API requests and retry handling
├── logger_config.py     # Logging configuration setup
├── requirements.txt     # Project dependencies
└── data/
    ├── coin_data.json   # JSON file storing fetched data
    └── coin_data.csv    # CSV file storing fetched data
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/api-data-fetcher.git
cd api-data-fetcher
pip install -r requirements.txt
```

---

## 🧩 Requirements

```
requests
```

Install via pip:

```bash
pip install requests
```

---

## ▶️ Usage

Run the main script to fetch and log data:

```bash
python main.py
```

This will:

* Fetch current Bitcoin price data from the CoinGecko API
* Log the process to the console and/or log files
* Save the resulting data in both `data/coin_data.json` and `data/coin_data.csv`

---

## 🧠 Example Output

**Console log:**

```
[INFO] Fetching Bitcoin price data...
[INFO] Data fetched successfully.
[INFO] Data saved to coin_data.json and coin_data.csv
```

**JSON file:**

```json
{
  "bitcoin": {
    "usd": 67241.23
  }
}
```

**CSV file:**

```csv
timestamp,bitcoin_usd
2025-11-01T03:15:12Z,67241.23
```

---

## 🧰 Tech Stack

* **Language:** Python 3
* **Libraries:** `requests`, `logging`, `csv`, `json`
* **API Source:** [CoinGecko API](https://www.coingecko.com/en/api)

---

## 🧑‍💻 Contributing

Contributions are welcome!
Feel free to fork this project, create a feature branch, and submit a pull request.

---

## 🪪 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments

* [CoinGecko](https://www.coingecko.com/en/api) for their free public cryptocurrency data API.
* Python’s logging and requests community for simple and powerful tools.

---

Would you like me to make this **README markdown file (`README.md`)** ready for download with your GitHub username filled in automatically?
