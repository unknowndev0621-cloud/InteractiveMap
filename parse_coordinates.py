import re

def parse_coordinates(text: str):
    if not text:
        return None, None

    # OCR 교정 
    corrections = {
        "O": "0", "o": "0",
        "l": "1", "I": "1",
        "j": "1", "J": "1",
        ";W": "W", ";E": "E", ";N": "N", ";S": "S"  
    }
    for k, v in corrections.items():
        text = text.replace(k, v)

    print("🔧 After corrections:", text)  # 디버깅용

    # 정규식: ° 또는 ; 둘 다 허용
    matches = re.findall(r"([0-9joOlJ]{1,3})[°;]?\s*([NSEW])", text)

    if len(matches) == 2:
        (y_num, y_dir), (x_num, x_dir) = matches
        y = f"{y_num}°{y_dir}"
        x = f"{x_num}°{x_dir}"
        return y, x

    return None, None
