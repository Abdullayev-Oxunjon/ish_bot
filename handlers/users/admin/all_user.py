from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.job_default import cancel_back
from keyboards.inline.job_inline import inline_user_button, show_users
from loader import dp, db
from states.job_state import ShowAllUserState


@dp.message_handler(Text(equals='⬅️  Ortga qaytish'), state='*')
async def func_cancel(message: types.Message, state: FSMContext):
    await message.answer(text = "orqaga qaytish",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo='https://www.atf.gov/sites/default/files/media/2015/08/people.jpg',
                                reply_markup=inline_user_button())
    await state.finish()




@dp.callback_query_handler(state=ShowAllUserState.id)
async def all_user(callback:types.CallbackQuery, state: FSMContext):
        user_id = callback.data
        user = db.get_user(id=user_id)
        if callback.data != "back":
            if user:

                await callback.message.answer(text=
                f"🧾 <b>Fuqaroning ism familyasi : {user[1]}\n\n"
                f"✅ Fuqaroning yoshi  : {user[2]}\n\n"
                f"📞 Fuqaroning telefon raqami : {user[3]}\n\n"
                f"🌍 Fuqaroning turar joy manzili  : {user[4]}\n\n"
                f"💼  Fuqaroning kasbi  : {user[5]}</b>",
                reply_markup=cancel_back())
              
                await state.finish()

        elif callback.data == "back":
            await callback.message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
                                    reply_markup=inline_user_button())
            await state.finish()









