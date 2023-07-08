from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.job_default import cancel_
from loader import dp
from states.job_state import AddUserState


@dp.message_handler(Text(equals="📞 Bizning aloqa manzil"))
async def phone_address(message:types.Message):
    await message.answer_photo(photo='https://img.freepik.com/free-photo/colleagues-working-together-call-center-with-headphones_23-2149256084.jpg',
                               caption="✅   Biz bilan bog'lanish uchun "
                                       "quyidagi raqamlarga quyidagi raqamlarga qo'ng'iroq qiling ! \n\n"
                                       ""
                                       "Telefon raqam : <b><em> +998912210506</em></b>")


@dp.message_handler(Text(equals="💼  Bot haqida"))
async def phone_address(message:types.Message):
    await message.answer_photo(photo='https://st2.depositphotos.com/3643473/6206/i/600/depositphotos_62060317-stock-photo-person-with-megaphone-and-word.jpg',
                               caption="✅ Agar sizda yaxshi daromad qilish,  yaxshi "
                                       "oylik olishni, yaxshi sharoitda  ishlashni"
                                       " xohlasangiz bu ish o’rinlarimiz  aynan siz uchun !\n\n✅ Bizga o'ziga ishongan ,Agar o'zingizni "
                                       "shunga loyiq xodim deb o'ylasangiz biz bilan bog'laning o'z ishining ustasi , karyerali"
                                       " o'sish qilaman degan xodim kerak.")


@dp.message_handler(Text(equals="👥️ Ro'yxatdan o'tish"))
async def phone_address(message:types.Message):
    await message.answer(text="🔹 Ro'yxatdan o'tish",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="<b><em>Ism familyangizni kiriting  </em></b>",
                         reply_markup=cancel_())
    await AddUserState.name.set()





