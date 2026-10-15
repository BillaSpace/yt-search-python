# YouTube Mixes

## Synchronous

```python
from youtubesearchpython import Mixes

videos = Mixes.get("pnxL4OOzPEc")
```

## Asynchronous

```python
from youtubesearchpython.future import Mixes

videos = await Mixes.get("https://www.youtube.com/watch?v=pnxL4OOzPEc")
```

`Mixes.get()` accepts a video ID, a YouTube video URL, or an existing `RD...` mix ID. It returns a direct list in YouTube's order. Duplicate video IDs are removed stably.

## Result shape

Each item uses the same fields as `Recommendations.get()`:

```json
[
  {
    "type": "video",
    "id": "VIDEO_ID",
    "title": "Video title",
    "publishedTime": null,
    "duration": "3:42",
    "viewCount": {
      "text": null,
      "short": null
    },
    "thumbnails": [],
    "channel": {
      "name": "Channel name",
      "id": "CHANNEL_ID",
      "link": "https://www.youtube.com/channel/CHANNEL_ID"
    },
    "isLive": false,
    "accessibility": {
      "title": "Video title",
      "duration": "3 minutes, 42 seconds"
    },
    "link": "https://www.youtube.com/watch?v=VIDEO_ID"
  }
]
```

Fields unavailable in YouTube's mix panel, such as `publishedTime` and `viewCount`, remain `null` instead of being guessed.
