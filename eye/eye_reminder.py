# eye_reminder.py
from plyer import notification
import time
import threading

def eye_reminder():
    while True:
        time.sleep(20 * 60)
        notification.notify(
            title="👀 20-20-20 Eye Care Break",
            message="Look 20 feet away for 25 seconds.",
            timeout=25
        )

def blink_reminder():
    while True:
        time.sleep(60)
        notification.notify(
            title="👁️ Blink Reminder",
            message="Blink slowly 5–6 times to keep your eyes moist.",
            timeout=10
        )

if __name__ == "__main__":
    threading.Thread(target=eye_reminder, daemon=True).start()
    threading.Thread(target=blink_reminder, daemon=True).start()
    while True:
        time.sleep(1)
#C:\Users\Mayank\Desktop\eye\eye_reminder.py
#pyinstaller --noconsole --onefile eye_reminder.py
#pyinstaller --noconsole --onefile --hidden-import=plyer.platforms.win.notification eye_reminder.py