from tkinter import *
from tkinter.filedialog import *
import requests


class Translator:

    def __init__(self, main):

        self.main = main

        self.KEY = 'trnsl.1.1.20180210T063150Z.887a84b1ad9e07eb.a4320e54acdfe84f353c1532a2d97186c7a6e50c'
        self.url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

        self.main_menu = Menu(main, bg='#9db7b2')
        main.configure(menu=self.main_menu, bg='#0f0e0e')
        first_menu_item = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='File',
                                   menu=first_menu_item)
        first_menu_item.add_command(label='Open',
                                    command=self.open_file)
        first_menu_item.add_command(label='Save translated text',
                                    command=self.save_file)
        first_menu_item.add_separator()
        first_menu_item.add_command(label='Exit',
                                    command=self.exit)


        self.lang = StringVar()
        self.translate_text_label = Label(text='Text for translate:',
                                          font='Ubuntu',
                                          bg='#0f0e0e',
                                          fg='#fcdbdb')
        self.translate_text = Text(width=75,
                                   height=20,
                                   bg='#a5a5a5')
        self.translate_lang = Label(text='Language of the text:',
                                    font='Ubuntu',
                                    bg='#0f0e0e',
                                    fg='#fcdbdb')
        self.lang_en_radio = Radiobutton(main,
                                         text='English',
                                         value='en',
                                         variable=self.lang,
                                         font='Ubuntu',
                                         bg='#0f0e0e',
                                         fg='#cecece',
                                         indicatoron=False,
                                         selectcolor='#707070')
        self.lang_ru_radio = Radiobutton(main,
                                         text='Russian',
                                         value='ru',
                                         variable=self.lang,
                                         font='Ubuntu',
                                         bg='#0f0e0e',
                                         fg='#cecece',
                                         indicatoron=False,
                                         selectcolor='#707070')
        self.lang_fr_radio = Radiobutton(main,
                                         text='French',
                                         value='fr',
                                         variable=self.lang,
                                         font='Ubuntu',
                                         bg='#0f0e0e',
                                         fg='#cecece',
                                         indicatoron=False,
                                         selectcolor='#707070')
        self.lang_es_radio = Radiobutton(main,
                                         text='Espanol',
                                         value='es',
                                         variable=self.lang,
                                         font='Ubuntu',
                                         bg='#0f0e0e',
                                         fg='#cecece',
                                         indicatoron=False,
                                         selectcolor='#707070')
        self.lang_de_radio = Radiobutton(main,
                                         text='German',
                                         value='de',
                                         variable=self.lang,
                                         font='Ubuntu',
                                         bg='#0f0e0e',
                                         fg='#cecece',
                                         indicatoron=False,
                                         selectcolor='#707070')

        self.res_text_label = Label(text='Translated text:',
                                    font='Ubuntu',
                                    bg='#0f0e0e',
                                    fg='#fcdbdb')
        self.res_text = Text(width=75,
                             height=20,
                             bg='#a5a5a5')
        self.res_lang = Label(text='Language for translation:',
                              font='Ubuntu',
                              bg='#0f0e0e',
                              fg='#fcdbdb')
        self.reslang = StringVar()
        self.res_lang_en_radio = Radiobutton(main,
                                             text='English',
                                             value='en',
                                             variable=self.reslang,
                                             font='Ubuntu',
                                             bg='#0f0e0e',
                                             fg='#cecece',
                                             indicatoron=False,
                                             selectcolor='#707070')
        self.res_lang_ru_radio = Radiobutton(main,
                                             text='Russian',
                                             value='ru',
                                             variable=self.reslang,
                                             font='Ubuntu',
                                             bg='#0f0e0e',
                                             fg='#cecece',
                                             indicatoron=False,
                                             selectcolor='#707070')
        self.res_lang_fr_radio = Radiobutton(main, text='French',
                                             value='fr',
                                             variable=self.reslang,
                                             font='Ubuntu',
                                             bg='#0f0e0e',
                                             fg='#cecece',
                                             indicatoron=False,
                                             selectcolor='#707070')
        self.res_lang_es_radio = Radiobutton(main,
                                             text='Espanol',
                                             value='es',
                                             variable=self.reslang,
                                             font='Ubuntu',
                                             bg='#0f0e0e',
                                             fg='#cecece',
                                             indicatoron=False,
                                             selectcolor='#707070')
        self.res_lang_de_radio = Radiobutton(main,
                                             text='German',
                                             value='de',
                                             variable=self.reslang,
                                             font='Ubuntu',
                                             bg='#0f0e0e',
                                             fg='#cecece',
                                             indicatoron=False,
                                             selectcolor='#707070')

        self.res_lang.grid(row=3, column=0)
        self.res_lang_en_radio.grid(row=3, column=1, sticky='w')
        self.res_lang_ru_radio.grid(row=3, column=2, sticky='w')
        self.res_lang_fr_radio.grid(row=3, column=3, sticky='w')
        self.res_lang_es_radio.grid(row=3, column=4, sticky='w')
        self.res_lang_de_radio.grid(row=3, column=5, sticky='w')
        self.res_text_label.grid(row=4, column=0)
        self.res_text.grid(row=4, column=1, columnspan=6)

        self.translate_text_label.grid(row=0, column=0)
        self.translate_text.grid(row=0, column=1, columnspan=6)
        self.translate_lang.grid(row=1, column=0)
        self.lang_en_radio.grid(row=1, column=1, sticky='w')
        self.lang_ru_radio.grid(row=1, column=2, sticky='w')
        self.lang_fr_radio.grid(row=1, column=3, sticky='w')
        self.lang_es_radio.grid(row=1, column=4, sticky='w')
        self.lang_de_radio.grid(row=1, column=5, sticky='w')

        self.translate_button = Button(main,
                                       text='Translate',
                                       relief='groove',
                                       width=22,
                                       height=2,
                                       font=('Ubuntu', 15),
                                       bg='#40c781',
                                       fg='white',
                                       activebackground='#ffdb2b',
                                       bd=-2)
        self.translate_button.grid(row=8, column=0, columnspan=3)
        self.translate_button.bind('<Button-1>', self.return_result)

        self.clear_button = Button(main,
                                   text='Clear',
                                   relief='groove',
                                   width=22,
                                   height=2,
                                   font=('Ubuntu', 15),
                                   bg='#cc2828',
                                   fg='white',
                                   activebackground='#ffdb2b',
                                   bd=-2)
        self.clear_button.grid(row=8, column=3, columnspan=3)
        self.clear_button.bind('<Button-1>', self.clear)

    def translator(self, text, lang, reslang):
        params = {'key': self.KEY,
                'text': text,
                'lang': '{}-{}'.format(lang, reslang)
                }
        response = requests.get(self.url, params=params)
        text = response.json()['text']
        return ' '.join(text)

    def return_result(self, event):
        text = self.translate_text.get(1.0, END)
        language = self.lang.get()
        res_language = self.reslang.get()
        result_text = self.translator(text, language, res_language)
        self.res_text.insert(END, result_text)

    def clear(self, event):
        self.res_text.delete(1.0, END)

    def open_file(self):
        of = askopenfilename()
        with open(of, 'r') as file:
            self.translate_text.insert(END, file.read())

    def save_file(self):
        sf = asksaveasfilename()
        final_text = self.res_text.get(1.0, END)
        with open(sf, 'w') as file:
            file.write(final_text)

    def exit(self):
        self.main.quit()


root = Tk()
root.geometry('743x735')
root.title('Translator')

main_window = Translator(root)

root.mainloop()
