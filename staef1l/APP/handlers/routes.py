from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()



@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет😊\nТелеграмм-канал - <a href='t.me/PusssyBastard'>ТЫЫК</a>✈️\nЮтуб-канал - <a href='www.youtube.com/@staefil-off'>ЖМЯК</a>🎥\nТвич-канал -- <a href='twitch.tv/staefil'>КЛИК</a>💜\nВк-группа -- <a href='vk.com/newuntitled'>ПУНЬ</a>🟦\n\nПодробнее об одной интересной функции -- /dist\nУзнать подробнее о нашей недо-команде можно по команде /about",
        parse_mode="HTML")


@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        "📫Предложить идею -- https://t.me/Staef1l_ideas_bot\n🛠️Техподдержка -- https://t.me/Staef1l_feedback_bot\n🎭Анонимки команде -- https://t.me/voprosy?start=h86ub\n\nСоздал pnp, помогали с ботом blood1lina.",
        parse_mode="HTML")
    

@router.message(Command("dist"))
async def dist(message: Message):
    await message.answer(
        "Эта функция ещё не доделана, в скором времени будет доделана.\n\nДанная функция должна работать как подписка на рассылку. Тем не менее это возможно осуществить и сейчас, но для этого придётся запариться и около 10-20 минут разбираться вместе с техподдержкой, а это никому не нужно.\n\nВажно понимать, что наша команда работает на износ, чтобы сократить время активирование рассылки и доделать бота в кратчайшие сроки все нужные функции.\n\nЕсли желание делать себе рассылку (которая может и не активироваться) никуда не пропало, то активируйте <a href='https://t.me/STAEF1L_distribution_bot'>ЭТОГО БОТА</a>, затем пишите в <a href='https://t.me/Staef1l_feedback_bot'>ТЕХПОДДЕРЖКУ</a>",
        parse_mode="HTML")


@router.message(Command("secret"))
async def secret(message: Message):
    await message.answer("<a href='https://byrutgame.org/index.php?do=download&id=175587'>секретка, нажми и узнай что это (там вирусы)</a>",
                         parse_mode="HTML")


@router.message()
async def mess(message: Message):
    await message.answer("❌Извини, но бот настолько тупой, что не может понять, что ты написал. Он в принципе ничего не может понять кроме двух команд: /start и /about")

