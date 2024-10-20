# EV Data API
Thank you for visiting, let's get to work building something great!

“The technology you use impresses no one. The experience you create with it is everything.”
— Sean Gerety

## Quick Review

1. **`main.py`**: I began by setting up a FastAPI application in `main.py`. This file is responsible for initializing the app, registering routes, and configuring the startup events to load the data.
  
2. **`routes/routes.py`**: Next, we defined the API endpoint in `routes.py` to handle requests for querying EV data by year. I ensured that the `year` could be passed as a path parameter and added support for a `verbose` query option.
  
3. **`ev_utils/ev_scraper.py`**: I then created a data scraper in `ev_scraper.py` to pull the latest EV data from a public API, storing it in memory to serve requests quickly without re-fetching data.

4. **`ev_utils/ev_evaluator.py`**: This file handles the logic of filtering the EV data by year and calculating metrics like the total number of cars and their average electric range, grouped by make.

5. **`ev_utils/logger.py`**: Finally, I added logging functionality in `logger.py` to track requests, errors, and data scraping activities, ensuring smooth operation and easy debugging.

Afterwards, the future of this API has many areas that can be improved:
- In terms of user functionality, we can showcase a lot more filter functionality such as vehicle price ranges, battery capacity, and specific makes or models.
- Integrating multiple data sources could provide even more accurate insights for users.
- Build a user-facing dashboard with data visualizations to enhance user interaction and insights from the API :D

For the API itself, we could add more safe guards and important workflows as we collect more data.
- Use async calls to fetch data without blocking operations, improving response times and scalability.
- Ensure code quality and prevent bugs by implementing thorough unit and integration tests
- Prevent abuse by limiting the number of API requests from users over a certain period.
- Secure the API by requiring users to authenticate via API keys, controlling access and usage
- Ensure that incoming data is properly validated to prevent invalid entries and improve API reliability
- Secure the API by enforcing HTTPS and adding security headers to prevent common vulnerabilitie

### User Manual

This FastAPI-based web service scrapes and serves electric vehicle (EV) data. Users can query the number of cars and the average electric range by make for a given year. The service also supports a verbose mode that includes detailed car data.

Available years in dataset: ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/ev-data-api.git
    cd ev-data-api
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To start the FastAPI server
```bash
python -m uvicorn main:app --reload
```

Alternatively, you can use **Uvicorn**:
```bash
uvicorn main:app --reload --port 8000
```


The server will be accessible at `http://localhost:8000`.

## Available Routes

### 1. Get EV Data by Year

- **Endpoint**: `/evdata/{year}`
- **Method**: `GET`
- **Path Parameter**:
  - `year`: (Required) The model year to filter EV data. Must be between 1900 and the current year.
- **Query Parameters**:
  - `verbose`: (Optional) Set to `true` to include detailed raw data for each car.

#### Example Requests:

1. **Get summarized EV data for the year 2011**:

    ```bash
    http://localhost:8000/evdata/2011
    ```

2. **Get verbose EV data for the year 2011 (includes raw car data)**:

    ```bash
    http://localhost:8000/evdata/2011?verbose=true
    ```

### Response Format

- **Summarized Response**:

    ```json
    {
      "year": "2018",
      "total_records": 100,
      "data": [
        {
          "make": "TESLA",
          "total_cars": 60,
          "average_electric_range": 300.5
        }
      ]
    }
    ```

- **Verbose Response**:

    ```json
    {
      "year": "2018",
      "total_records": 100,
      "data": [
        {
          "make": "TESLA",
          "total_cars": 60,
          "average_electric_range": 300.5,
          "raw_data": [
            {
              "vin_1_10": "5YJ3E1EB5J",
              "county": "Kitsap",
              "city": "Bremerton",
              "state": "WA",
              "zip_code": "98310",
              "model_year": "2018",
              "make": "TESLA",
              "model": "MODEL 3",
              "electric_range": "215"
            },
            {
              "vin_1_10": "5YJ3E1EA8J",
              "county": "King",
              "city": "Seattle",
              "state": "WA",
              "zip_code": "98101",
              "model_year": "2018",
              "make": "TESLA",
              "model": "MODEL S",
              "electric_range": "370"
            }
          ]
        }
      ]
    }
    ```

## Data Source
https://data.wa.gov/resource/f6w7-q2d2.json

## License

This project is licensed under the MIT License.

---
