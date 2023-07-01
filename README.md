#### Eastern Conference

| Team                |   W |   L | Last10Games   |
|:--------------------|----:|----:|:--------------|
| Milwaukee Bucks     |  58 |  23 | 7W3L          |
| Boston Celtics      |  56 |  25 | 7W3L          |
| Philadelphia 76ers  |  53 |  28 | 5W5L          |
| Cleveland Cavaliers |  51 |  30 | 7W3L          |
| New York Knicks     |  47 |  34 | 6W4L          |
| Brooklyn Nets       |  45 |  36 | 6W4L          |
| Miami Heat          |  43 |  38 | 5W5L          |
| Atlanta Hawks       |  41 |  40 | 6W4L          |

#### Western Conference

| Team                  |   W |   L | Last10Games   |
|:----------------------|----:|----:|:--------------|
| Denver Nuggets        |  52 |  29 | 5W5L          |
| Memphis Grizzlies     |  51 |  30 | 7W3L          |
| Sacramento Kings      |  48 |  33 | 5W5L          |
| Phoenix Suns          |  45 |  36 | 7W3L          |
| LA Clippers           |  43 |  38 | 6W4L          |
| Golden State Warriors |  43 |  38 | 7W3L          |
| Los Angeles Lakers    |  42 |  39 | 8W2L          |
| New Orleans Pelicans  |  42 |  39 | 8W2L          |

The `nba-standings-python` repo is last updated on *2023-06-30*

---
<img alt="JPG" src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" width="400" height="320" />

## How it works
The script uses an `API key` that is stored in a GitHub secret to authenticate with the `Rapid API`. The API key is passed as an environment variable to the script, which then uses it to make the API request. The script retrieves the standings data as a JSON object, parses it using the json library, and creates a pandas DataFrame containing the standings for each conference.

The script then sorts the standings by wins and losses and selects the top 8 teams from each conference. The standings for each conference are then formatted as markdown tables using the to_markdown() method of the pandas DataFrame. The markdown tables are then appended to the end of the `README.md` file.

## How to use it
To use this script, you need to have a Rapid API account and an `API key` that has access to the standings endpoint. You should store your `API key` as a secret in your GitHub repository, which can be accessed by the script during execution.

To schedule the script to run at a regular interval, you can use a `GitHub Actions` workflow that is triggered by a schedule event. The workflow `YAML file` should specify the interval at which the script should run, as well as the timezone in which the script should be executed. An example workflow YAML file is included in this repository, which you can modify to suit your needs.
