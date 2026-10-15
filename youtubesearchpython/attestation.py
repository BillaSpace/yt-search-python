class BotGuard:
    @staticmethod
    def _provider(**options):
        try:
            from ytsp_po_provider import POTokenProvider
        except ImportError as error:
            raise RuntimeError("Install yt-search-python[botguard] to enable BotGuard token generation") from error
        return POTokenProvider(**options)

    @classmethod
    def generate(cls, video_id: str, **options) -> str:
        return cls._provider(**options).get(video_id=video_id).token

    @classmethod
    async def agenerate(cls, video_id: str, **options) -> str:
        return (await cls._provider(**options).aget(video_id=video_id)).token
