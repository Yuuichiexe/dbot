from io import BytesIO
from pyrogram import Client, filters

from . import async_searcher, LOGS


@Client.on_message(filters.command("gpt2", prefixes="."))
async def chatgpt2(client, message):
    query = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None
    reply = message.reply_to_message

    if not query:
        if reply and reply.text:
            query = reply.text
        else:
            await message.reply("Gimme a Question to ask from ChatGPT")
            return

    eris = await message.reply("Generating answer...")
    payloads = {
        "message": query,
        "chat_mode": "assistant",
        "dialog_messages": "[{'bot': '', 'user': ''}]"
    }
    
    try:
        response = await async_searcher(
            "https://api.safone.me/chatgpt",
            post=True,
            json=payloads,
            re_json=True,
            headers={"Content-Type": "application/json"},
        )
        if not (response and "message" in response):
            LOGS.error(response)
            raise ValueError("Invalid Response from Server")

        response = response.get("message")
        if len(response + query) < 4080:
            to_edit = (
                f"<b>Query:</b>\n~ <i>{query}</i>\n\n<b>ChatGPT:</b>\n~ <i>{response}</i>"
            )
            await eris.edit(to_edit, parse_mode="html")
        else:
            with BytesIO(response.encode()) as file:
                file.name = "gpt_response.txt"
                await message.reply_document(
                    document=file,
                    caption=f"{query[:1020]}",
                    reply_to_message_id=message.reply_to_message.message_id if reply else None,
                )
            await eris.delete()
    except Exception as exc:
        LOGS.exception(exc)
        await eris.edit(f"Ran into an Error: \n{exc}")