import requests
import time
import json
import csv


class APIFetcher:
    def __init__(self, logger, retries=3, delay=2):
        self.logger = logger
        self.retries = retries
        self.delay = delay

    def fetch(self, url):
        """Fetch data from an API with retry logic."""
        for attempt in range(1, self.retries + 1):
            try:
                self.logger.info(f"Fetching data (Attempt {attempt} from {url})")
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                self.logger.info("Data fetched successfully")
                return response.json()
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Attempt {attempt} failed: {e}")
                if attempt < self.retries:
                    self.logger.info(f"Retrying in {self.delay} seconds...")
                    time.sleep(self.delay)
        self.logger.critical("All retry attempts failed.")
        return None

    def save_json(self, data, file_path):
        """Save API data to JSON file."""
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        self.logger.info(f"Data saved to {file_path}")

    def save_csv(self, data, file_path):
        """Save API data to CSV file (if it's a list of dictionaries)."""
        if not isinstance(data, list) or not data:
            self.logger.warning("Data is not a list or is empty; skipping CSV save.")
            return

        keys = data[0].keys()
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        self.logger.info(f"Data saved to {file_path}")
