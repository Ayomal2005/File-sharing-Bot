from bot import Bot
import asyncio

async def main():
    bot = Bot()
    await bot.start()  # Properly await the start coroutine
    
    try:
        print("Bot is running...")
        await asyncio.get_event_loop().create_future()  # Keep the bot running
    except KeyboardInterrupt:
        print("Stopping bot...")
    finally:
        await bot.stop()  # Properly stop the bot

if __name__ == "__main__":
    asyncio.run(main())
