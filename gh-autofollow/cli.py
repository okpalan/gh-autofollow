import argparse
import os
from gh_autofollow.core import GitHubAutoFollow

# Function to read GitHub token from an environment variable or file
def get_github_token():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise Exception("GitHub token not found. Please set it using 'autogithubfollow config <token>'.")
    return token

def main():
    parser = argparse.ArgumentParser(
        description="GitHub Auto Follow CLI tool"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands help')

    # Follow command
    follow_parser = subparsers.add_parser('follow', help='Follow a GitHub user')
    follow_parser.add_argument('username', type=str, help='Username of the GitHub user to follow')

    # Unfollow command
    unfollow_parser = subparsers.add_parser('unfollow', help='Unfollow a GitHub user')
    unfollow_parser.add_argument('username', type=str, help='Username of the GitHub user to unfollow')

    # List followers command
    list_followers_parser = subparsers.add_parser('list-followers', help='List your current GitHub followers')

    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Monitor your GitHub followers and auto-follow/unfollow')
    monitor_parser.add_argument('--interval', type=int, default=60, help='Interval in seconds between follower checks (default: 60)')

    # Config command (to set GitHub token)
    config_parser = subparsers.add_parser('config', help='Set or update your GitHub API token')
    config_parser.add_argument('token', type=str, help='Your GitHub personal access token')

    args = parser.parse_args()

    if args.command == 'config':
        # Save the token in an environment variable (or a config file)
        os.environ['GITHUB_TOKEN'] = args.token
        print("GitHub token has been set.")
        return

    token = get_github_token()  # Get the token for other operations
    github_follow = GitHubAutoFollow(token)

    if args.command == 'follow':
        github_follow.follow_user(args.username)
        print(f"Followed user {args.username}.")

    elif args.command == 'unfollow':
        github_follow.unfollow_user(args.username)
        print(f"Unfollowed user {args.username}.")

    elif args.command == 'list-followers':
        followers = github_follow.get_current_followers()
        print("Current followers:")
        for follower in followers:
            print(f"- {follower}")

    elif args.command == 'monitor':
        print(f"Starting to monitor followers every {args.interval} seconds...")
        github_follow.monitor_followers(interval=args.interval)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
