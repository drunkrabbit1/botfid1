import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

tkn = ""
vk_session = vk_api.VkApi(token=tkn)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if 
