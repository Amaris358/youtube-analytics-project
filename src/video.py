from googleapiclient.discovery import build


class Video:
    api_key = 'AIzaSyCN7BT8XlSAdIBsCM4FqxqwgfX87CGaH-g'
    youtube = build("youtube", "v3", developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                        id=self.video_id).execute()
            self.video_full_info = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=self.video_id).execute()
            self.title = self.video_full_info['items'][0]['snippet']['title']
            self.url = "https://youtu.be/" + self.video_id
            self.view_count = self.video_full_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_full_info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id


