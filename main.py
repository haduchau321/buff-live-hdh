from fastapi import FastAPI
# import uvicorn
import buff_live



app = FastAPI()

@app.get('/get_data/cookies={cookies}')
async def home(cookies:str):
    b = buff_live.main_buff(cookies)
    out = b.get_data()
    return out

@app.get('/Buff/id_sy={id_sy}/id_post={id_post}/id_video={id_video}/cookies={cookies}')
async def buff(id_sy:str,id_post:str,id_video:str,cookies:str):
    print(id_sy,id_post,id_video,cookies)
    b = buff_live.main_buff(cookies)
    out = b.buff(id_sy,id_post,id_video)
    return out

# uvicorn.run(app)

#  {"id_sy":"AQE5yR7GMR_37vQ:AQFZ_gcVHE0wO-M","id_post":"22412"}