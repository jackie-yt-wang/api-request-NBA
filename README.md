#### Eastern Conference

| Team                |   W |   L | Last10Games   |
|:--------------------|----:|----:|:--------------|
| Milwaukee Bucks     |  52 |  20 | 7W3L          |
| Boston Celtics      |  50 |  23 | 5W5L          |
| Philadelphia 76ers  |  49 |  23 | 9W1L          |
| Cleveland Cavaliers |  47 |  28 | 7W3L          |
| New York Knicks     |  42 |  33 | 5W5L          |
| Miami Heat          |  40 |  34 | 7W3L          |
| Brooklyn Nets       |  39 |  34 | 5W5L          |
| Atlanta Hawks       |  36 |  37 | 4W6L          |

#### Western Conference

| Team                   |   W |   L | Last10Games   |
|:-----------------------|----:|----:|:--------------|
| Denver Nuggets         |  49 |  24 | 5W5L          |
| Memphis Grizzlies      |  45 |  27 | 7W3L          |
| Sacramento Kings       |  43 |  29 | 6W4L          |
| Phoenix Suns           |  38 |  34 | 5W5L          |
| LA Clippers            |  38 |  35 | 5W5L          |
| Golden State Warriors  |  38 |  36 | 4W6L          |
| Minnesota Timberwolves |  37 |  37 | 5W5L          |
| Oklahoma City Thunder  |  36 |  36 | 8W2L          |

The `nba-standings-python` repo is last updated on *2023-03-23*

---
<img alt="JPG" src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" width="400" height="320" />

## How it works
The script uses an `API key` that is stored in a GitHub secret to authenticate with the `Rapid API`. The API key is passed as an environment variable to the script, which then uses it to make the API request. The script retrieves the standings data as a JSON object, parses it using the json library, and creates a pandas DataFrame containing the standings for each conference.

The script then sorts the standings by wins and losses and selects the top 8 teams from each conference. The standings for each conference are then formatted as markdown tables using the to_markdown() method of the pandas DataFrame. The markdown tables are then appended to the end of the `README.md` file.

## How to use it
To use this script, you need to have a Rapid API account and an `API key` that has access to the standings endpoint. You should store your `API key` as a secret in your GitHub repository, which can be accessed by the script during execution.

To schedule the script to run at a regular interval, you can use a `GitHub Actions` workflow that is triggered by a schedule event. The workflow `YAML file` should specify the interval at which the script should run, as well as the timezone in which the script should be executed. An example workflow YAML file is included in this repository, which you can modify to suit your needs.
