import sys as _sys

from youtubesearchpython import sync as _sync
from youtubesearchpython.attestation import BotGuard
from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import close_clients
from youtubesearchpython.core.utils import *
from youtubesearchpython.legacy import SearchPlaylists, SearchVideos
from youtubesearchpython.legacy import SearchVideos as searchYoutube
from youtubesearchpython.sync import (
    Channel,
    ChannelSearch,
    ChannelsSearch,
    Comments,
    CustomSearch,
    Hashtag,
    Playlist,
    PlaylistsSearch,
    Recommendations,
    Search,
    StreamURLFetcher,
    Suggestions,
    SuggestionsSession,
    Transcript,
    Video,
    VideosSearch,
)

__title__='yt-search-python'
__version__='2.2.2'
__author__='Prakhar-Shukla'
__license__='MIT'
for _name in ('search','extras','streamurlfetcher'): _sys.modules[f'{__name__}.{_name}']=_sync
