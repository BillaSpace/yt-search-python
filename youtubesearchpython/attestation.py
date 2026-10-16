class BotGuard:
    @staticmethod
    def _provider(**options):
        try:
            from ytsp_po_provider import POTokenProvider
        except ImportError as error:
            raise RuntimeError("Install yt-search-python[botguard] to enable BotGuard token generation") from error
        return POTokenProvider(**options)

    @classmethod
    def generate(cls, video_id: str, bypass_cache: bool = False, **options) -> str:
        return cls.resolve(video_id, bypass_cache=bypass_cache, **options).token

    @classmethod
    async def agenerate(cls, video_id: str, bypass_cache: bool = False, **options) -> str:
        return (await cls.aresolve(video_id, bypass_cache=bypass_cache, **options)).token

    @classmethod
    def resolve(cls, video_id: str, bypass_cache: bool = False, **options):
        return cls._provider(**options).get(video_id=video_id, bypass_cache=bypass_cache)

    @classmethod
    async def aresolve(cls, video_id: str, bypass_cache: bool = False, **options):
        return await cls._provider(**options).aget(video_id=video_id, bypass_cache=bypass_cache)
