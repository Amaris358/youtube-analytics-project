import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.youtube = build("youtube", "v3", developerKey='AIzaSyCN7BT8XlSAdIBsCM4FqxqwgfX87CGaH-g')
        self.video_full_info = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
        self.title = self.video_full_info['items'][0]['snippet']['title']
        self.url = "https://youtu.be/" + self.video_id
        self.view_count = self.video_full_info['items'][0]['statistics']['viewCount']
        self.like_count = self.video_full_info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id


