from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1256063269:AAHgWudeRj0hqJoSvW0sYm4egiETqVguDg4"
    APP_ID = 2554836
    API_HASH = "8e1ad7c819bf50241f9b71db624606c8"
    OWNER_ID = 1175834525
    AUTH_CHANNEL = [-1001417641550]
    DESTINATION_FOLDER = "Torrent-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token": "ya29.A0AfH6SMAo5aUFnWiwxm57xUOQOtgnI9FEjnBoIN7rqDtv_WGjdoRntNV_3SwErxIAQYy9M2DLw4Zoukok8eZndsiCcIpmWf8YDwpSwAd5t8JJpIS-JVtxId_3M6wPEpicFpSJl1fL9CmAEmotfbwOSXrJTWpfccBos1u-OREEEiU":"Bearer","refresh_token":"1//0dTrR4aPfQoQ1CgYIARAAGA0SNwF-L9Ir1XG1FlQhjCenZu0xhM3aYyA8IFi2eiRMU722oxnQWR7-KTm_qrZWbcv9fEOqM9WdQFw","expiry":"2020-11-13T15:58:12Z"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
