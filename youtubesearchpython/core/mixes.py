from typing import Optional

from youtubesearchpython.core.constants import ResultMode
from youtubesearchpython.core.playlist import PlaylistCore
from youtubesearchpython.core.requests import YouTubeRequestError
from youtubesearchpython.core.utils import get_playlist_id, get_video_id


class MixesCore:
    def __init__(self, videoLink: str, timeout: Optional[int] = None):
        self.videoLink = videoLink
        self.timeout = timeout
        self.resultComponents = []
        self._playlist = PlaylistCore(self._mix_id(videoLink), "getVideos", ResultMode.dict, timeout)

    @staticmethod
    def _mix_id(value: str) -> str:
        playlist_id = get_playlist_id(value)
        if playlist_id.startswith("RD"):
            return playlist_id
        video_id = get_video_id(value)
        if len(video_id) != 11 or any(character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for character in video_id):
            raise YouTubeRequestError("A valid video ID, video URL, or RD mix ID is required")
        return "RD" + video_id

    @staticmethod
    def _normalize(video: dict) -> dict:
        channel = video.get("channel") or {}
        normalized_channel = {
            "name": channel.get("name"),
            "id": channel.get("id"),
        }
        if channel.get("link"):
            normalized_channel["link"] = channel["link"]
        return {
            "type": "video",
            "id": video.get("id"),
            "title": video.get("title"),
            "publishedTime": None,
            "duration": video.get("duration"),
            "viewCount": {"text": None, "short": None},
            "thumbnails": video.get("thumbnails") or [],
            "channel": normalized_channel,
            "isLive": bool(video.get("isLive")),
            "accessibility": video.get("accessibility") or {"title": None, "duration": None},
            "link": video.get("link"),
        }

    def _process(self) -> None:
        videos = (self._playlist.result or {}).get("videos") or []
        self.resultComponents = [self._normalize(video) for video in videos if video.get("id")]

    def sync_create(self) -> None:
        self._playlist.sync_create()
        self._process()

    async def async_create(self) -> None:
        await self._playlist.async_create()
        self._process()
