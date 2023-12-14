token = ""

from MyBaleCloud.balecloud import BaleCloud
import time

app = BaleCloud(token)

msg_list = []

dataBase : dict = {}

def learn(what : str, data : str):
    dataBase[what] = data
    return True

while 1:
    for msg in app.getUpdates_1():
        text = str(msg.text)
        chat = msg.chat_id
        msg_id = msg.message_id
        if not msg_id in msg_list:
            msg_list.append(msg_id)
            print(text)
            if text.startswith('learn'):
                study = text.replace('learn ', '')
                print(msg.reply_to_message_text)
                
                if msg.reply_to_message_text == None:
                    app.sendMessage('Please Reply a Data', chat, msg_id)
                    
                else:
                    learn(msg.reply_to_message_text, study)
                    app.sendMessage(f'I Learn {study} for {msg.reply_to_message_text}', chat, msg_id)
                       
                    
            for k, v in dataBase.items():
                
                if k in text:
                    app.sendMessage(str(v).replace('#time', "{}".format(time.strftime("%H:%M:%S"))).replace('#name', str(msg.chat_side['first_name'])).replace('#id', str(msg.chat_side['id'])).replace('#username', msg.chat_side['username'] if "username" in msg.chat_side.keys() else "#not").replace('#bio', msg.chat_side['bio'] if "bio" in msg.chat_side.keys() else "#not"), chat, msg_id)
                else:
                    pass
        
        else:
            msg_list.append(msg_id)
