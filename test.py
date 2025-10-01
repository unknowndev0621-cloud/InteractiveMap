import time
import win32gui
from check_win import is_longvinter_running
from read_coordinates import capture_coords
from ENUM import Direction

while True:
    if not is_longvinter_running(foreground_only=False):
        print("❌ Longvinter 실행 안 됨. 2초 후 다시 확인...")
        time.sleep(2)
        continue

    
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)

    if "Longvinter" not in title:
        print("⏸ OCR 일시정지 (다른 창이 포커스됨)")
        time.sleep(1)
        continue

    # Only working when the current window is Longvinter
    x, y, raw = capture_coords(
        Direction.X_LEFT.value,
        Direction.Y_TOP.value,
        Direction.X_RIGHT.value,
        Direction.Y_BOT.value
    )

    if x and y:
        print(f"Results → X: {x}, Y: {y}, original Text: {raw}")
    else:
        print(f"Failed, original Text: {raw}")

    # For Memory overload, sleep every 1sec
    time.sleep(1)
