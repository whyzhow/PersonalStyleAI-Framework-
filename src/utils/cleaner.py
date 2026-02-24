import re

class DataCleaner:
    """
    用于清理原始文本数据的工具类
    """
    @staticmethod
    def clean_text(text: str) -> str:
        # 1. 去除 URL 链接
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        
        # 2. 去除特定的系统消息或表情占位符 (例如微信中的 [图片], [表情])
        text = re.sub(r'\[[^\]]+\]', '', text)
        
        # 3. 去除多余的空白字符和换行
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        
        return text

    @staticmethod
    def is_valid(text: str) -> bool:
        """
        判断文本是否具有训练价值（如过短的内容通常舍弃）
        """
        if not text or len(text) < 2:
            return False
        return True
