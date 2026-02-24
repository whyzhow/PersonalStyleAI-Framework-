from src.core.providers.openai_p import OpenAIProvider
from src.core.providers.ollama_p import OllamaProvider

def get_llm(provider_name: str, **kwargs):
    """
    根据名称返回对应的 AI 实例
    """
    providers = {
        "openai": OpenAIProvider,
        "ollama": OllamaProvider,
        # 之后可以继续添加 anthropic, gemini 等
    }
    
    provider_class = providers.get(provider_name.lower())
    if not provider_class:
        raise ValueError(f"不支持的提供者: {provider_name}")
    
    return provider_class(**kwargs)
