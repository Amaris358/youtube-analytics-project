import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key = "AIzaSyCN7BT8XlSAdIBsCM4FqxqwgfX87CGaH-g"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.channel_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.channel_info["items"][0]["id"]
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.subscriber_count = int(self.channel_info['items'][0]['statistics']['subscriberCount'])
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return build("youtube", "v3", developerKey=cls.api_key)

    def info_dict(self) -> dict:
        """Возвращает словарь с информацией о канале."""
        return {
            "id канала": self.__channel_id,
            "Название канала": self.title,
            "Описание канала": self.description,
            "Ссылка на канал": self.url,
            "Количество подписчиков": self.subscriber_count,
            "Количество видео": self.video_count,
            "Общее количество просмотров": self.view_count,
        }

    def to_json(self, file_name: str) -> None:
        """Сохранить данные в файл."""
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(self.info_dict(), f, indent=2, ensure_ascii=False)


