from telethon import TelegramClient, events, sync
#
from time import gmtime, strftime
from emoji import emojize
import asyncio
#

import zeus.client, zeus.test, zeus.bombs, zeus.help, zeus.loading, zeus.emoji, zeus.dump, zeus.sexy, zeus.type, zeus.magicrun, zeus.animation, zeus.animation2, zeus.chatinfo, zeus.mq, zeus.mute, zeus.nq, zeus.fuck, zeus.rev, zeus.tr, zeus.userinfo, zeus.base64, zeus.react, zeus.snow, zeus.ar, zeus.smsbomb, zeus.url
#
client = zeus.client.client
#
with client as friday:
	friday.add_event_handler(zeus.test.test) 
with client as friday:
	friday.add_event_handler(zeus.bombs.bombs)
with client as friday:
	friday.add_event_handler(zeus.help.help) 
with client as friday:
	friday.add_event_handler(zeus.loading.loading) 
with client as friday:
	friday.add_event_handler(zeus.emoji.itachi) 
with client as friday:
	friday.add_event_handler(zeus.dump.dump) 	
with client as friday:
	friday.add_event_handler(zeus.sexy.sexy) 
with client as friday:
	friday.add_event_handler(zeus.type.type) 
with client as friday:
	friday.add_event_handler(zeus.magicrun.magicrun) 	
with client as friday:
	friday.add_event_handler(zeus.animation.lul)
with client as friday:
	friday.add_event_handler(zeus.animation.snake)
with client as friday:
	friday.add_event_handler(zeus.animation.nothappy)
with client as friday:
	friday.add_event_handler(zeus.animation.clock)
with client as friday:
	friday.add_event_handler(zeus.animation.muah)
with client as friday:
	friday.add_event_handler(zeus.animation.heart)	
with client as friday:
	friday.add_event_handler(zeus.animation.gym)
with client as friday:
	friday.add_event_handler(zeus.animation.earth)
with client as friday:
	friday.add_event_handler(zeus.animation.moon)
with client as friday:
	friday.add_event_handler(zeus.animation.candy)
with client as friday:
	friday.add_event_handler(zeus.animation.smoon)
with client as friday:
	friday.add_event_handler(zeus.animation.tmoon)
with client as friday:
	friday.add_event_handler(zeus.animation.clown)
with client as friday:
	friday.add_event_handler(zeus.animation2.star)
with client as friday:
	friday.add_event_handler(zeus.animation2.boxs)		
with client as friday:
	friday.add_event_handler(zeus.animation2.rain)
with client as friday:
	friday.add_event_handler(zeus.animation2.clol)
with client as friday:
	friday.add_event_handler(zeus.animation2.odra)
with client as friday:
	friday.add_event_handler(zeus.animation2.fleaveme)		
with client as friday:
	friday.add_event_handler(zeus.animation2.loveu)
with client as friday:
	friday.add_event_handler(zeus.animation2.plane)
with client as friday:
	friday.add_event_handler(zeus.animation2.police)
with client as friday:
	friday.add_event_handler(zeus.animation2.jio)		
with client as friday:
	friday.add_event_handler(zeus.animation2.solarsystem)
with client as friday:
	friday.add_event_handler(zeus.chatinfo.info)
with client as friday:
	friday.add_event_handler(zeus.mq.mq)
with client as friday:
	friday.add_event_handler(zeus.mute.mute)		
with client as friday:
	friday.add_event_handler(zeus.nq.nq)	
with client as friday:
	friday.add_event_handler(zeus.fuck.fuck)					
with client as friday:
	friday.add_event_handler(zeus.rev.rev)										
with client as friday:
	friday.add_event_handler(zeus.tr.tr)
with client as friday:
	friday.add_event_handler(zeus.userinfo.userinfo)
with client as friday:
	friday.add_event_handler(zeus.base64.runb64)				
with client as friday:
	friday.add_event_handler(zeus.react.react)
with client as friday:
	friday.add_event_handler(zeus.snow.snow)
with client as friday:
	friday.add_event_handler(zeus.ar.runar)
	
with client as friday:
	friday.add_event_handler(zeus.smsbomb.runj)					
with client as friday:
	friday.add_event_handler(zeus.url.runus)
	

client.start()
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
                                                   

\033[1;32mUSERBOT STARTED""")

client.run_until_disconnected()