
import os
import time
import threading
from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT
from datetime import datetime

name = """
░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗
██╔══██╗████╗░██║██║████╗░████║██╔════╝
███████║██╔██╗██║██║██╔████╔██║█████╗░░
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░
██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝
"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.files_directory = "files"
        os.makedirs(self.files_directory, exist_ok=True)  # Create directory for files
        self.uploaded_files = {}  # Track uploaded files with timestamps

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.create_chat_invite_link(chat_id=FORCE_SUB_CHANNEL2, creates_join_request=True)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__, a)

    @Client.on_message(filters.command("upload") & filters.private)
    async def upload_file(self, client, message):
        if message.reply_to_message and message.reply_to_message.document:
            file_name = message.reply_to_message.document.file_name
            file_path = os.path.join(self.files_directory, file_name)

            await message.reply_to_message.download(file_path)
            await message.reply(f"File '{file_name}' uploaded successfully!")

            # Track the uploaded file with the timestamp
            self.uploaded_files[file_name] = {
                "timestamp": time.time(),
                "user_id": message.from_user.id  # Track user ID for notifications
            }
            # Start a thread to notify user after 30 minutes
            threading.Thread(target=self.file_notification_timer, args=(file_name, message.from_user.id)).start()
        else:
            await message.reply("Please reply to a file to upload it.")

    def file_notification_timer(self, file_name, user_id):
        time.sleep(1800)  # Wait for 30 minutes (1800 seconds)
        if file_name in self.uploaded_files:
            # Notify user that the file is still in the directory
            self.send_message(user_id, f"⏳ The file '{file_name}' will be deleted in 5 minutes unless downloaded.")

            # Wait for an additional 5 minutes before deleting
            time.sleep(300)
            if file_name in self.uploaded_files:
                os.remove(os.path.join(self.files_directory, file_name))  # Delete the file
                del self.uploaded_files[file_name]  # Remove from tracking
                # Notify user about file deletion
                self.send_message(user_id, f"The file '{file_name}' has been deleted after 30 minutes.")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
