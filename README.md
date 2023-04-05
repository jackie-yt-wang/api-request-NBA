#### Eastern Conference

| Team                |   W |   L | Last10Games   |
|:--------------------|----:|----:|:--------------|
| Milwaukee Bucks     |  57 |  22 | 7W3L          |
| Boston Celtics      |  54 |  24 | 7W3L          |
| Philadelphia 76ers  |  51 |  27 | 5W5L          |
| Cleveland Cavaliers |  50 |  30 | 7W3L          |
| New York Knicks     |  46 |  33 | 7W3L          |
| Brooklyn Nets       |  43 |  36 | 4W6L          |
| Miami Heat          |  42 |  37 | 5W5L          |
| Toronto Raptors     |  40 |  39 | 7W3L          |

#### Western Conference

| Team                   |   W |   L | Last10Games   |
|:-----------------------|----:|----:|:--------------|
| Denver Nuggets         |  52 |  26 | 6W4L          |
| Memphis Grizzlies      |  49 |  29 | 8W2L          |
| Sacramento Kings       |  47 |  31 | 6W4L          |
| Phoenix Suns           |  43 |  35 | 6W4L          |
| LA Clippers            |  41 |  38 | 5W5L          |
| Golden State Warriors  |  41 |  38 | 5W5L          |
| Minnesota Timberwolves |  40 |  40 | 4W6L          |
| Los Angeles Lakers     |  40 |  38 | 7W3L          |

The `nba-standings-python` repo is last updated on *2023-04-04*

---
<img alt="JPG" src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" width="400" height="320" />

## How it works
The script uses an `API key` that is stored in a GitHub secret to authenticate with the `Rapid API`. The API key is passed as an environment variable to the script, which then uses it to make the API request. The script retrieves the standings data as a JSON object, parses it using the json library, and creates a pandas DataFrame containing the standings for each conference.

The script then sorts the standings by wins and losses and selects the top 8 teams from each conference. The standings for each conference are then formatted as markdown tables using the to_markdown() method of the pandas DataFrame. The markdown tables are then appended to the end of the `README.md` file.

## How to use it
To use this script, you need to have a Rapid API account and an `API key` that has access to the standings endpoint. You should store your `API key` as a secret in your GitHub repository, which can be accessed by the script during execution.

To schedule the script to run at a regular interval, you can use a `GitHub Actions` workflow that is triggered by a schedule event. The workflow `YAML file` should specify the interval at which the script should run, as well as the timezone in which the script should be executed. An example workflow YAML file is included in this repository, which you can modify to suit your needs.
