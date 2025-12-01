import os
import datetime
from PIL import ImageGrab
import keyboard

SAVE_DIR = r"C:\Users\B1443kouda\Documents\Obsidian Vault\Codex\snips"
LOG_PATH = r"C:\Users\B1443kouda\Documents\Obsidian Vault\Codex\tools\snip_hotkey\snip_hotkey.log"
os.makedirs(SAVE_DIR, exist_ok=True)


def log(message: str) -> None:
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {message}\n")
    except Exception:
        pass


def save_clipboard_image():
    log("F8 pressed")
    try:
        img = ImageGrab.grabclipboard()
    except Exception as e:
        log(f"grabclipboard failed: {e}")
        return
    if img is None:
        log("no image in clipboard")
        return

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(SAVE_DIR, f"snip_{ts}.png")
    try:
        img.save(path, "PNG")
        log(f"saved image -> {path}")
    except Exception as e:
        log(f"save failed: {e}")
        return

    try:
        keyboard.write(path)
        log("typed path into active window")
    except Exception as e:
        log(f"keyboard.write failed: {e}")


def main():
    log("snip_hotkey started (F8)")
    try:
        keyboard.add_hotkey("f8", save_clipboard_image)
        log("hotkey registered")
        keyboard.wait()
    except KeyboardInterrupt:
        log("snip_hotkey stopped by KeyboardInterrupt")
    except Exception as e:
        log(f"add_hotkey failed or runtime error: {e}")


if __name__ == "__main__":
    main()
