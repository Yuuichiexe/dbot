from typing import Optional

from telegram import Message, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters
from telegram.utils.helpers import escape_markdown

import DazaiRobot.modules.sql.rules_sql as sql
from DazaiRobot import dispatcher
from DazaiRobot.modules.helper_funcs.alternate import typing_action
from DazaiRobot.modules.helper_funcs.chat_status import user_admin
from DazaiRobot.modules.helper_funcs.string_handling import markdown_parser


@typing_action
def get_rules(update, context):
    chat_id = update.effective_chat.id
    send_rules(update, chat_id)


# Do not async - not from a handler
def send_rules(update, chat_id, from_pm=False):
    bot = dispatcher.bot
    user = update.effective_user  # type: Optional[User]
    try:
        chat = bot.get_chat(chat_id)
    except BadRequest as excp:
        if excp.message != "Chat not found" or not from_pm:
            raise

        bot.send_message(
            user.id,
            "The rules shortcut for this chat hasn't been set properly! Ask admins to "
            "fix this.",
        )
        return
    rules = sql.get_rules(chat_id)
    text = "The rules for *{}* are:\n\n{}".format(escape_markdown(chat.title), rules)

    if from_pm and rules:
        bot.send_message(user.id, text, parse_mode=ParseMode.MARKDOWN)
    elif from_pm:
        bot.send_message(
            user.id,
            "The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!",
        )
    elif rules:
        update.effective_message.reply_text(
            "𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗅𝗂𝖼𝗄 𝗍𝗁𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗌𝖾𝖾 𝗍𝗁𝖾 𝗋𝗎𝗅𝖾𝗌.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝖱𝗎𝗅𝖾𝗌 📑",
                            url=f"t.me/{bot.username}?start={chat_id}",
                        ),
                        InlineKeyboardButton(text="𝖣𝖾𝗅𝖾𝗍𝖾 ❌", callback_data="close"),
                    ]
                ]
            ),
        )
    elif rules:
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝖱𝗎𝗅𝖾𝗌 📑",
                        url=f"t.me/{bot.username}?start={chat_id}",
                    ),
                    InlineKeyboardButton(text="𝖣𝖾𝗅𝖾𝗍𝖾 ❌", callback_data="close"),
                ]
            ]
        )
        txt = "𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗅𝗂𝖼𝗄 𝗍𝗁𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗌𝖾𝖾 𝗍𝗁𝖾 𝗋𝗎𝗅𝖾𝗌."
        if not message.reply_to_message:
            message.reply_text(txt, reply_markup=btn)

        if message.reply_to_message:
            message.reply_to_message.reply_text(txt, reply_markup=btn)
    else:
        update.effective_message.reply_text(
            "The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!"
        )


@user_admin
@typing_action
def set_rules(update, context):
    chat_id = update.effective_chat.id
    msg = update.effective_message  # type: Optional[Message]
    raw_text = msg.text
    args = raw_text.split(None, 1)  # use python's maxsplit to separate cmd and args
    if len(args) == 2:
        txt = args[1]
        offset = len(txt) - len(raw_text)  # set correct offset relative to command
        markdown_rules = markdown_parser(
            txt, entities=msg.parse_entities(), offset=offset
        )

        sql.set_rules(chat_id, markdown_rules)
        update.effective_message.reply_text("Successfully set rules for this group.")


@user_admin
@typing_action
def clear_rules(update, context):
    chat_id = update.effective_chat.id
    sql.set_rules(chat_id, "")
    update.effective_message.reply_text("Successfully cleared rules!")


def __stats__():
    return "× {} chats have rules set.".format(sql.num_chats())


def __import_data__(chat_id, data):
    # set chat rules
    rules = data.get("info", {}).get("rules", "")
    sql.set_rules(chat_id, rules)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    return "This chat has had it's rules set: `{}`".format(bool(sql.get_rules(chat_id)))


__help__ = """
Every chat works with different rules; this module will help make those rules clearer!

➛ /rules: get the rules for this chat.

*Admin only:*
➛ /setrules <your rules here>: Sets rules for the chat.
➛ /clearrules: Clears saved rules for the chat.
"""

__mod_name__ = "𝚁ᴜʟᴇs"

GET_RULES_HANDLER = CommandHandler(
    "rules", get_rules, filters=Filters.chat_type.groups, run_async=True
)
SET_RULES_HANDLER = CommandHandler(
    "setrules", set_rules, filters=Filters.chat_type.groups, run_async=True
)
RESET_RULES_HANDLER = CommandHandler(
    "clearrules", clear_rules, filters=Filters.chat_type.groups, run_async=True
)

dispatcher.add_handler(GET_RULES_HANDLER)
dispatcher.add_handler(SET_RULES_HANDLER)
dispatcher.add_handler(RESET_RULES_HANDLER)
