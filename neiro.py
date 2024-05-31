import requests
from aiogram import Bot, Dispatcher, types, executor


TELEGRAM_TOKEN = '7472572194:AAE6yB63ltbkT1FFjp2t7QWNo5-ynCsAwd8'
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
API_KEY = 'AQVNxnZzc6oh7wYQWT05IWj2wEfjAAXmUcttuq44'

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("Аллеу")

async def get_response(message_text):
    prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 1,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты - нейросеть, помогающая улучшить промт. Исправь сообщение, написанное пользователем, в одно единственное предложение."
        },
        {
            "role": "user",
            "text": message_text
        }
    ]
}



    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    print(response)
    result = response.json()
    print(result)
    return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
    response_text = await get_response((message.text))
    await message.answer(response_text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)