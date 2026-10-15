import sys as _sys

from . import requests as _requests
from . import search as _search
from . import social as _social
from . import video as _video
from .constants import *
from .playlist import PlaylistCore
from .search import ChannelSearchCore, SearchCore
from .social import (
    ChannelCore,
    CommentsCore,
    HashtagCore,
    SuggestionsCore,
    TranscriptCore,
)
from .video import RecommendationsCore, StreamURLFetcherCore, VideoCore

_aliases={'channelsearch':_search,'channel':_social,'comments':_social,'hashtag':_social,'suggestions':_social,'transcript':_social,'recommendations':_video,'streamurlfetcher':_video,'cookies':_requests,'exceptions':_requests}
for _name,_module in _aliases.items(): _sys.modules[f'{__name__}.{_name}']=_module
