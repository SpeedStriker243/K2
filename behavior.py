import social_media as SocialMedia
import human_functions as Person
import pass_lock as PassChecker
from datetime import datetime

PassChecker.CheckForPass("NWORDPASS.md")
Awake = True

while Awake == True:
    print("K2 now active")
    SocialMedia.Twitter.Login("@yaboiK2")
    SocialMedia.Discord.Login("K2", 9711, 521830344937308160)
    Person.Intelligence.Enable = True
    try:
        if datetime.current_time.hour > 11 and datetime.current_time.minute > 59:
            Awake = False
    except:
        print("datetime error")
        break

print("K2 now inactive")
