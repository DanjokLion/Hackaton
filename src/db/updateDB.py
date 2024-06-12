import asyncio
from src.database import async_session_factory

class DataBaseController:
    async def update_data(self):
        new_data = await self.fetch_new_data()
        await self.update_database(new_data)
        await self.update_dashboard()
        
        # await asyncio.sleep(28_800)  # обновление раз в 8 часов

    async def fetch_new_data(self):
        pass

    async def update_database(self,new_data):
        pass

    async def update_dashboard(self):
        pass

controller = DataBaseController()