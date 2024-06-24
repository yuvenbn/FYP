from poe_api_wrapper import AsyncPoeApi, PoeApi
import asyncio
from .configurations import API_TOKENS

tokens = API_TOKENS

async def translate_text(source_text, source_language, target_language):
    client = await AsyncPoeApi(cookie=tokens).create()
    message = f"Translate \"{source_text}\" from {source_language} to {target_language}.Your response should only be the translated text."
    
    translated_text = ""
    async for chunk in client.send_message(bot="gpt3_5", message=message):
        translated_text += chunk["response"]

    return translated_text
