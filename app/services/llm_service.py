class LLMService:


    def __init__(self) -> None:
       
        ...

    async def generate(
        self,
        prompt: str,
        system: str | None = None,
        json_mode: bool = False,
        temperature: float = 0.0,
        use_cache: bool = True,
    ) -> str:
        ...

    def _cache_key(
        self,
        prompt: str,
        system: str | None,
        json_mode: bool,
        temperature: float,
    ) -> str:
        ...

    async def _call_provider(
        self,
        prompt: str,
        system: str | None,
        json_mode: bool,
        temperature: float,
    ) -> str:
        
        ...

    async def _call_ollama(
        self,
        prompt: str,
        system: str | None,
        json_mode: bool,
        temperature: float,
    ) -> str:
        ...

    async def _call_groq(
        self,
        prompt: str,
        system: str | None,
        json_mode: bool,
        temperature: float,
    ) -> str:
        raise NotImplementedError("Groq provider is not written yet")

    async def _call_gemini(
        self,
        prompt: str,
        system: str | None,
        json_mode: bool,
        temperature: float,
    ) -> str:
        raise NotImplementedError("Gemini provider is not written yet")