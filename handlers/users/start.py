from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.job_default import user_rkm, main_menu_default_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id == 6122889250:
        await message.answer(text=f"Admin xush kelibsiz !",
                             reply_markup=user_rkm())

    else:
        await message.answer(f"Salom, {message.from_user.full_name}!",
                             reply_markup=main_menu_default_button())



