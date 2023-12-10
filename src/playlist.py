from googleapiclient.discovery import build
import isodate
from datetime import datetime, time, timedelta


class PlayList:
    youtube = build("youtube", "v3", developerKey='AIzaSyCN7BT8XlSAdIBsCM4FqxqwgfX87CGaH-g')

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__playlist_full_info = PlayList.youtube.playlists().list(id=self.__playlist_id, part='snippet').execute()
        self.title = self.__playlist_full_info['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.__playlist_id
        self.__videos = PlayList.youtube.playlistItems().list(playlistId=self.__playlist_id, part='contentDetails', maxResults=50,).execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__videos['items']]

    @property
    def total_duration(self):
        video_response = PlayList.youtube.videos().list(part='contentDetails,statistics', id=','.join(self.__video_ids)).execute()
        playlist_duration = timedelta(seconds=0)
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            playlist_duration += duration
        return playlist_duration

    def show_best_video(self):
        best_video = 0
        likes_max = 0
        for i in range(0, len(self.__video_ids)):
            like_count = int(self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.__video_ids[i]).execute()['items'][0]['statistics']['likeCount'])
            if like_count > likes_max:
                likes_max = like_count
                best_video = i
        return 'https://youtu.be/' + self.__video_ids[best_video]









