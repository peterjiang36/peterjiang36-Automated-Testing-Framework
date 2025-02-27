from selenium.webdriver.common.by import By

class ToDoPage:
    def __init__(self, driver):
        self.driver = driver
        self.task_input = (By.CSS_SELECTOR, "input.new-todo")
        self.task_list = (By.CSS_SELECTOR, "ul.todo-list li")
        self.delete_button = (By.CSS_SELECTOR, "button.destroy")

    def add_task(self, task_name):
        self.driver.find_element(*self.task_input).send_keys(task_name + "\n")

    def get_tasks(self):
        return [task.text for task in self.driver.find_elements(*self.task_list)]

    def delete_task(self, task_name):
        tasks = self.driver.find_elements(*self.task_list)
        for task in tasks:
            if task_name in task.text:
                task.find_element(*self.delete_button).click()
                break