import json
import os
from src.utils.cleaner import DataCleaner

def convert_to_training_format(input_file, output_file):
    """
    将原始文本转换为 JSONL 格式 (OpenAI ChatML 格式)
    """
    cleaner = DataCleaner()
    processed_data = []

    if not os.path.exists(input_file):
        print(f"错误: 找不到文件 {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 简单的逻辑：假设奇数行为用户提问，偶数行为你的回复（个人风格）
    # 在实际应用中，你可能需要根据日志的时间戳或用户 ID 来区分
    for i in range(0, len(lines) - 1, 2):
        user_input = cleaner.clean_text(lines[i])
        my_response = cleaner.clean_text(lines[i+1])

        if cleaner.is_valid(user_input) and cleaner.is_valid(my_response):
            # 构造符合 OpenAI/Llama 规范的对话结构
            entry = {
                "messages": [
                    {"role": "system", "content": "你现在正在模仿用户的个人对话风格。"},
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": my_response}
                ]
            }
            processed_data.append(entry)

    # 写入 JSONL 文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in processed_data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"处理完成！共生成 {len(processed_data)} 条训练样本。")

if __name__ == "__main__":
    # 示例运行
    convert_to_training_format('data/raw/chat_history.txt', 'data/processed/train_data.jsonl')
