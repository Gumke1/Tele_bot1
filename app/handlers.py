from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
from data import db_session
from data.users import User
import requests

router = Router()




class Register(StatesGroup):
    name = State()
    age = State()
    id_user = State()
    phone_user = State()
    where_from = State()
    where_to = State()



class ChoseProject(StatesGroup):
    subject = State()



@router.message(Command('wiki'))
async def wiki_search(message: types.Message):
    search_query = message.text.replace('/wiki ', '')
    response = requests.get(
        f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={search_query}")
    data = response.json()
    page_id = list(data['query']['pages'].keys())[0]
    extract = data['query']['pages'][page_id]['extract']

    await message.answer(extract)


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAKWQGYwoJnQtmM453xUE46hATztgheOAAKsEwACOJ4hS9HIZVrp3vjbNAQ")
    await message.answer("Привет", reply_markup=kb.main)
    await message.answer("Как дела?")


@router.message(Command('help'))
async def help_user(message: Message):
    await message.answer("Здесь должна быть инструкция, но я хочу спать так что вот так")


@router.message(F.text == "Помощь с выбором")
async def help_me(message: Message, state: FSMContext):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAKWQmYwp2n_Ikj1jh3joimUVWWsnUBmAALdEgACNwHBSlEqf3fiYXSYNAQ")
    await message.answer(f'Оценка своих интересов и анализ ресурсов')
    await message.answer('Начните с определения сфер, которые вас особенно интересуют. Это поможет выбрать прое'
                         'кт, который будет вам по душе и поддерживать мотивацию.')
    await message.answer('Проанализируйте, какими навыками, временем и средствами вы располагаете.'
                         ' Это важно, чтобы выбрать реалистичный и достижимый проект')
    await state.set_state(ChoseProject.subject)
    await message.answer('Введите ваше предмет')


@router.message(F.text == "Нормально")
async def help_me(message: Message, ):
    await message.answer("Нормально это не плохо, но нужно стремиться к лучшему.")


@router.message(F.text == "Хорошо")
async def help_me(message: Message, ):
    await message.answer("Рад за тебя.")


@router.message(F.text == "Плохо")
async def help_me(message: Message, ):
    await message.answer("Не печалься, воспользуйся ботом и подними настроение.")



@router.message(ChoseProject.subject)
async def reg_name(messange: Message, state: FSMContext):
    await state.update_data(subject=messange.text)
    await messange.answer('Оценка сложности')
    await messange.answer('Обратите внимание на сложность реализации проекта. Лучше начать с несложных,'
                          ' но интересных идей, чтобы набраться опыта.')
    await messange.answer("Выберите желаемою сложность предмета", reply_markup=kb.catalog_complexity)


@router.callback_query(F.data == "oveasy")
async def projeasy(callback: CallbackQuery):
    await callback.message.answer("В жизни слишком просто не бывает. Рекомендуем сказать что сломал ногу или"
                                  " ещё что-нибудь, по вашему запросу это лучший метод.")


@router.callback_query(F.data == "easy")
async def projeasy(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.answer('Изучение аналогов')
    await callback.message.answer('Ознакомтесь с примерами которые размещены у нас в боте,чтобы понять,'
                                  ' какие решения и подходы могут быть эффективными.')
    await callback.message.answer(f'Вы выбрали проект по предмету: {data["subject"]}\nВашa сложность: легкая')
    await callback.message.answer(f'Рекомендуем посмотреть 1-ый и 2-ой проекты по предмету {data["subject"]}')
    await state.clear()


@router.callback_query(F.data == "normal")
async def projeasy(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.answer('Изучение аналогов')
    await callback.message.answer('Ознакомтесь с примерами которые размещены у нас в боте,чтобы понять,'
                                  ' какие решения и подходы могут быть эффективными.')
    await callback.message.answer(f'Вы выбрали проект по предмету: {data["subject"]}\nВашa сложность: Нормальная')
    await callback.message.answer(f'Рекомендуем посмотреть 3-ий проект по предмету {data["subject"]}')
    await state.clear()


@router.callback_query(F.data == "hard")
async def projeasy(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.answer('Изучение аналогов')
    await callback.message.answer('Ознакомтесь с примерами которые размещены у нас в боте,чтобы понять,'
                                  ' какие решения и подходы могут быть эффективными.')
    await callback.message.answer(f'Вы выбрали проект по предмету: {data["subject"]}\nВашa сложность: Сложная')
    await callback.message.answer(
        f'Рекомендуем посмотреть 4-ый проект по предмету {data["subject"]}.\n'
        f'Также рекомендуем отдыхать, ведь выполнение сложных задач дело не простое')
    await state.clear()


@router.message(F.text == "Контакты")
async def catalog(messange: Message):
    await messange.answer("qqqqqqqqqqqqqqqqqq@gmail.com")


@router.message(F.text == "O нас")
async def catalog(messange: Message):
    await messange.answer(
        "Здравствуйте! Мы... хм, молодые разработчики. "
        "У нас есть много идей, но пока мы смогли сделать только этого бота."
        "Будем рады если он окажется полезным."
        "Если есть какие-то пожелания или вопросы пишите на почту.")
    await messange.answer_sticker(sticker="CAACAgIAAxkBAAKWRmYwp-mk8czWfr6Vq-LSdGCUrXMvAAISFQACmnfBSWitcLbp2lapNAQ")


@router.message(Command('Регистрация'))
async def reg(messange: Message, state: FSMContext):
    await messange.answer_sticker(sticker="CAACAgIAAxkBAAKWOmYwn7kros4v7IOjhT1V4kIxK-GFAAI-FQAC9QNBSQwAAWcZnwmGXTQE")
    await state.set_state(Register.name)
    await messange.answer('Введите ваше имя')


@router.message(Register.name)
async def reg_name(messange: Message, state: FSMContext):
    await state.update_data(name=messange.text)
    await state.set_state(Register.age)
    await messange.answer("Введите ваш возраст")


@router.message(Register.age)
async def reg_age(messange: Message, state: FSMContext):
    await state.update_data(age=messange.text)
    data = await state.get_data()
    db_session.global_init("db/blogs.db")
    na = data['name']
    ag = data['age']
    user = User()
    user.name = na
    user.hashed_password = ag
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    await messange.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}')
    await state.clear()


@router.message(F.text == "Оглавление")
async def catalog(messange: Message):
    await messange.answer_sticker(sticker="CAACAgIAAxkBAAKWSmYwqdBBiwcbW--t8LLFGMOkiCCwAAKRFwACG1DZSkYoQ3AhkU5KNAQ")
    await messange.answer("Выберите желаемый предмет", reply_markup=kb.catalog2)


@router.callback_query(F.data == "subject_him")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_him)


@router.callback_query(F.data == "subject_rus")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_rus)


@router.callback_query(F.data == "subject_astr")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_astra)


