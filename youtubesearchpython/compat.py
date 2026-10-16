import json
from typing import Union

from youtubesearchpython.core.componenthandler import ComponentHandler
from youtubesearchpython.core.search import SearchCore as RequestHandler
from youtubesearchpython.sync import PlaylistsSearch, VideosSearch


def _view_count(item: dict) -> int:
    value = item.get("viewCount") or {}
    text = value.get("text") if isinstance(value, dict) else value
    digits = "".join(character for character in str(text or "") if character.isdigit())
    return int(digits) if digits else 0


def _thumbnail_urls(item: dict) -> list:
    return [thumbnail["url"] for thumbnail in item.get("thumbnails") or [] if thumbnail.get("url")]


class _CompatibilitySearch:
    search_class = None

    def __init__(self, keyword, offset=1, mode="json", max_results=20, language="en", region="US"):
        self.mode = mode
        self.resultComponents = []
        search = self.search_class(keyword, limit=max_results, language=language, region=region)
        for _ in range(max(1, int(offset)) - 1):
            if not search.next():
                break
        self.resultComponents = [self._convert(item, index) for index, item in enumerate(search.result().get("result") or [])]

    def result(self) -> Union[str, dict, list, None]:
        if not self.resultComponents:
            return None
        data = {"search_result": self.resultComponents}
        if self.mode == "dict":
            return data
        if self.mode == "json":
            return json.dumps(data, indent=4)
        if self.mode == "list":
            return [list(component.values()) for component in self.resultComponents]
        return None


class SearchVideos(_CompatibilitySearch):
    search_class = VideosSearch

    @staticmethod
    def _convert(item: dict, index: int) -> dict:
        channel = item.get("channel") or {}
        return {
            "index": index,
            "id": item.get("id"),
            "link": item.get("link"),
            "title": item.get("title"),
            "channel": channel.get("name") if isinstance(channel, dict) else channel,
            "duration": item.get("duration"),
            "views": _view_count(item),
            "thumbnails": _thumbnail_urls(item),
            "channeId": channel.get("id") if isinstance(channel, dict) else None,
            "publishTime": item.get("publishedTime"),
        }


class SearchPlaylists(_CompatibilitySearch):
    search_class = PlaylistsSearch

    @staticmethod
    def _convert(item: dict, index: int) -> dict:
        channel = item.get("channel") or {}
        return {
            "index": index,
            "id": item.get("id"),
            "link": item.get("link"),
            "title": item.get("title"),
            "thumbnails": _thumbnail_urls(item),
            "count": item.get("videoCount"),
            "channel": channel.get("name") if isinstance(channel, dict) else channel or None,
        }


searchYoutube = SearchVideos

__all__ = ["ComponentHandler", "RequestHandler", "SearchVideos", "SearchPlaylists", "searchYoutube"]
