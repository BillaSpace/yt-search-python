# Changelog

## [2.2.2] - Unreleased

- Restored live streaming-format retrieval with current, internally consistent Innertube client profiles.
- Preserved all sync, async, and legacy import paths while fixing legacy transport initialization.
- Parsed durations and metadata from the current recommendation lockup response shape.
- Added optional BotGuard-backed PO-token integration through the companion provider.
- Added lazy automatic BotGuard fallback for bot-confirmation player responses in sync and async video APIs.
- Scoped generated web tokens to WEB/MWEB retries and kept successful Android-family requests token-free.
- Added automatic video-bound token application when `StreamURLFetcher` receives a video ID or URL.
- Added the global sync and async `Mixes` API with video ID, video URL, and `RD...` mix input support.
- Normalized `Mixes` items to the same field contract as `Recommendations` while preserving YouTube's order.

## [2.2.1] - 2026-08-14

### HTTP and resource lifecycle
- Fixed async client shutdown to use `AsyncClient.aclose()`.
- Removed the invalid async `.close()` cleanup path.
- Centralized sync/async request transport and request-body construction.
- Bounded keep-alive reuse to 8 idle connections with a 5-second expiry to balance connection reuse with FD/`CLOSE_WAIT` safety.
- HTTP client lifecycle is now internally managed: sync pools close at process exit and async pools close with their owning event loops. `close_clients()` / `aclose_clients()` remain optional forced-teardown APIs.
- Made proxy clients request-scoped and deterministically closed.
- Restored bounded default request timeouts when callers pass `None`.
- Forwarded per-request custom headers through the canonical transport.
- Isolated transcript cookie state from the shared HTTP clients.
- Made temporary downloaded-cookie ownership/cleanup deterministic.

### Search and pagination
- Added optional `VideosSearch(..., is_live=True)` support in sync and async APIs.
- Added live badge detection to video search results.
- Fixed stale search continuation state that could repeat the final page.
- Fixed malformed `richItemRenderer` entries from crashing a search page.
- Fixed `ChannelSearch.next()` to use continuation tokens instead of repeating the first request.
- Fixed hashtag continuation exhaustion so the last page is not fetched repeatedly.
- Fixed comments continuation exhaustion and instance-state isolation.

### Playlists
- Added native Innertube support for YouTube Mix/Radio `RD...` playlists through `/next`.
- Parse direct `playlistPanelVideoRenderer` entries even when `playlistPanelRenderer` is absent.
- Preserve exact YouTube response order with stable first-occurrence duplicate removal.
- Prevent comment/engagement continuation tokens in Mix responses from being followed as playlist pages.
- Retained regular playlist browse/continuation support with stable duplicate removal.

### Video, thumbnails and recommendations
- Fixed `Video` JSON result mode returning a dict through a dead result path.
- Added `po_token` and `visitor_data` support to sync/async video player requests.
- Prefer player responses containing direct stream URLs when multiple Innertube clients are tried.
- `Video.getFormats()` now fails clearly when no streaming formats are returned instead of substituting unrelated search metadata.
- Normalize YouTube thumbnails against the actual video ID and reject mismatched video thumbnails.
- Removed unnecessary search requests that were previously used only to replace thumbnails.
- Improved Recommendations parsing for compact, regular and lockup video models.
- Recommendations now preserve order, skip the source video and stably remove duplicate video IDs.

### StreamURLFetcher
- Removed the yt-dlp dependency from stream URL extraction.
- Added direct video ID/link input in addition to existing format-dictionary input.
- Added sync/async PO-token and visitor-data forwarding.
- Resolve direct URLs and cipher entries that already contain a usable signature.
- Surface encrypted signature entries under `unresolved` instead of returning invalid URLs.
- Mark URLs that still contain an `n` parameter with `throttled=True`.

### Suggestions, transcripts and channels
- Fixed the duplicate `Suggestions.get` definition that made one public path unreachable.
- Forward `YTS_IDENTITY_TOKEN` correctly and raise explicit errors on non-200 suggestion responses.
- Fixed transcript language selection and isolated native caption requests from global cookie state.
- Kept the optional yt-dlp transcript fallback behind the `transcript` extra.
- Improved channel playlist pagination order and stable duplicate handling.

### Packaging and compatibility
- Package version is consistent in sync/async namespaces and build metadata.
- Added an explicit `handlers` package marker so compatibility handlers are included deterministically.
- Included `README.md`, `CHANGELOG.md` and `LICENSE` in source distributions.
- Set the supported runtime floor to Python 3.9+ and retained legacy public search imports.
- Audited Python 3.14-facing asyncio/deprecation behavior and hardened simultaneous multi-loop runtime use.

## [2.1.1] - 2026-07-30
- Consolidated request/component handling, fixed multiple API crashes and improved httpx 0.28 compatibility.

## [2.0.0] - 2026-01-18
- Added the `future` async namespace and modernized the project structure.
