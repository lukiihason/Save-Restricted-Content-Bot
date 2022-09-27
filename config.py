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
    SESSION = os.environ.get("SESSION", "BQBR_9kJA0exmNqUbxMaqy972QYrn6-ltg_Pdt6DxSUskg2qHMn6gF-e3eIa_lGPQOTZU_lAaq4nZMARc39Oi_ISO_mkm_-Ldi2_ffdey9DKC-tUuzy4z2oBx5vkkdayLkf3E4aNemNt9LVxZLwGHWXv0b-L5J-oBDZQ-jCK-9xtpiMydRgEHYnDrVLjszMux7a7TEuat-kVQLLcnc4fPKFphkDxR7byMfJA-g-u8qmJ9_797Aaxck1JnAWqugB2L0Lu-ukDE91D1QAHdLpJIya4bX1LpkTJmdNUNo7xA-Pk9XdybmoaF_UOI6yxa-zUD0iJZTbgF6tIWBIvzzYuoqBhcdf4KQA")
  
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
