import argparse
import json
import time
from typing import Any, Dict, List, Tuple, Union

import requests

parser = argparse.ArgumentParser(description="Get Github activity")
parser.add_argument("username", type=str, help="Github username")
args = parser.parse_args()
username = args.username


def get_user_activity(username: str) -> Tuple[List[Dict[str, Any]], str]:
    try:
        events = requests.get(
            f"https://api.github.com/users/{username}/events", timeout=5
        )
        if events.status_code != 200:
            return [], f"Error: {events.text}"
        limits_left = int(events.headers.get("X-RateLimit-Remaining"))
        refresh_time = int(events.headers.get("X-RateLimit-Reset"))
        till_refresh = int(refresh_time - int(time.time()))
        if limits_left == 0:
            return [], f"API rate limit exceeded, try again in {till_refresh} seconds"
        events = events.json()
        print(
            f"got {len(events)} events, {limits_left} requests left within {till_refresh} seconds"
        )
        return events, ""
    except Exception as e:
        error = str(e)
        return [], error


def format_events(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # returns a multiline string with the formatted events
    # add username, event type, repo name, and created_at
    formatted_events = []
    for event in events:
        formatted_event = {
            "username": event["actor"]["login"],
            "event_type": event["type"],
            "action": (
                event["payload"]["action"] if "action" in event["payload"] else None
            ),  # some events don't have an action
            "repo_name": event["repo"]["name"],
            "created_at": event["created_at"],
        }
        formatted_events.append(formatted_event)

    return formatted_events


def main():
    events, error = get_user_activity(username)
    if error:
        print(f"Error: {error}")
        return
    formatted_events = format_events(events)
    print(json.dumps(formatted_events, indent=2))


if __name__ == "__main__":
    main()
