# Github-Unfollowed-Notifier

Github Unfollowed Notifier is a Python script that helps you identify GitHub users who have unfollowed you. It utilizes the GitHub API to retrieve your followers and following lists, and then compares them to find users who are not following you back. Additionally, it provides an option to automatically unfollow those users.

## Features

- Retrieve your GitHub followers and following lists.
- Identify users who are not following you back.
- Automatically unfollow users who are not following you back.

## Requirements

- Python 3.6 or above
- Requests library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/unfollowed-notifier.git

2. Install the required dependencies:

   ```bash
   pip install requests

## Usage
1. Open the unfollowed_notifier.py file.

2. Replace "your_username" and "your_token" with your GitHub username and an access token that has the necessary scope to unfollow users. You can create a personal     access token with the public_repo or repo scope from your GitHub account settings.(Click this link to know how to create your github personal access token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

3. Run the script:

   ```bash
   python unfollowed_notifier.py
The script will retrieve your followers and following lists, compare them, and display a list of users who are not following you back.

4. (Optional) To automatically unfollow the users, uncomment the relevant code in the unfollowed_notifier.py script.


## Contributing
Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.
