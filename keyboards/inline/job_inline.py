from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db


def works_inline_button():
    rkm = InlineKeyboardMarkup(row_width=2)
    btn2 = InlineKeyboardButton(text ='🚗  Xaydovchi  ',callback_data='driver')
    btn3 = InlineKeyboardButton(text ="👨‍🏫  O'qituvchi  ",callback_data="teacher")
    btn4 = InlineKeyboardButton(text ="👨‍🌾  Bog'bon  ",callback_data="bo'g'bon")
    btn5 = InlineKeyboardButton(text ="👩‍💼  Enaga  ",callback_data='enaga')
    btn6= InlineKeyboardButton(text ="👩‍🦰  Farrosh  ",callback_data='farrosh')
    btn7 = InlineKeyboardButton(text ="👷  Quruvchi  ",callback_data='quruvchi')
    btn8 = InlineKeyboardButton(text ="👨‍💼  Bugalter  ",callback_data='bugalter')
    btn9 = InlineKeyboardButton(text ="🏗️  Arxetektor  ",callback_data='arxetektor')
    btn10 = InlineKeyboardButton(text ="👨‍💼  Bank sohasi  ",callback_data='bank sohasi')
    btn11 = InlineKeyboardButton(text ="👩‍⚕  Hamshira  ",callback_data='hamshira')
    rkm.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    return rkm


def driver_category():
    rkm = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton(text='A - toifadagi haydovchi' , callback_data='A - toifadagi haydovchi')
    btn2 = InlineKeyboardButton(text='B - toifagi haydovchi' , callback_data='B - toifagi haydovchi')
    btn3 = InlineKeyboardButton(text='C - toifadagi haydovchi' , callback_data='C - toifadagi haydovchi')
    btn4 = InlineKeyboardButton(text='D - toifadagi haydovchi' , callback_data='D - toifadagi haydovchi')
    btn5 = InlineKeyboardButton(text='BE - toifadagi haydovchi' , callback_data='BE - toifadagi haydovchi')
    btn6 = InlineKeyboardButton(text='CE - toifadagi haydovchi' , callback_data='CE - toifadagi haydovchi')
    btn7 = InlineKeyboardButton(text='DE - toifadagi haydovchi' , callback_data='DE - toifadagi haydovchi')
    btn8 = InlineKeyboardButton(text="💼  Ortga qaytish",callback_data='cancel_jobs')
    rkm.add(btn,btn2, btn3, btn4, btn5,btn6, btn7,btn8)
    return rkm


def teacher_category():
    rkm = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardMarkup(text='Oliy Magistr', callback_data="O'qituvchi - oliy magistr")
    btn2 = InlineKeyboardMarkup(text='Magistr', callback_data="O'qituvchi - magistr")
    btn3 = InlineKeyboardMarkup(text="To'liq Oliy",callback_data="O'qituvchi - to'liq oliy")
    btn4 = InlineKeyboardMarkup(text="O'rta Maxsus", callback_data="O'qituvchi - orta maxsus")
    btn5 = InlineKeyboardButton(text="💼   Kasblar ro'yxatiga qaytish",callback_data='cancel_jobs')
    rkm.add(btn, btn2, btn3, btn4,btn5)
    return rkm


def inline_user_button():
    ikm = InlineKeyboardMarkup(row_width=1)
    button2 = InlineKeyboardButton(text="✅ Ro'yxatdan o'tgan foydalanuvchilar", callback_data="all_user")
    button4 = InlineKeyboardButton(text="✅ Ro'yxatdan biror bir fuqaroni o'chirish", callback_data="delete_user")
    button5 = InlineKeyboardButton(text="✅ Ortga qaytish", callback_data="cancel")
    ikm.add(button2,button4,   button5)
    return ikm


def show_users():
    ikm = InlineKeyboardMarkup(row_width=2)
    for i in db.all_user():
        button = InlineKeyboardButton(text=f"{i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    button1= InlineKeyboardButton(text="⬅️ Orqaga qaytish",
                                  callback_data="back")
    ikm.add(button1)
    return ikm


def delete_user_button():
    ikm = InlineKeyboardMarkup()
    for i in db.all_user():
        button = InlineKeyboardButton(text=f"ID : {i[0]}                      Ismi : {i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    return ikm


