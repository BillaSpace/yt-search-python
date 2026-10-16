# Async API

`youtubesearchpython.future` is the supported async namespace for yt-search-python 2.2.2. It mirrors the current content APIs without changing the synchronous imports at the package root.

## Search

```python
import asyncio

from youtubesearchpython.future import VideosSearch


async def main():
    search = VideosSearch("Arijit Singh", limit=10)
    first_page = await search.next()
    second_page = await search.next()
    print(first_page, second_page)


asyncio.run(main())
```

The first `await search.next()` performs the initial request. Later calls request continuation pages until YouTube returns no continuation.

## Video, mixes, and recommendations

```python
from youtubesearchpython.future import Mixes, Recommendations, Video

info = await Video.getInfo("pnxL4OOzPEc")
formats = await Video.getFormats("pnxL4OOzPEc")
mix = await Mixes.get("pnxL4OOzPEc")
related = await Recommendations.get("pnxL4OOzPEc")
```

Install `yt-search-python[botguard]` to enable lazy automatic PO-token fallback for bot-confirmation player responses. Explicit `po_token` and `visitor_data` values take precedence, and `auto_po_token=False` disables automatic handling.

## Streams

```python
from youtubesearchpython.future import StreamURLFetcher

fetcher = StreamURLFetcher()
result = await fetcher.getAll("pnxL4OOzPEc")
print(result["streams"])
print(result["unresolved"])
```

## Lifecycle

Async clients are scoped to their event loop and close when the owning loop shuts down normally. `await aclose_clients()` remains available for explicit teardown in tests and unusual long-running lifecycle arrangements.

```python
from youtubesearchpython.future import aclose_clients

await aclose_clients()
```

See the [root README](../../README.md) for installation, the complete API surface, sync examples, compatibility policy, and optional extras.
