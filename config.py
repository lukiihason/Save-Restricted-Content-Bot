#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
  
#Your API HASH from my.telegram.org    
    API_ID = int(os.environ.get("API_ID", "1945966"))
#Your API HASH from my.telegram.org      
    API_HASH = os.environ.get("API_HASH", "6b73197f50512e26f5ebd42e73c3315f")
#BOT TOKEN: @Botfather on telegram    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740014121:AAFEF_Jpj0k_rzljg4oImLrdH9BCLgRl_D4")
#Public channel username without '@'. Don't forget to add bot in channel as administrator.    
    FORCESUB = os.environ.get("FORCESUB", "after_ever_happy_end") 
#Owner user id   
    AUTH  = os.environ.get("OWNER_ID", "5143506371")
#Pyrogram string session using (https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1)
    SESSION = os.environ.get("SESSION", "AQA5aXqC5nSWIQHtNn0wDfBO1fz6pyxNHTEh2AHVSYPB_SzoEO0miF_4naTMruoVM3fnmX_QwmSSR6UK_jr-au4Z923JEp-6qlYDOz0m6vDzwTzX3paHRVAiOg5yBFDII9MlDeLKIAg-CJPttolByprAPL3RBej7YPL5Ap3iJztKIqNNBPD4sjmWKwMfFDhUikFr_Bb4iqLMb5cESSb6eY0c9xRIulIRmVKYvFJjD5-cODh9jvhXKRWxC-afvua9kCZDsQpuf8W-emwUQTSHgZq4MRwPTHdsHJio08d9bmZ_quxB8VYekdug-1yBP6vjppCfiZnw8y8celMewDvBWzR5AAAAATKTrcMA")
  
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
