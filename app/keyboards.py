from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove)

main = ReplyKeyboardMarkup(one_time_keyboard=True,
                           keyboard=[[KeyboardButton(text='Оглавление')],
                                     [KeyboardButton(text="Контакты")],
                                     [KeyboardButton(text="O нас")],
                                     [KeyboardButton(text="Помощь с выбором")],
                                     [KeyboardButton(text="/Регистрация")],
                                     [KeyboardButton(text="/start")]
                                     ], resize_keyboard=True,
                           input_field_placeholder="Выберите пункт меню...")
catalog_complexity = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True,
                                          inline_keyboard=[[InlineKeyboardButton(text="Очень легко",
                                                                                 callback_data='oveasy')],
                                                           [InlineKeyboardButton(text="Легко",
                                                                                 callback_data='easy')],
                                                           [InlineKeyboardButton(text="Нормально",
                                                                                 callback_data='normal')],
                                                           [InlineKeyboardButton(text="Сложно",
                                                                                 callback_data='hard')]],
                                          resize_keyboard=True)
catalog2 = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True,
                                inline_keyboard=[[InlineKeyboardButton(text="Астрономия",
                                                                       callback_data='subject_astr')],
                                                 [InlineKeyboardButton(text="Франц. язык",
                                                                       callback_data='subject_franch')],
                                                 [InlineKeyboardButton(text="Химия",
                                                                       callback_data='subject_him')],
                                                 [InlineKeyboardButton(text="Русск. язык",
                                                                       callback_data='subject_rus')],
                                                 [InlineKeyboardButton(text="Экология",
                                                                       callback_data='subject_ekol')],
                                                 [InlineKeyboardButton(text="Право",
                                                                       callback_data='subject_prav')],
                                                 [InlineKeyboardButton(text="География",
                                                                       callback_data='subject_geog')],
                                                 [InlineKeyboardButton(text="Математика",
                                                                       callback_data='subject_mat')],
                                                 [InlineKeyboardButton(text="Общество",
                                                                       callback_data='subject_com')],
                                                 [InlineKeyboardButton(text="Литература",
                                                                       callback_data='subject_lit')],
                                                 [InlineKeyboardButton(text="Экономика",
                                                                       callback_data='subject_ekon')],
                                                 [InlineKeyboardButton(text="Физика",
                                                                       callback_data='subject_fis')],
                                                 [InlineKeyboardButton(text="Англ. яз",
                                                                       callback_data='subject_inaz')],
                                                 [InlineKeyboardButton(text="ОБЖ",
                                                                       callback_data='subject_obz')],
                                                 [InlineKeyboardButton(text="История",
                                                                       callback_data='subject_hist')],
                                                 [InlineKeyboardButton(text="Информатика",
                                                                       callback_data='subject_info')],
                                                 [InlineKeyboardButton(text="Биология",
                                                                       callback_data='subject_biolog')],
                                                 [InlineKeyboardButton(text="МХК",
                                                                       callback_data='subject_mhk')],
                                                 [InlineKeyboardButton(text="Физ-ра",
                                                                       callback_data='subject_fisra')],

                                                 ], resize_keyboard=True)
sub_him = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projecthim1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projecthim2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projecthim3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projecthim4')]
                                                ])
sub_astra = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                        callback_data='projectastra1')],
                                                  [InlineKeyboardButton(
                                                      text="project2",
                                                      callback_data='projectastra2')],
                                                  [InlineKeyboardButton(text="project3",
                                                                        callback_data='projectastra3')],
                                                  [InlineKeyboardButton(text="project4",
                                                                        callback_data='projectastra4')]
                                                  ])
sub_franch = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                         callback_data='projectfranch1')],
                                                   [InlineKeyboardButton(
                                                       text="project2",
                                                       callback_data='projectfranch2')],
                                                   [InlineKeyboardButton(text="project3",
                                                                         callback_data='projectfranch3')],
                                                   [InlineKeyboardButton(text="project4",
                                                                         callback_data='projectfranch')]
                                                   ])
sub_rus = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectrus1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectrus2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectrus3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectrus4')]
                                                ])
sub_ekol = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                       callback_data='projectekol1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projectekol2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectekol3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectekol4')]
                                                 ])
sub_fis = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectfis1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectfis2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectfis3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectfis4')]
                                                ])
sub_prav = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                       callback_data='projectprav1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projectprav2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectprav3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectprav4')]
                                                 ])
sub_geog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                       callback_data='projectgeog1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projectgeog2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectgeog3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectgeog4')]
                                                 ])
sub_mat = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectmat1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectmat2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectmat3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectmat4')]
                                                ])
sub_com = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Долгосрочно прогнозирование моды",
                                                                      callback_data='projectcom1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectcom2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectcom3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectcom4')]
                                                ])
sub_lit = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectlit1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectlit2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectlit3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectlit4')]
                                                ])
sub_ekon = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                       callback_data='projectekon1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projectekon2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectekon3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectekon4')]
                                                 ])
sub_inaz = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                       callback_data='projectinaz1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projectinaz2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectinaz3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectinaz4')]
                                                 ])
sub_obz = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectobz1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectobz')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectobz3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectobz4')]
                                                ])
sub_hist = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Николай II: Портрет на фоне эпохи",
                                                                       callback_data='projecthist1')],
                                                 [InlineKeyboardButton(
                                                     text="project2",
                                                     callback_data='projecthist2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projecthist3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projecthist4')]
                                                 ])
sub_info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Создание сайта для игр",
                                                                       callback_data='projectinfo1')],
                                                 [InlineKeyboardButton(
                                                     text="projectinfo2",
                                                     callback_data='project2')],
                                                 [InlineKeyboardButton(text="project3",
                                                                       callback_data='projectinfo3')],
                                                 [InlineKeyboardButton(text="project4",
                                                                       callback_data='projectinfo4')]
                                                 ])
sub_biolog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                         callback_data='projectbiolog1')],
                                                   [InlineKeyboardButton(
                                                       text="project2",
                                                       callback_data='projectbiolog2')],
                                                   [InlineKeyboardButton(text="project3",
                                                                         callback_data='projectbiolog3')],
                                                   [InlineKeyboardButton(text="project4",
                                                                         callback_data='projectbiolog4')]
                                                   ])
sub_mhk = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="project1",
                                                                      callback_data='projectmhk1')],
                                                [InlineKeyboardButton(
                                                    text="project2",
                                                    callback_data='projectmhk2')],
                                                [InlineKeyboardButton(text="project3",
                                                                      callback_data='projectmhk3')],
                                                [InlineKeyboardButton(text="project4",
                                                                      callback_data='projectmhk4')]
                                                ])
sub_fisra = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Особенности специальной подготовки в футболе",
                                           callback_data='projectfisra1')],
                     [InlineKeyboardButton(
                         text="project2",
                         callback_data='projectfisra2')],
                     [InlineKeyboardButton(text="project3",
                                           callback_data='projectfisra3')],
                     [InlineKeyboardButton(text="project4",
                                           callback_data='projectfisra4')]
                     ])
