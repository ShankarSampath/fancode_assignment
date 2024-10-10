import pytest
from pages.todos_page import TodosPage
from pages.users_page import UsersPage
from config.config import Config

def test_fan_code_users_completed_tasks_percentage():
    config = Config()
    todos_page = TodosPage(config.BASE_URL)
    users_page = UsersPage(config.BASE_URL)
    users = users_page.get_users()
    fan_code_users = [user for user in users if config.FAN_CODE_LAT_MIN <= float(user["address"]["geo"]["lat"]) <= config.FAN_CODE_LAT_MAX and
                      config.FAN_CODE_LONG_MIN <= float(user["address"]["geo"]["lng"]) <= config.FAN_CODE_LONG_MAX]
    for user in fan_code_users:
        user_id = user["id"]
        todos = todos_page.get_todos()
        user_todos = [todo for todo in todos if todo["userId"] == user_id]
        completed_tasks = [todo for todo in user_todos if todo["completed"]]
        assert len(completed_tasks) / len(user_todos) > 0.5, f"User {user_id} has less than 50% completed tasks"