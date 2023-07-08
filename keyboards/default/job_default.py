from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db


def main_menu_default_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              row_width=2)
    btn = KeyboardButton(text="👥️ Ro'yxatdan o'tish")
    btn2 = KeyboardButton(text="📞 Bizning aloqa manzil")
    btn3 = KeyboardButton(text="💼  Bot haqida")
    rkm.add(btn, btn3, btn2)
    return rkm


def user_rkm() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="👥 Ro'yxatdan o'tgan foydalanuvchilar")
    rkm.add(button)
    return rkm



def cancel_():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='⬅️  Ortga qaytish 🟩')
    rkm.add(btn)
    return rkm


def cancel_back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='⬅️  Ortga qaytish')
    rkm.add(btn)
    return rkm


def citizen():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    for user in db.all_user():
        return rkm.add(f"{user.id}")


def ortga_qaytish():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text="⏪ ortga qaytish")
    rkm.add(btn)
    return rkm





