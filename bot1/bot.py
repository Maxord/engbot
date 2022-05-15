import logging
from test import *
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5340919234:AAGk24VPKHYHtXjuydBxhQ8oDjt5NqxeCtM"
verbal = "First, let’s make sure you now some English reading. Read the words taken from the text for aural comprehension that you are going to listen in to later. Pay attention to the stressed vowel sound.\n\nRead the first line aloud, check the transcription of the words you don’t know.\n\n-camera, back, challenge, happening, actual, battery, capture, sample, `navigate"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    greetbtn = types.ReplyKeyboardMarkup()
    start_button_1 = types.KeyboardButton(text="Попробуем!")
    greetbtn.add(start_button_1)
    await message.answer(greetmsg, reply_markup=greetbtn)

@dp.message_handler(Text(equals="Попробуем!"))
async def lesson(message: types.Message):
    unscramble_answer_button = types.ReplyKeyboardMarkup()
    unscramble_answer_button.add(types.KeyboardButton(text="Показать ответ"))
    await message.reply(lessonmsg, reply_markup=unscramble_answer_button)
    await message.reply("Нажмите на кнопку чтобы продолжить")
    

@dp.message_handler(Text(equals="Показать ответ"))
async def unscramble(message: types.Message):
        engbtn = types.ReplyKeyboardMarkup()
        eng_button_1 = types.KeyboardButton(text="Ok, let's!")
        engbtn.add(eng_button_1)
        await message.reply("Тема урока - Reading and speaking about science")
        await message.reply("The lesson has begun, now we will speak English.",reply_markup=engbtn)

@dp.message_handler(Text(equals="Ok, let's!"))
async def lesson(message: types.Message):
    interestedbtn = types.ReplyKeyboardMarkup()
    interestedbtn.add(types.KeyboardButton(text="Cool, I’m interested"))
    await message.reply(aimmsg, reply_markup=interestedbtn)

@dp.message_handler(Text(equals="Cool, I’m interested"))
async def verbal1(message: types.Message):
    verbal_1 = types.ReplyKeyboardMarkup()
    verbal_1.add(types.KeyboardButton(text="Done"))
    await message.reply(text="First, let’s make sure you now some English reading. Read the words taken from the text for aural comprehension that you are going to listen in to later. Pay attention to the stressed vowel sound.\n\nRead the first line aloud, check the transcription of the words you don’t know.\n\n-camera, back, challenge, happening, actual, battery, capture, sample, `navigate", reply_markup=verbal_1)

@dp.message_handler(Text(equals="Done"))
async def verbal2(message: types.Message):
    verbal_2 = types.ReplyKeyboardMarkup()
    verbal_2.add(types.KeyboardButton(text="Done!"))
    await message.reply("Now, the second line. The words are grouped in pairs.\n\n- collect, letting, never, stressed, developed, experiment, second, said, very, reply_markup=verbal_1",reply_markup=verbal_2)

@dp.message_handler(Text(equals="Done!"))
async def skip_cont(message: types.Message):
    skip_or_cont = types.ReplyKeyboardMarkup()
    skip_or_cont.add(types.KeyboardButton(text="Done."))
    skip_or_cont.add(types.KeyboardButton(text="Continue"))
    await message.reply("Third line\n\n-lived – least, give – see, `insect – beetle, system – be, finished – seen\n\nYou can skip the second part of it if you will", reply_markup=skip_or_cont)

@dp.message_handler(Text(equals="Continue"))
async def verbal3(message: types.Message):
    verbal_3 = types.ReplyKeyboardMarkup()
    verbal_3.add(types.KeyboardButton(text="Go for it"))
    await message.reply("I see you're ready to learn)\n\nwanted – explore, on – before, from – re`cord, rocky – small\n\nOne more line left", reply_markup=verbal_3)

@dp.message_handler(Text(equals="Go for it"))
async def verbal4(message: types.Message):
    verbal_4 = types.ReplyKeyboardMarkup()
    verbal_4.add(types.KeyboardButton("Done."))
    await message.reply("I’ll be calling you Mr. Steadfast tin soldier\n\n-tiny – bug – last, excited – enough – after, light – us – hard", reply_markup=verbal_4)

@dp.message_handler(Text(equals="Done."))
async def part2(message: types.Message):
    check = types.ReplyKeyboardMarkup() 
    check.add(types.KeyboardButton("Let's check"))
    await message.reply("Match the following synonyms (the words are taken from the text).",reply_markup=check)
    # Print out an image with an excercise here ->

@dp.message_handler(Text(equals="Let's check"))
async def goon(message:types.Message):
    goon = types.ReplyKeyboardMarkup()
    goon.add(types.KeyboardButton(text="Sure"))
    # Print out an image with answers here ->
    await message.reply("Well done!\n\nReady to go on?",reply_markup=goon)

@dp.message_handler(Text(equals="Sure"))
async def vocab(message:types.Message):
    vocab = types.ReplyKeyboardMarkup()
    vocab.add(types.KeyboardButton(text="Ready"))
    await message.reply("You performed well with the words. Now, look through the given vocabulary (the words are taken from the text you are going to listen in to) and do the matching.", reply_markup=vocab)
    # Print out an image with an excercise here ->

@dp.message_handler(Text(equals="Ready"))
async def checkvocab(message:types.Message):
    check_vocab = types.ReplyKeyboardMarkup()
    check_vocab.add(types.KeyboardButton(text="Next"))
    # Print out an image with anwers here ->
    await message.reply("Now you’ll listen to the text. The task is to mark the statements below true (T), false (F), not stated (NS).\n\nSay “Ready” to the task and hear the recording.\n\nYou have 20 seconds to read the task", reply_markup=check_vocab)

@dp.message_handler(Text(equals="Next"))
async def audio(message:types.Message):
    audio = types.ReplyKeyboardMarkup()
    audio.add(types.KeyboardButton(text="Check"))
    await message.reply("Check answers when you are ready", reply_markup=audio)
    # Print out an image with answer field here ->

@dp.message_handler(Text(equals="Check"))
async def checkaudio(message:types.Message):
    check_audio = types.ReplyKeyboardMarkup()
    check_audio.add(types.KeyboardButton(text="Ok"))
    # Print out an image with  here
    await message.reply("Listen to the text again and be ready choose the right option for the text.", reply_markup=check_audio)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)