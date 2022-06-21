import json
from os import getenv

from utils.console import print_step

    redditobj,
):  # don't set this to be run anyplace that isn't subreddit.py bc of inspect stack
    """params:
    reddit_object: The Reddit Object you received in askreddit.py"""
    with open("./video_creation/data/videos.json", "r") as done_vids_raw:
        done_videos = json.load(done_vids_raw)
    for video in done_videos:
        if video["id"] == str(redditobj):
            if getenv("POST_ID"):
                print_step(
            print_step("Getting new post as the current one has already been done")
            return None
    return redditobj