@router.callback_query(F.data == "subject_franch")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_franch)


@router.callback_query(F.data == "subject_ekol")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_ekol)


@router.callback_query(F.data == "subject_prav")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_prav)


@router.callback_query(F.data == "subject_geog")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_geog)


@router.callback_query(F.data == "subject_mat")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_mat)


@router.callback_query(F.data == "subject_com")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_com)


@router.callback_query(F.data == "subject_lit")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_lit)


@router.callback_query(F.data == "subject_ekon")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_ekon)


@router.callback_query(F.data == "subject_fis")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_fis)


@router.callback_query(F.data == "subject_inaz")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_inaz)


@router.callback_query(F.data == "subject_obz")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_obz)


@router.callback_query(F.data == "subject_hist")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_hist)


@router.callback_query(F.data == "subject_info")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_info)


@router.callback_query(F.data == "subject_biolog")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_biolog)


@router.callback_query(F.data == "subject_mhk")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_mhk)


@router.callback_query(F.data == "subject_fisra")
async def projecthim(callback: CallbackQuery):
    await callback.message.answer("Выберите желаемый проект", reply_markup=kb.sub_fisra)


@router.callback_query(F.data == "projectastra1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectastra2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectastra3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectastra4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projecthim1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projecthim2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projecthim3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projecthim4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfranch1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfranch2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfranch3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectfranch4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectrus1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectrus2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectrus3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectrus4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekol1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekol2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekol3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectekol4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfis1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfis2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfis3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectfis4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectprav1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectprav2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectprav3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectprav4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectgeog1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectgeog2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectgeog3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectgeog4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmat1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmat2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmat3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectmat4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectcom1")
async def project1(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали проект на тему: Долгосрочное прогнозирование моды")
    await callback.message.answer('https://disk.yandex.ru/i/MbFs-D0bEZ8fvg')


@router.callback_query(F.data == "projectcom2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectcom3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectcom4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectlit1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectlit2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectlit3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectlit4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekon1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekon2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectekon3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectekon4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectinaz1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectinaz2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectinaz3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectinaz4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectobz1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectobz2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectobz3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectobz4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projecthist1")
async def project1(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали проект на тему: Николай II на фоне эпохи")
    await callback.message.answer('https://disk.yandex.ru/i/DDeleJNDsWDkSw')


@router.callback_query(F.data == "projecthist2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projecthist3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projecthist4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectinfo1")
async def project1(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали проект на тему: создание сайта для игр")
    await callback.message.answer('https://disk.yandex.ru/i/uAIgx-fqCnWXBA')


@router.callback_query(F.data == "projectinfo2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectinfo3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectinfo4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectbiolog1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectbiolog2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectbiolog3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectbiolog4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmhk1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmhk2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectmhk3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectmhk4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfisra1")
async def project1(callback: CallbackQuery):
    await callback.message.answer('Вы выбрали проект: Особенности специальной подготовки в футболе')
    await callback.message.answer('https://disk.yandex.ru/i/4bKZ6QcgaLXsYQ')


@router.callback_query(F.data == "projectfisra2")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')


@router.callback_query(F.data == "projectfisra3")
async def project1(callback: CallbackQuery):
    await callback.message.answer("1")


@router.callback_query(F.data == "projectfisra4")
async def project1(callback: CallbackQuery):
    await callback.message.answer('1')
