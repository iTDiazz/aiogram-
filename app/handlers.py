from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello. "
                        f"\nYour ID: {message.from_user.id}. "
                        f"\nYour name: {message.from_user.first_name}")


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("It command /help")


@router.message(F.text == "1")
async def f_otvet(message: Message):
    await message.reply("2")


@router.message(Command("photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIF5WXTDh-wm8COfi8yslvk6S-qkHtYAAJL0zEbzoiYSnfYcWBABKwjAQADAgADeQADNAQ', caption="It supra")


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")
