import unittest
from unittest.mock import patch
from gh_autofollow.core import GitHubAutoFollow

class TestGitHubAutoFollow(unittest.TestCase):
    def setUp(self):
        # Initialize GitHubAutoFollow with a mock token
        self.auto_follow = GitHubAutoFollow(token='mock_token')

    @patch('gh_autofollow.core.requests.get')
    def test_get_current_followers(self, mock_get):
        # Mock the API response to return a dummy list of followers
        mock_response = {
            "status_code": 200,
            "json.return_value": [
                {"login": "user1"},
                {"login": "user2"},
                {"login": "user3"}
            ]
        }
        
        # Set the mock return value for the get request
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"login": "user1"},
            {"login": "user2"},
            {"login": "user3"}
        ]

        # Call the method under test
        followers = self.auto_follow.get_current_followers()

        # Assertions
        self.assertIsInstance(followers, set)
        self.assertEqual(followers, {"user1", "user2", "user3"})  # Expected set of followers

    @patch('gh_autofollow.core.requests.put')
    def test_follow_user(self, mock_put):
        # Mock successful follow (204 status code)
        mock_put.return_value.status_code = 204

        # Call the follow_user method
        self.auto_follow.follow_user('user_to_follow')

        # Ensure the put request was made with the correct URL
        mock_put.assert_called_once_with(
            'https://api.github.com/user/following/user_to_follow',
            headers={'Authorization': 'token mock_token'}
        )

    @patch('gh_autofollow.core.requests.delete')
    def test_unfollow_user(self, mock_delete):
        # Mock successful unfollow (204 status code)
        mock_delete.return_value.status_code = 204

        # Call the unfollow_user method
        self.auto_follow.unfollow_user('user_to_unfollow')

        # Ensure the delete request was made with the correct URL
        mock_delete.assert_called_once_with(
            'https://api.github.com/user/following/user_to_unfollow',
            headers={'Authorization': 'token mock_token'}
        )


if __name__ == '__main__':
    unittest.main()
