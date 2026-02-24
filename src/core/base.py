from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """
    所有 AI 提供者的抽象基类
    """
    @abstractmethod
    def chat(self, prompt: str, system_prompt: str = "") -> str:
        """
        统一的聊天接口
        :param prompt: 用户输入
        :param system_prompt: 系统提示词（用于注入个人风格）
        :return: AI 生成的内容
        """
        pass
