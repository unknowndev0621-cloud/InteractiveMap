#installed pywin32
import win32gui

def is_longvinter_running(foreground_only: bool = False) -> bool:
    """
    Function for checking whether Longvinter is running 
    Returns bool for it
    """
    hwnd = None

    def callback(h, _):
        nonlocal hwnd
        if win32gui.IsWindowVisible(h):
            title = win32gui.GetWindowText(h)
            if "Longvinter" in title:
                hwnd = h

    win32gui.EnumWindows(callback, None)

    if not hwnd:
        return False  

    if foreground_only:
        return hwnd == win32gui.GetForegroundWindow()

    return True
