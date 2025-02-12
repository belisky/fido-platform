from my_service.config.config import settings
from my_service.models.models import ArgoCDCreds
import aiohttp
from cachetools import TTLCache
from my_service.utils.logger import setup_logger

creds = ArgoCDCreds(
    username=settings.ARGOCD_USERNAME,
    password=settings.ARGOCD_PASSWORD
)

logger = setup_logger()
token_cache = TTLCache(maxsize=1, ttl=settings.TOKEN_CACHE_TTL)


async def fetch_argocd_token():
    """Fetch JWT token from ArgoCD and store it with TTL based on expiration."""

    creds = ArgoCDCreds(
        username=settings.ARGOCD_USERNAME,
        password=settings.ARGOCD_PASSWORD
    )

    async with aiohttp.ClientSession() as temp_session:
        async with temp_session.post(
            f"https://{settings.ARGOCD_URL}/api/v1/session",
                json=creds.model_dump(),
                verify_ssl=False,
        ) as resp:
            data = await resp.json()
            token = data.get("token")
            if token:
                logger.debug(
                    f"ArgoCD session token has been successfully, setting up cache TTL")
                try:
                    decoded = jwt.decode(
                        token, options={"verify_signature": False})
                    exp = decoded.get("exp", int(
                        time.time()) + settings.TOKEN_CACHE_TTL)
                    ttl = max(exp - int(time.time()) - 10, 60)
                except Exception:
                    ttl = settings.TOKEN_CACHE_TTL
                token_cache.clear()
                token_cache[token] = ttl
                return token
            raise Exception("Failed to fetch ArgoCD token")


async def get_token():
    """Retrieve token from cache or fetch a new one if expired."""
    if not token_cache:
        logger.info("Cache is empty, fetching a new token")
        return await fetch_argocd_token()
    logger.info("Cache hit! found token in cache")
    logger.info(f"Cache: {token_cache}")
    return next(iter(token_cache.keys()))
