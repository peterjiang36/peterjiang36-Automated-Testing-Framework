import pytest
from test_setup import get_driver
from pages.todo_page import ToDoPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://example-todo-app.com")  # Replace with your app URL
    yield driver
    driver.quit()

def test_add_task(setup):
    page = ToDoPage(setup)
    page.add_task("Buy groceries")
    tasks = page.get_tasks()
    assert "Buy groceries" in tasks

def test_delete_task(setup):
    page = ToDoPage(setup)
    page.add_task("Walk the dog")
    page.delete_task("Walk the dog")
    tasks = page.get_tasks()
    assert "Walk the dog" not in tasks