#### Eastern Conference

| Team                |   W |   L | Last10Games   |
|:--------------------|----:|----:|:--------------|
| Milwaukee Bucks     |  58 |  22 | 7W3L          |
| Boston Celtics      |  55 |  25 | 7W3L          |
| Philadelphia 76ers  |  52 |  28 | 5W5L          |
| Cleveland Cavaliers |  51 |  30 | 7W3L          |
| New York Knicks     |  47 |  33 | 7W3L          |
| Brooklyn Nets       |  44 |  36 | 5W5L          |
| Miami Heat          |  43 |  37 | 6W4L          |
| Atlanta Hawks       |  41 |  39 | 6W4L          |

#### Western Conference

| Team                  |   W |   L | Last10Games   |
|:----------------------|----:|----:|:--------------|
| Denver Nuggets        |  52 |  27 | 6W4L          |
| Memphis Grizzlies     |  50 |  30 | 7W3L          |
| Sacramento Kings      |  48 |  32 | 5W5L          |
| Phoenix Suns          |  44 |  35 | 7W3L          |
| LA Clippers           |  42 |  38 | 5W5L          |
| Golden State Warriors |  42 |  38 | 6W4L          |
| Los Angeles Lakers    |  41 |  39 | 7W3L          |
| New Orleans Pelicans  |  41 |  39 | 8W2L          |

The `nba-standings-python` repo is last updated on *2023-04-06*

---
<img alt="JPG" src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" width="400" height="320" />

## How it works
The script uses an `API key` that is stored in a GitHub secret to authenticate with the `Rapid API`. The API key is passed as an environment variable to the script, which then uses it to make the API request. The script retrieves the standings data as a JSON object, parses it using the json library, and creates a pandas DataFrame containing the standings for each conference.

The script then sorts the standings by wins and losses and selects the top 8 teams from each conference. The standings for each conference are then formatted as markdown tables using the to_markdown() method of the pandas DataFrame. The markdown tables are then appended to the end of the `README.md` file.

## How to use it
To use this script, you need to have a Rapid API account and an `API key` that has access to the standings endpoint. You should store your `API key` as a secret in your GitHub repository, which can be accessed by the script during execution.

To schedule the script to run at a regular interval, you can use a `GitHub Actions` workflow that is triggered by a schedule event. The workflow `YAML file` should specify the interval at which the script should run, as well as the timezone in which the script should be executed. An example workflow YAML file is included in this repository, which you can modify to suit your needs.
