# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "24817837")
    API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7561380664:AAExB4yPbg2_TylrTu9PgezvKTbrfpnnmyQ") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Digital_Rename_Bot")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://iili.io/3cZ02kl.md.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7428552084').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002376378205"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = False 
    PREMIUM_MODE = False 
    
    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "botzflix")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "kgcanime")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Yo, {}👋

Ceci est un bot de renommage avancé et puissant. En utilisant ce bot,\n\nVous pouvez renommer et changer la miniature de votre fichier. Vous pouvez également convertir des vidéos en fichiers et des fichiers en vidéos\n\nCE BOT SUPPORTE ÉGALEMENT DES MINIATURES ET CAPTIONS PERSONNALISÉES.

<blockquote>Ce bot a été créé par :  @BotZFlix 💞</blockquote></b>"""

    ABOUT_TXT = """<b>╭───────────⍟
<blockquote>├🤖 ᴍy ɴᴀᴍᴇ : {}</blockquote>
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href='t.me/Kingcey'>◡̈⃝ㅤ🇰ιηg¢єу</a>
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href='t.me/Kingcey'>◡̈⃝ㅤ🇰ιηg¢єу</a>
├📕 Lɪʙʀᴀʀy : <a href='t.me/pyrogram.org'>Pyrogram</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href='t.me/python.org'>Python3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href='t.me/BotZFlix'>CloudFare</a>
├📊 ᴠᴇʀsɪᴏɴ: 2V2.0</b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Démarrer le bot.

✏️ <b><u>COMMENT RENOMMER UN FICHIER ?</u></b>
<b>•></b> Envoyer une vidéo ou document et entrer le nouveau nom\nEt puis sélectionner le format [ document, video, audio ].           
Si tu as un problème, Contactez moi :- <a href=https://t.me/Kingcey>◡̈⃝ㅤ🇰ιηg¢єу</a>
"""

    UPGRADE_PREMIUM= """
•⪼ ★Plans - ⏳Date - 💸Prix  
•⪼ 🥉Bronze - 3 jours - 500f  
•⪼ 🥈Argent - 7 jours - 1000f  
•⪼ 🥇Or - 15 jours - 1500f  
•⪼ 🏆Platine - 1 mois - 2500f  
•⪼ 💎Diamant - 2 mois - 3000f  

- Limite de téléchargement quotidien illimitée  
- Remise sur tous les plans : En Dollars également 
    """
    
    UPGRADE_PLAN= """
Plan : Pro  
Date : 1 mois  
Prix : 1000f  
Limite : 100 Go  

Plan : Ultra Pro  
Date : 1 mois  
Prix : 1500f  
Limite : 1000 Go  

- Remise sur tous les plans : en dollars également
    """
    
    THUMBNAIL = """
<b><u>Comment définir une miniature</u></b>**

<b>•></b> Envoyez une photo pour définir automatiquement la miniature.  
<b>•></b> /del_thumb Utilisez cette commande pour supprimer votre ancienne miniature.  
<b>•></b> /view_thumb Utilisez cette commande pour voir votre miniature actuelle.
"""
    CAPTION= """
<b><u>Comment définir une légende personnalisée</u></b>**

<b>•></b> /set_caption - Utilisez cette commande pour définir une légende personnalisée.  
<b>•></b> /see_caption - Utilisez cette commande pour voir votre légende personnalisée.  
<b>•></b> /del_caption - Utilisez cette commande pour supprimer votre légende personnalisée.  

Exemple : `/set_caption 📕 Nom du fichier : {filename}  
💾 Taille : {filesize}  
⏰ Durée : {duration}`
"""
    BOT_STATUS = """
⚡️ STATUT DU BOT ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 Utilisateurs: `{}`
💸 Utilisateurs Premiums: `{}`
֍ Téléversé: `{}`
⊙ Télécharger: `{}`
"""
    LIVE_STATUS = """
⚡ STATUT DE VIE ⚡

Temps: `{}`
CPU: `{}%`
RAM: `{}%` 
DISQUE TOTAL: `{}`
Espace Utilisé: `{} {}%`
Espace Gratuit: `{}`
Téléversé: `{}`
Télécharger: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ DÉFINIR DES MÉTADONNÉES PERSONNALISÉES ❫

- /metadata - Pour définir et changer votre code de métadonnées.

☞ Par exemple : 

`--change-title @BotZFlix  
--change-video-title @BotZFlix  
--change-audio-title @BotZFlix  
--change-subtitle-title @BotZFlix  
--change-author @BotZFlix`

📥 Pour de l'aide, contactez @Kingcey
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋 Nom de fichier personnalisé</u>

Vous pouvez pré-ajouter un préfixe et un suffixe avec votre nouveau nom de fichier.

➢ /set_prefix - Pour ajouter un préfixe à votre _nom de fichier.  
➢ /see_prefix - Pour voir votre préfixe !!  
➢ /del_prefix - Pour supprimer votre préfixe !!  
➢ /set_suffix - Pour ajouter un suffixe à votre nom de fichier_.  
➢ /see_suffix - Pour voir votre suffixe !!  
➢ /del_suffix - Pour supprimer votre suffixe !!  

**Exemple :** <code>/set_suffix @BotZFlix</code>  
**Exemple :** <code>/set_prefix @BotZFlix</code>
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>⛔️⛔️⛔️MESSAGE URGENT‼️‼️‼️ </u>

Rejoignez Notre Groupe de film & de séries. Dans ce groupe, il faut juste écrire le nom du film ou de la série, pour le recevoir

<u>EXEMPLE:</u>

<code>Loki</code> 
<code>Warrior</code>
<code>Hulk</code>
<code>Squid Game</code>

En écrivant le nom, Un bot va vous l'envoyé. il faut et seulement écrire le nom du film.


<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>
<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>
<a href='t.me/ZFlixTeam'>Rejoindre le groupe</a>


pour tout Problème contactez moi : <a href='t.me/Kingcey'>◡̈⃝ㅤ🇰ιηg¢єу</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ DÉFINIR DES MÉTADONNÉES PERSONNALISÉES ❫

- /metadata - Pour définir et changer votre code de métadonnées.

☞ Par exemple : 

`--change-title @BotZFlix  
--change-video-title @BotZFlix  
--change-audio-title @BotZFlix  
--change-subtitle-title @BotZFlix  
--change-author @BotZFlix`

📥 Pour de l'aide, contactez @Kingcey
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰Processus en cours.......❱━➣  
┣⪼ 🗃 Taille : {1} | {2}  
┣⪼ ⏳ Fait : {0}%  
┣⪼ 🚀 Vitesse : {3}/s  
┣⪼ ⏰ ETA : {4}  
╰━━━━━━━━━━━━━━━➣ </b>"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
