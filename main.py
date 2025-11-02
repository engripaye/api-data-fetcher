from logger_config import setup_logger
from fetcher import APIFetcher
import os


def main():
    logger = setup_logger()
    fetcher = APIFetcher(logger)

    os.makedirs("data", exist_ok=True)
    # Public API - no key required
    api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"

    data = fetcher.fetch(api_url)
    if data:
        fetcher.save_json(data, "data/coin_data.json")
        fetcher.save_csv(data, "data/coin_data.csv")
        logger.info("✅ Project run completed successfully.")
    else:
        logger.error("❌ Failed to fetch data after retries.")


if __name__ == "__main__":
    main()
