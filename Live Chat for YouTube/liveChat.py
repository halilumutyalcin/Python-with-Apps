######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################


from pytchat import LiveChat
from termcolor import colored

livechat = LiveChat(video_id="")

while livechat.is_alive():
    try:
        chatdata = livechat.get()
        for c in chatdata.items:
            print(colored(c.datetime, "red"), colored(c.author.name, "green"), "- " + c.message)
            chatdata.tick()
    except KeyboardInterrupt:
        livechat.terminate()
        break
