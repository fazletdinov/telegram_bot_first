from aiogram import Dispatcher, types


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description="Нажмите чтобы начать играть"),
        types.BotCommand(command='/help', description="Нажмите, если что-то непонятно"),

    ]

    await dp.bot.set_my_commands(main_menu_commands)
