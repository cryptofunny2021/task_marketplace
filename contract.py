# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class TaskMarketplace(gl.Contract):

    tasks: TreeMap[Address, str]

    def __init__(self):
        pass

    @gl.public.write
    def create_task(self, task: str) -> None:
        user = gl.message.sender_address
        self.tasks[user] = task

    @gl.public.view
    def my_task(self) -> str:
        user = gl.message.sender_address
        return self.tasks.get(user, "")
