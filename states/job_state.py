from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    address = State()
    job = State()
    confirm = State()


class DeleteUserState(StatesGroup):
    id = State()


class GetUserState(StatesGroup):
    id = State()


class ShowAllUserState(StatesGroup):
    id=State()


class Admin(StatesGroup):
    id = State()





