import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.job_default import main_menu_default_button
from keyboards.inline.job_inline import works_inline_button, teacher_category, driver_category
from loader import dp, bot, db
from states.job_state import AddUserState


@dp.message_handler(Text(equals='⬅️  Ortga qaytish 🟩'), state="*")
async def ortga(message:types.Message,state:FSMContext):
    await message.answer(text="orqaga qaytish",
                         reply_markup=main_menu_default_button())
    await state.finish()


@dp.message_handler(state=AddUserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_text =message.text
        NAME = re.match(r'^[a-zA-Z\s.,?!\'"]*$', user_text)
        if NAME:
            data['name'] = message.text
            await message.answer(text="<b><em>✅ Yoshingizni kiriting</em></b>")
            await AddUserState.next()
        else:
            await message.answer(text="<b>Ismni familyani  kiritishda xatolik bor</b>")


@dp.message_handler(state=AddUserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
            await message.answer(text="<b><em>📞 Telefon raqamingizni kiriting</em></b>")
            await AddUserState.next()

        except ValueError:
            await message.answer("<b><em>✅ Yosh butun son bo'lsin</em></b>")


@dp.message_handler(state=AddUserState.phone_number)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data['phone_number'] = message.text

            await AddUserState.next()
            await message.answer("<b><em>🏠 Yashash turar-joy manzilingingizni kiriting</em></b>")
        else:
            await message.answer("<b>Telefon raqam xato kiritildi</b>")


@dp.message_handler(state=AddUserState.address)
async def add_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer(text='<b><em>💼 Qaysi kasbni tanlamoqchisiz ?</em></b>')
    await message.answer_photo(photo='https://alum.kuleuven.be/img/fotos/pointofsale-jobs.jpg/image',
                               reply_markup=works_inline_button())
    await AddUserState.next()


@dp.callback_query_handler(state=AddUserState.job)
async def add_job(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:

        if callback.data == 'driver':
            await callback.message.answer_photo(
                photo="https://freedesignfile.com/upload/2020/10/Taxi-driver-cartoon-vector.jpg",
                caption='💁‍♂️ Qaysi toifadagi haydovchisiz ?', reply_markup=driver_category())

        elif callback.data == 'teacher':
            await callback.message.answer_photo(
                photo="https://images.assetsdelivery.com/compings_v2/microone/microone1808/microone180800029.jpg",
                reply_markup=teacher_category())                                                                                        

        elif callback.data == 'cancel_jobs':
            await callback.message.answer_photo(
                photo="https://alum.kuleuven.be/img/fotos/pointofsale-jobs.jpg/image",
                reply_markup=works_inline_button())

        elif callback.data:
            data['job'] = callback.data

            await bot.send_message(chat_id=ADMINS[0],
                                   text=f"Ushbu foydalanuvchi {data['name']} ro'yhatdan o'tdi !\n"
                                   )

            await bot.send_photo(chat_id=callback.message.chat.id,
                                 photo="https://w7.pngwing.com/pngs/627/693/png-transparent-computer-icons-user-user-icon.png",
                                 caption=f"🧾 <b>  Fuqaroning ismi  : {data['name']}\n\n"
                                         f"✅   Fuqaroning yoshi  :  {data['age']}\n\n"
                                         f"📞   Fuqaroning telefon raqami: {data['phone_number']}\n\n"
                                         f"🌍   Fuqaroning turar joy manzili  : {data['address']}\n\n"
                                         f"💼   Fuqaroning kasbi  : {data['job']}</b>",
                                 reply_markup=ReplyKeyboardRemove())

            db.add_user(name=data['name'],
                        age=data['age'],
                        phone_number=data['phone_number'],
                        address=data['address'],
                        job=data['job'])

            await callback.message.answer(text="<b><em>🔹 Ma'lumotlaringiz saqlandi !   "
                                               "Bizning xizmatlarimizda foydalanish uchun "
                                               "4️⃣0️⃣ ming so'm to'lov qilishing kerak . Tez orada siz bilan "
                                               "aloqaga chiqamiz xurmatli foydalanuvchi !\n\n"
                                               "Bizning click raqam : 9860 3501 0373 4371</em></b>",
                                          reply_markup=main_menu_default_button())
            await state.finish()











        


























