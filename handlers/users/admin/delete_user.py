from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.job_default import user_rkm
from keyboards.inline.job_inline import inline_user_button
from loader import dp, db
from states.job_state import DeleteUserState


@dp.message_handler(Text(equals="✅ orqaga qaytish"),  state="*")
async def get_cancel_back(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi !",
                         reply_markup=user_rkm())
    await state.finish()


@dp.message_handler(Text(equals="⏪ ortga qaytish"), state="*")
async def back_func(message:types.Message, state:FSMContext):
    await message.answer(text='Orqaga qaytish',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
                         reply_markup=inline_user_button())
    await state.finish()


@dp.message_handler(state=DeleteUserState.id)
async def delete_user(message:types.Message, state:FSMContext):
        try:
                user_id = int(message.text)
                user = db.get_user(id=user_id)
                if user:
                        db.delete_user(id=user_id)
                        await message.answer(text=" <b><i>Fuqaro muvaffaqiyatli ravishda o'chirildi </i></b>")
                        await message.answer_photo(
                           photo='https://www.atf.gov/sites/default/files/media/2015/08/people.jpg',
                           reply_markup=inline_user_button())
                        await state.finish()

                else:
                        await message.answer('Bu id ga ega fuqaro topilmadi')

        except ValueError:
                await message.answer("ID raqam bo'lsin")






