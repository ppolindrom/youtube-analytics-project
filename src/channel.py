import json
import os
from googleapiclient.discovery import build




class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']["default"]['url']
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.viewCount = channel['items'][0]['statistics']['viewCount']


    @property
    def channel_id(self) -> str:
        return self.__channel_id
    #
    # @channel_id.setter
    # def channel_id(self, channel_id):
    #     self.__channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info)
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        object_get = build('youtube', 'v3', developerKey=api_key)
        return object_get

    def to_json(self, file_name):
        # with open(file_name, 'w') as f:
        #     json.dump(self.__dict__, f)
        dict = {}
        dict['id'] = self.channel_id
        dict['title'] = self.title
        dict['description'] = self.description
        dict['url'] = self.url
        dict['subscriberCount'] = self.subscriber_count
        dict['video_count'] = self.video_count

        with open(file_name, 'w') as f:
            json.dump(dict, f, indent=2)