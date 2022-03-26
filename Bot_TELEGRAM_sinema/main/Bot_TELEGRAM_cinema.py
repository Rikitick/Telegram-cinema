import requests
from bs4 import BeautifulSoup
import lxml
import telebot
import os

def telegram_bot():
    bot = telebot.TeleBot("Your token")

    @bot.message_handler(commands=['start'])
    def start(message):

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Анимация')
        item2 = telebot.types.KeyboardButton('Аниме')
        item3 = telebot.types.KeyboardButton('Балет')
        item4 = telebot.types.KeyboardButton('Биография')
        item5 = telebot.types.KeyboardButton('Боевик')
        item6 = telebot.types.KeyboardButton('Вестерн')
        item7 = telebot.types.KeyboardButton('Военный')
        item8 = telebot.types.KeyboardButton('Детектив')
        item9 = telebot.types.KeyboardButton('Детский')
        item10 = telebot.types.KeyboardButton('Документальный')
        item11 = telebot.types.KeyboardButton('Драма')
        item12 = telebot.types.KeyboardButton('Исторический')
        item13 = telebot.types.KeyboardButton('Комедия')
        item14 = telebot.types.KeyboardButton('Концерт')
        item15 = telebot.types.KeyboardButton('Короткометражный')
        item16 = telebot.types.KeyboardButton('Криминал')
        item17 = telebot.types.KeyboardButton('Мелодрама')
        item18 = telebot.types.KeyboardButton('Мистика')
        item19 = telebot.types.KeyboardButton('Музыка')
        item20 = telebot.types.KeyboardButton('Мюзикл')
        item21 = telebot.types.KeyboardButton('Приключения')
        item22 = telebot.types.KeyboardButton('Сборник')
        item23 = telebot.types.KeyboardButton('Семейный')
        item24 = telebot.types.KeyboardButton('Сказка')
        item25 = telebot.types.KeyboardButton('Спорт')
        item26 = telebot.types.KeyboardButton('Триллер')
        item27 = telebot.types.KeyboardButton('Ужасы')
        item28 = telebot.types.KeyboardButton('Фантастика')
        item29 = telebot.types.KeyboardButton('Фэнтези')
        item30 = telebot.types.KeyboardButton('Эротика')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                   item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26,
                   item27, item28, item29, item30)

        os.getcwd()
        sti = open('310891935.png', "rb")
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, f'Если ты не знаешь что посмотреть в ближайшее время, то ты пришёл по адресу! \nЯ подскажу тебе лучшие фильмы по версии сайта Kinoafisha.')
        bot.send_message(message.chat.id, 'Выбери, по какому жанру ты хочешь узнать лучший фильм.', reply_markup=markup)

    @bot.message_handler()
    def best_film(message):
        ganre = {
            'Анимация': 'animation/',
            'Аниме': 'anime/',
            'Балет': 'ballet/',
            'Биография': 'biography/',
            'Боевик': 'action/',
            'Вестерн': 'western/',
            'Военный': 'military/',
            'Детектив': 'detective/',
            'Детский': 'children/',
            'Документальный': 'documentary/',
            'Драма': 'drama/',
            'Исторический': 'history/',
            'Комедия': 'comedy/',
            'Концерт': 'koncert/',
            'Короткометражный': 'short/',
            'Криминал': 'criminal/',
            'Мелодрама': 'romantic/',
            'Мистика': 'mystic/',
            'Музыка': 'music/',
            'Мюзикл': 'musical/',
            'Приключения': 'adventure/',
            'Сборник': 'collection/',
            'Семейный': 'family/',
            'Сказка': 'fairytale/',
            'Спорт': 'sport/',
            'Триллер': 'thriller/',
            'Ужасы': 'horror/',
            'Фантастика': 'sci-fi/',
            'Фэнтези': 'fantasy/',
            'Эротика': 'erotic/',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

        try:
            req = requests.get(url=f'https://www.kinoafisha.info/rating/movies/{ganre[message.text]}', headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            film = soup.find('div', class_="grid_cell9").find('div', class_="movieItem-rating")
            img = soup.find('div', class_="grid_cell9").find('div', class_="movieItem-rating").find('a').find('picture', class_="movieItem_poster").find('source').get('srcset')
            name_film = film.find("a", class_='movieItem_title').text.strip()
            genre = film.find('span', class_='movieItem_genres').text.strip()
            grade = film.find('span', class_='rating_num').text.strip()
            req1 = requests.get(url=film.find('a').get('href'))
            soup1 = BeautifulSoup(req1.text, 'lxml')
            try:
                content = soup1.find('div', class_='js-active').find('p').text.strip()
            except:
                content = 'Нет информации'

            bot.send_message(message.chat.id, f"Постер фильма: {img}")
            bot.send_message(message.chat.id, f"Название фильма: {name_film}")
            bot.send_message(message.chat.id, f"Жанр: {genre}")
            bot.send_message(message.chat.id, f"Рейтинг: {grade}")
            bot.send_message(message.chat.id, f"Описание: {content}")
            bot.send_message(message.chat.id, 'Если вы хотите посмотреть больше фильмов по этому жанру, то можете '
                                              f'перейти на сайт: https://www.kinoafisha.info/rating/movies/{ganre[message.text]}')
        except:
            bot.send_message(message.chat.id, 'Я вас не понял.')

    bot.polling()

if __name__ == "__main__":
    telegram_bot()
