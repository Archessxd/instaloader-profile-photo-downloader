import instaloader
import sys

def DownloadPp(target):
    print(f"trying to download {target} 's profile picture ")
    instaloader.Instaloader().download_profile(target,profile_pic_only=False)
    print("downloaded succesfully")

try:
    uName = str(input("type profile name :"))
    DownloadPp(uName)

except Exception as e:
    if(type(e.__cause__) == "instaloader.exceptions.LoginRequiredException"):
        sys.exit()

