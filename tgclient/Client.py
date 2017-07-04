"""
    Author: Negative
    Telegram: @Negative
"""

import requests
import re
import json
import six

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self._commands = {}
        self._handler = {}
        self._callback_handler = []
        self._inline_handler = []
        self._report_http_err = True

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def _req(self, method, data, files=None):
        if files is not None:

            request = requests.post("https://api.telegram.org/bot{}/{}".format(self.token, method),
                                    data=data, files=files)
        else:
            request = requests.post("https://api.telegram.org/bot{}/{}".format(self.token, method),
                                    data=data)

        if request.status_code == 200:
            j = request.json()
            if 'result' in j and 'ok' in j:
                return j['result']
        else:
            if self._report_http_err:
                raise Exception("Error HTTP : {}\n{}".format(request.status_code, request.content))
            else:
                print("Error HTTP : {}\n{}".format(request.status_code, request.content))

    def command(self, regex):

        def decorator(d):
            self._commands[regex] = d

        return decorator

    def message(self, type_message):

        def decorator(d):
            self._handler[type_message] = d

        return decorator

    def callback_query(self):
        def decorator(d):
            self._callback_handler.append(d)

        return decorator

    def inline_query(self):

        def decorator(d):
            self._inline_handler.append(d)

        return decorator

    def getMe(self):
        return self._req("getMe", {})

    def sendMessage(self, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None):
        query = {}

        if chat_id and text:
            query['chat_id'] = chat_id
            query['text'] = text

        if parse_mode:
            query['parse_mode'] = parse_mode

        if disable_web_page_preview:
            query['disable_web_page_preview'] = disable_web_page_preview

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendMessage", query)

    def sendPhoto(self, chat_id, photo, caption=None, disable_notification=None,
                  reply_to_message_id=None, reply_markup=None):

        query = {}
        files = {}

        if isinstance(photo, six.string_types):
            query['photo'] = photo
        else:
            files['photo'] = photo

        if chat_id:
            query['chat_id'] = chat_id

        if caption:
            query['caption'] = caption

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendPhoto", query, files)

    def getUpdates(self, offset=0, limit=0, timeout=0, allowed_updates=None):

        query = {}
        if offset:
            query['offset'] = offset
        if limit:
            query['limit'] = limit
        if timeout:
            query['timeout'] = timeout

        if allowed_updates:
            query['allowed_updates'] = allowed_updates

        return self._req("getUpdates", query)


    def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=None):

        query = {}
        if chat_id and from_chat_id and message_id:
            query['chat_id'] = chat_id
            query['from_chat_id'] = from_chat_id
            query['message_id'] = message_id

        if disable_notification:
            query['disable_notification'] = disable_notification

        return self._req('forwardMessage', query)


    def sendAudio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None,
                  disable_notification=None, reply_to_message_id=None, reply_markup=None):

        query = {}
        files = {}

        if chat_id and audio:
            if isinstance(audio, six.string_types):
                query['audio'] = audio
            else:
                files['audio'] = audio

        if caption:
            query['caption'] = caption

        if duration:
            query['duration'] = duration

        if performer:
            query['performer'] = performer

        if title:
            query['title'] = title

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendAudio", query, files)


    def sendDocument(self, chat_id, document, caption=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):

        query = {}
        files = {}

        if chat_id and document:
            query['chat_id'] = chat_id
            if isinstance(document, six.string_types):
                query['document'] = document
            else:
                files['document'] = document

        if caption:
            query['caption'] = caption

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendDocument", query, files)


    def answerCallbackQuery(self, callback_query_id, text, show_alert=False, url=None, cache_time=None):

        query = {}
        if callback_query_id and text:
            query['callback_query_id'] = callback_query_id
            query['text'] = text

        if show_alert:
            query['show_alert'] = show_alert

        if url:
            query['url'] = url

        if cache_time:
            query['cache_time'] = cache_time

        return self._req("answerCallbackQuery", query)

    def sendSticker(self, chat_id, sticker, disable_notification=False, reply_to_message_id=None,
                    reply_markup=None):

        query = {}
        files = {}

        if chat_id and sticker:
            if isinstance(sticker, six.string_types):
                query['sticker'] = sticker
            else:
                files['sticker'] = sticker
            query['chat_id'] = chat_id

        if disable_notification:
            query['disable_notification'] = disable_notification
        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendSticker", query, files)

    def sendVoice(self, chat_id, voice, caption=None, duration=None,
                  disable_notification=None, reply_to_message_id=None, reply_markup=None):

        query = {}
        files = {}

        if chat_id and voice:
            if isinstance(voice, six.string_types):
                query['voice'] = voice
            else:
                files['voice'] = voice
            query['chat_id'] = chat_id

        if caption:
            query['caption'] = caption

        if duration:
            query['duration'] = duration

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendVoice", query, files)

    def sendVideoNote(self, chat_id, video_note, duration=None, length=None, disable_notification=None,
                      reply_to_message_id=None, reply_markup=None):

        query = {}
        files = {}

        if chat_id and video_note:
            if isinstance(video_note, six.string_types):
                query['video_note'] = video_note

            else:
                files['video_note'] = video_note

            query['chat_id'] = chat_id

        if duration:
            query['duration'] = duration

        if length:
            query['length'] = length

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = reply_markup

        return self._req("sendVideoNote", query, files)

    def sendLocation(self, chat_id, latitude, longitude, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):

        query = {}

        if chat_id and latitude and longitude:
            query['chat_id'] = chat_id
            query['latitude'] = latitude
            query['longitude'] = longitude

        if disable_notification:
            query['disable_notification'] = disable_notification

        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendLocation", query)

    def sendVenue(self, chat_id, latitude, longitude, title, address,
                  foursquare_id=None, disable_notification=False, reply_to_message_id=0,
                  reply_markup=None):

        query = {}
        if chat_id and latitude and longitude and title and address:

            query['chat_id'] = chat_id
            query['latitude'] = latitude
            query['longitude'] = longitude
            query['title'] = title
            query['address'] = address

        if foursquare_id:
            query['foursquare_id'] = foursquare_id

        if disable_notification:
            query['disable_notification'] = disable_notification
        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendVenue", query)

    def sendContact(self, chat_id, phone_number, first_name,
                    last_name=None, disable_notification=False, reply_to_message_id=0,
                    reply_markup=None):

        query = {}
        if chat_id and phone_number and first_name:
            query['chat_id'] = chat_id
            query['phone_number'] = phone_number
            query['first_name'] = first_name

        if last_name:
            query['last_name'] = last_name

        if disable_notification:
            query['disable_notification'] = disable_notification
        if reply_to_message_id:
            query['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("sendContact", query)

    def sendChatAction(self, chat_id, action):

        query = {}
        if chat_id and action:
            query['chat_id'] = chat_id
            query['action'] = action

        return self._req("sendChatAction", query)

    def getUserProfilePhotos(self, user_id, offset=0, limit=0):

        query = {}

        if user_id:
            query['user_id'] = user_id

        if offset:
            query['offset'] = offset

        if limit:
            query['limit'] = limit

        return self._req('getUserProfilePhotos', query)


    def getFile(self, file_id):

        query = {}
        if file_id:
            query['file_id'] = file_id

        return self._req("getFile", query)



    def kickChatMember(self, chat_id, user_id):

        query = {}

        if chat_id and user_id:
            query['chat_id'] = chat_id
            query['user_id'] = user_id

        return self._req("kickChatMember", query)

    def unbanChatMember(self, chat_id, user_id):

        query = {}

        if chat_id and user_id:
            query['chat_id'] = chat_id
            query['user_id'] = user_id

        return self._req("unbanChatMember", query)

    def restrictChatMember(self, chat_id, user_id, until_date=0, can_send_messages=False,
                           can_send_media_messages=False, can_send_other_messages=False,
                           can_add_web_page_previews=False):

        query = {}
        if chat_id and user_id:
            query['chat_id'] = chat_id
            query['user_id'] = user_id


        if until_date:
            query['until_date'] = until_date

        if can_send_media_messages is not None:
            query['can_send_media_messages'] = can_send_media_messages

        if can_send_other_messages is not None:
            query['can_send_other_messages'] = can_send_other_messages

        if can_add_web_page_previews is not None:
            query['can_add_web_page_previews'] = can_add_web_page_previews

        if can_send_messages is not None:
            query['can_send_messages'] = can_send_messages

        return self._req("restrictChatMember", query)

    def promoteChatMember(self, chat_id, user_id, can_change_info=False,
                          can_post_messages=False, can_edit_messages=False,
                          can_delete_messages=False, can_invite_users=False,
                          can_restrict_members=False, can_pin_messages=False,
                          can_promote_members=False):

        query = {}
        if chat_id and user_id:
            query['chat_id'] = chat_id
            query['user_id'] = user_id

        if can_change_info is not None:
            query['can_change_info'] = can_change_info

        if can_post_messages is not None:
            query['can_post_messages'] = can_post_messages

        if can_edit_messages is not None:
            query['can_edit_messages'] = can_edit_messages

        if can_delete_messages is not None:
            query['can_delete_messages'] = can_delete_messages

        if can_invite_users is not None:
            query['can_invite_users'] = can_invite_users

        if can_restrict_members is not None:
            query['can_restrict_members'] = can_restrict_members

        if can_pin_messages is not None:
            query['can_pin_messages'] = can_pin_messages

        if can_promote_members is not None:
            query['can_promote_members'] = can_promote_members

        return self._req("promoteChatMember", query)


    def exportChatInviteLink(self, chat_id):

        return self._req("exportChatInviteLink", {'chat_id': chat_id})

    def setChatPhoto(self, chat_id, photo):

        query = {}
        files = {}

        if chat_id and photo:
            if isinstance(photo, six.string_types):
                query['photo'] = photo
            else:
                files['photo'] = photo
            query['chat_id'] = chat_id

        return self._req("setChatPhoto", query, files)

    def deleteChatPhoto(self, chat_id):

        return self._req("deleteChatPhoto", {'chat_id': chat_id})

    def setChatTitle(self, chat_id, title):

        return self._req("setChatTitle", {'chat_id': chat_id, 'title': title})


    def setChatDescription(self, chat_id, description):

        if chat_id and description:
            return self._req("setChatDescription", {
                'chat_id': chat_id,
                'description': description
            })

    def pinChatMessage(self, chat_id, message_id, disable_notification=False):

        query = {}

        if chat_id and message_id:
            query['chat_id'] = chat_id
            query['message_id'] = message_id

        if disable_notification:
            query['disable_notification'] = disable_notification

        return self._req("pinChatMessage", query)


    def unpinChatMessage(self, chat_id):

        return self._req("unpinChatMessage", {'chat_id': chat_id})

    def leaveChat(self, chat_id):

        return self._req("leaveChat", {'chat_id': chat_id})

    def getChat(self, chat_id):

        return self._req("getChat", {'chat_id': chat_id})

    def getChatAdministrators(self, chat_id):

        return self._req("getChatAdministrators", {'chat_id': chat_id})

    def getChatMembersCount(self, chat_id):

        return self._req("getChatMembersCount", {'chat_id': chat_id})

    def getChatMember(self, chat_id, user_id):

        return self._req("getChatMember", {'chat_id': chat_id, 'user_id': user_id})


    def editMessageText(self, text, chat_id=None, message_id=None, inline_message_id=None,
                        parse_mode=None, disable_web_page_preview=None,
                        reply_markup=None):

        query = {}

        if text:
            query['text'] = text

        if chat_id and message_id:
            query['chat_id'] = chat_id
            query['message_id'] = message_id
        if inline_message_id:
            query['inline_message_id'] = inline_message_id

        if parse_mode:
            query['parse_mode'] = parse_mode

        if disable_web_page_preview:
            query['disable_web_page_preview'] = disable_web_page_preview

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("editMessageText", query)

    def editMessageCaption(self, chat_id=None, message_id=None,
                           inline_message_id=None, caption=None,
                           reply_markup=None):

        query = {}
        if chat_id and message_id and not inline_message_id:
            query['chat_id'] = chat_id
            query['message_id'] = message_id

        elif inline_message_id:
            query['inline_message_id'] = inline_message_id

        if caption:
            query['caption'] = caption

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("editMessageCaption", query)

    def editMessageReplyMarkup(self, chat_id=None, message_id=None, inline_message_id=None,
                               reply_markup=None):

        query = {}
        if chat_id and message_id and not inline_message_id:
            query['chat_id'] = chat_id
            query['message_id'] = message_id

        elif inline_message_id:
            query['inline_message_id'] = inline_message_id

        if reply_markup:
            query['reply_markup'] = json.dumps(reply_markup)

        return self._req("editMessageReplyMarkup", query)

    def deleteMessage(self, chat_id, message_id):

        return self._req("deleteMessage", {
            'chat_id': chat_id,
            'message_id': message_id
        })

    def answerInlineQuery(self, inline_query_id, results,
                          cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None,
                          switch_pm_parameter=None):

        query = {}

        if inline_query_id and results:
            query['inline_query_id'] = inline_query_id
            query['results'] = json.dumps(results)

        if cache_time:
            query['cache_time'] = cache_time

        if next_offset:
            query['next_offset'] = next_offset

        if switch_pm_text:
            query['switch_pm_text'] = switch_pm_text

        if switch_pm_parameter:
            query['switch_pm_parameter'] = switch_pm_parameter

        if is_personal is not None:
            query['is_personal'] = is_personal


        return self._req("answerInlineQuery", query)




    def run(self, report_http_errors=True):

        if not report_http_errors:
            self._report_http_err = False

        offset = 0
        while True:
            updates = self.getUpdates(offset + 1)

            if updates:
                for result in updates:
                    if 'update_id' in result and result['update_id'] > offset:
                        offset = result['update_id']

                        if 'message' in result:
                            if 'text' in result['message']:
                                for k, v in self._commands.items():

                                    regex = re.compile(k, flags=re.MULTILINE | re.DOTALL)
                                    m = regex.match(result['message']['text'])
                                    if m:
                                        try:
                                            v(result['message'], m)
                                        except TypeError:
                                            v(result['message'])

                            for k, v in self._handler.items():
                                if k in result['message']:
                                    v(result['message'])

                        elif 'callback_query' in result:
                            for v in self._callback_handler:
                                v(result['callback_query'])

                        elif 'inline_query' in result:
                            for v in self._inline_handler:
                                v(result['inline_query'])
