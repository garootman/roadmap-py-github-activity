# roadmap-py-github-activity

Project for [roadmpa.sh](https://roadmap.sh/projects/github-user-activity)
[github API reference](https://docs.github.com/en/rest/activity/events)


In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a simple CLI application.

The application should run from the command line, accept the GitHub username as an argument, fetch the user’s recent activity using the GitHub API, and display it in the terminal. The user should be able to:


## usage
```bash
python main.py garootman
# prints activity
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...
```

If you are looking to build a more advanced version of this project, you can consider adding features like filtering the activity by event type, displaying the activity in a more structured format, or caching the fetched data to improve performance. You can also explore other endpoints of the GitHub API to fetch additional information about the user or their repositories.