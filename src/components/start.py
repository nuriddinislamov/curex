from telegram import Update
from telegram.ext import CallbackContext
from utils.text import text
from .home import Home
from ..main import logger

home = Home()


class Starter():

    def start(self, update: Update, context: CallbackContext) -> None:
        """
        Send a message when the command /start is issued.
        """
        user = update.effective_user
        update.message.reply_html(
            f"Hi <b>{user.id}</b>!",
        )
        logger.info(f"User {user.id} initiated '/start' command")

        return home.display(update, context)
