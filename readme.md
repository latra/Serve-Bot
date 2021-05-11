!serve terraria 
- Inicia server de terraria 
El servidor desde el que se lanza debe salir el servers.json
Solo un Terraria server por servidor


Discord - BOT - server - check - return ok/ko - if ok run server

!stop terraria 
- Detiene server de terraria
discord - bot - server 

# SERVE | STOP
/api
BOT -> SERVER (TERRARIA)
server_uid
game
action
channel_uid (Only serve)
callbackurl  (Only serve)


## callback (Only serve)
SERVER -> BOT
server_uid
channel_uid 
game
status
ip
port

STATUS>
    200 -> OK, SERVER STARTED
    403 -> SERVER WITHOUT PERMISSION
    440 -> SERVER ALREADY RUNNING/STOPPED 

----
## SERVER DATABASE
'ID': 
    games: {'game':'permission'},
    running: {'game':'isrunning'}