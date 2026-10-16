import sys as _sys

from youtubesearchpython import compat as _compat
from youtubesearchpython import sync as _sync
from youtubesearchpython.attestation import BotGuard
from youtubesearchpython.compat import SearchPlaylists, SearchVideos, searchYoutube
from youtubesearchpython.core import componenthandler as _componenthandler
from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import close_clients
from youtubesearchpython.core.utils import *
from youtubesearchpython.sync import (
    Channel,
    ChannelSearch,
    ChannelsSearch,
    Comments,
    CustomSearch,
    Hashtag,
    Mixes,
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
for _name in ('search','extras','mixes','streamurlfetcher'): _sys.modules[f'{__name__}.{_name}']=_sync
_sys.modules[f'{__name__}.legacy']=_compat
_sys.modules[f'{__name__}.handlers']=_compat
_sys.modules[f'{__name__}.handlers.componenthandler']=_componenthandler
_sys.modules[f'{__name__}.handlers.requesthandler']=_compat
