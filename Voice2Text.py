from pyrogram import Client, filters, enums
import asyncio
import time
import os
import whisper

api_id = 
api_hash = ""

app = Client("Voice2Text", api_id=api_id, api_hash=api_hash)
model = whisper.load_model("base")

def remove_file(voice_file):
    os.remove(voice_file)

def voice_to_text(voice_file, i=0):
    if i == 5:
        return False
    try:
        result = model.transcribe(
            voice_file,
            fp16=False,
            language='Portuguese'
        )['text']
    except:
        time.sleep(3)
        result = voice_to_text(voice_file, i+1)
    return result

def download_voice(message):
    return app.download_media(message)

def edit_message(client, msg, message, transcription):
    text = (
        f'<b>🎙 Transcrição automática:</b>'
        f'\n<i>{transcription}</i>'
    )
    client.edit_message_text(
        chat_id=message.chat.id,
        message_id=msg.id,
        text=text,
        parse_mode=enums.ParseMode.HTML
    )

def send_message(client, message):
    msg = app.send_message(
        chat_id=message.chat.id,
        text='📝 Transcrição iniciada...',
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=message.id
    )
    return msg

def delete_message(client, msg):
    app.delete_messages(
        chat_id=msg.chat.id,
        message_ids=msg.id
    )

@app.on_message(filters.private & (filters.voice | filters.video_note))
def receive_voice(client, message):
    msg = send_message(client, message)
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    voice_file = download_voice(message)
    transcription = voice_to_text(voice_file)
    if not transcription:
        delete_message(client, msg)
        return
    print(f'{message.chat.id} disse: {transcription}')
    edit_message(client, msg, message, transcription)
    remove_file(voice_file)

app.run()
