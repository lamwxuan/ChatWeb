import json
from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import datetime, time
from chatgpt.chatgpt import Session
from chatgpt.chatgpt import OpenAIBot

# class chatGptConsumer(SyncConsumer):
#     def websocket_connect(self, event):
#         print("%s:%d  connected !" %(self.scope['client'][0], self.scope['client'][1]))

#         self.accept();
#         # self.send({
#         #     "type": "websocket.accept",
#         # })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })
#         self.send('auto reply'.encode('utf-8'))


#     def disconnect(self, close_code):
#         # Called when the socket closes
#         print("%s:%d  disconnected !" %(self.scope['client'][0], self.scope['client'][1]))
#         self.close()

class chatGptConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        print("%s:%d  connected !" %(self.scope['client'][0], self.scope['client'][1]))

        content = 'connect success'
        temp = json.dumps({"emit":"chatMessage","system":True,"id":-2, 'type': "friend", 'content': content, "cid": 0, "mine": False})
        self.send(text_data=temp) 


    def receive(self, text_data=None, bytes_data=None):

        # Called with either text_data or bytes_data for each frame
        # You can call:
        receiveData = json.loads(text_data)
        prompt = Session.combine_session(receiveData['data']['mine']['content'])
        AiRespond =  OpenAIBot().chatwithGpt(prompt) 
        temp = json.dumps({"emit":"chatMessage", "username": "chatGPT","id":receiveData['data']['to']['id'], 'type': receiveData['data']['to']['type'], 'content': AiRespond,"fromid":receiveData['data']['to']['id'], "timestamp": time.time()*1000, "mine": False})
        # temp = json.dumps({"emit":"chatMessage","data":{"mine":{"mine":False, "id":receiveData['data']['to']['id'],"content":AiRespond},"to":{"name":"chatGPT","type":"friend","id":receiveData['data']['to']['id']}}})
        
        
        self.send(temp)

    def disconnect(self, close_code):
        # Called when the socket closes
        self.close()
        print("%s:%d  disconnected" %(self.scope['client'][0], self.scope['client'][1]))

