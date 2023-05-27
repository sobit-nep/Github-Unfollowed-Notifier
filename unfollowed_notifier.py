import requests

username = "your_username"

# Get followers
followers_url = f"https://api.github.com/users/{username}/followers"
response = requests.get(followers_url)
followers = response.json()

# Get following
following_url = f"https://api.github.com/users/{username}/following"
response = requests.get(following_url)
following = response.json()

# Create a set of follower usernames
follower_usernames = set()
for follower in followers:
    follower_usernames.add(follower["login"])

# Find users you are following but not following you back
not_following_back = []
for user in following:
    if user["login"] not in follower_usernames:
        not_following_back.append(user["login"])

print("Users you are following but not following you back:")
for username in not_following_back:
    print(username)
    # Unfollow the user
    unfollow_url = f"https://api.github.com/user/following/{username}"
    response = requests.delete(unfollow_url, auth=("your_username", "your_token"))
    if response.status_code == 204:
        print(f"Unfollowed {username}.")
    else:
        print(f"Failed to unfollow {username}.")
