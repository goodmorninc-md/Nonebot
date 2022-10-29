from nonebot import get_bot

bot = get_bot("bot_id")
result = await bot.get_user_info(user_id=12345678)

await bot.call_api("get_user_info",user_id=12345678)
