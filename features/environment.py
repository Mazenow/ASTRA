import os
from allure_commons.types import AttachmentType
import allure

def before_all(context):
    import os
    os.environ["LANG"] = "ru_RU.UTF-8"

def before_all(context):
    context.allure_results_path = 'allure-results'
    context.report_dir = 'allure-report'
    if os.path.exists(context.allure_results_path):
        for file in os.listdir(context.allure_results_path):
            os.remove(os.path.join(context.allure_results_path, file))


def after_step(context, step):
    if step.status == 'failed':
        with allure.step('скриншот при ошибке'):
            screenshot_file = 'screenshot.png'
            context.driver.save_screenshot(screenshot_file)
            allure.attach.file(screenshot_file, attachment_type=AttachmentType.PNG)