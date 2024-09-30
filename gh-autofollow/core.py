import time
import requests

class GitHubAutoFollow:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {self.token}"}
        self.previous_followers = set()

    def follow_user(self, username):
        url = f"{self.base_url}/user/following/{username}"
        response = requests.put(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Successfully followed {username}")
        else:
            print(f"Failed to follow {username}: {response.json()}")

    def unfollow_user(self, username):
        url = f"{self.base_url}/user/following/{username}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Successfully unfollowed {username}")
        else:
            print(f"Failed to unfollow {username}: {response.json()}")

    def get_current_followers(self):
        url = f"{self.base_url}/user/followers"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return {user['login'] for user in response.json()}  # Return as set for comparison
        else:
            print("Failed to retrieve followers")
            return set()

    def monitor_followers(self, interval=60):
        print(f"Monitoring followers every {interval} seconds...")

        # Initial fetch
        self.previous_followers = self.get_current_followers()
        print(f"Initial followers: {self.previous_followers}")

        while True:
            try:
                current_followers = self.get_current_followers()

                # Find new followers
                new_followers = current_followers - self.previous_followers
                for user in new_followers:
                    print(f"New follower detected: {user}")
                    self.follow_user(user)

                # Find users who unfollowed
                unfollowed_users = self.previous_followers - current_followers
                for user in unfollowed_users:
                    print(f"User unfollowed: {user}")
                    self.unfollow_user(user)

                # Update previous followers
                self.previous_followers = current_followers

                # Sleep for the specified interval
                time.sleep(interval)

            except Exception as e:
                print(f"Error occurred: {str(e)}")
