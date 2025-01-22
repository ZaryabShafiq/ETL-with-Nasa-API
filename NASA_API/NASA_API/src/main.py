import datetime
from utils import setup_logger, handle_error
from extract import fetch_neo_data
from transform import calculate_risk

LOG_FILE = "logs/app.log"

def main():
    # Set up logger
    logger = setup_logger(LOG_FILE)

    # Define the date range
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=7)
    end_date = today

    logger.info(f"Starting ETL pipeline from {start_date} to {end_date}")

    # Extract
    neo_data = fetch_neo_data(start_date, end_date, logger)
    if not neo_data:
        handle_error(logger, "Failed to fetch NEO data. Exiting.")
        return

    # Transform
    hazardous_asteroids = calculate_risk(neo_data)
    if hazardous_asteroids:
        logger.info(f"Identified {len(hazardous_asteroids)} hazardous asteroids.")
        for asteroid in hazardous_asteroids[:5]:
            logger.info(f"Asteroid: {asteroid['name']} | Risk Score: {asteroid['risk_score']:.2f}")
    else:
        logger.info("No hazardous asteroids identified.")

if __name__ == "__main__":
    main()
