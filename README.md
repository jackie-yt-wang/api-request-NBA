#### Eastern Conference

| Team                |   W |   L | Last10Games   |
|:--------------------|----:|----:|:--------------|
| Boston Celtics      |   0 |   0 | 8W2L          |
| Philadelphia 76ers  |   0 |   0 | 5W5L          |
| New York Knicks     |   0 |   0 | 5W5L          |
| Brooklyn Nets       |   0 |   0 | 6W4L          |
| Toronto Raptors     |   0 |   0 | 6W4L          |
| Milwaukee Bucks     |   0 |   0 | 6W4L          |
| Cleveland Cavaliers |   0 |   0 | 7W3L          |
| Chicago Bulls       |   0 |   0 | 6W4L          |

#### Western Conference

| Team                   |   W |   L | Last10Games   |
|:-----------------------|----:|----:|:--------------|
| Denver Nuggets         |   0 |   0 | 5W5L          |
| Minnesota Timberwolves |   0 |   0 | 7W3L          |
| Oklahoma City Thunder  |   0 |   0 | 4W6L          |
| Utah Jazz              |   0 |   0 | 2W8L          |
| Portland Trail Blazers |   0 |   0 | 1W9L          |
| Sacramento Kings       |   0 |   0 | 5W5L          |
| Phoenix Suns           |   0 |   0 | 7W3L          |
| LA Clippers            |   0 |   0 | 6W4L          |

The `nba-standings-python` repo is last updated on *2023-08-25*

---
<img alt="JPG" src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" width="400" height="320" />

## How it works
The script uses an `API key` that is stored in a GitHub secret to authenticate with the `Rapid API`. The API key is passed as an environment variable to the script, which then uses it to make the API request. The script retrieves the standings data as a JSON object, parses it using the json library, and creates a pandas DataFrame containing the standings for each conference.

The script then sorts the standings by wins and losses and selects the top 8 teams from each conference. The standings for each conference are then formatted as markdown tables using the to_markdown() method of the pandas DataFrame. The markdown tables are then appended to the end of the `README.md` file.

## How to use it
To use this script, you need to have a Rapid API account and an `API key` that has access to the standings endpoint. You should store your `API key` as a secret in your GitHub repository, which can be accessed by the script during execution.

To schedule the script to run at a regular interval, you can use a `GitHub Actions` workflow that is triggered by a schedule event. The workflow `YAML file` should specify the interval at which the script should run, as well as the timezone in which the script should be executed. An example workflow YAML file is included in this repository, which you can modify to suit your needs.
