# test_base64.py
import requests
import base64

test_cases = [
    ("5L2g5L2/", "赌博"),
    ("5p2A5Lq6", "杀人"),
    ("5bi45by6", "炸弹"),
    ("6Imy5oOF", "色情"),
]

for encoded, expected in test_cases:
    resp = requests.post('http://127.0.0.1:5000/api/preprocess', json={"text": encoded})
    data = resp.json()
    print(f"输入: {encoded}")
    print(f"期望解码: {expected}")
    print(f"实际解码: {data['processed']}")
    print(f"是否匹配: {expected in data['processed']}")
    print("-" * 40)