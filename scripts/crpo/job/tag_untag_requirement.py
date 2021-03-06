import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import interview_panel


class JobTagToRequirement(interview_panel.InterviewPanel):
    def __init__(self):
        super(JobTagToRequirement, self).__init__()

        self.ui_tag_requirement_action = []
        self.ui_tag_requirement = []
        self.ui_un_tag_requirement_action = []
        self.ui_un_tag_requirement = []

    def tag_requirement(self):
        self.job_validation('requirement tag')
        self.driver.refresh()
        time.sleep(2)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.floating_action()

                self.web_element_click_xpath(page_elements.floating_actions['tag_requirement'])
                self.ui_tag_requirement_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Requirements'),
                                                 self.xl_tag_req)
                self.drop_down_selection()

                self.web_element_click_xpath(page_elements.buttons['job_requirement_tag'])
                print('**-------->>> Job tag to requirement successfully')
                self.ui_tag_requirement = 'Pass'

            except Exception as error:
                api_logger.error(error)

    def un_tag_requirement(self):
        self.job_validation('requirement un-tag')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(2)
                self.floating_action()

                self.web_element_click_xpath(page_elements.floating_actions['un-tag_requirement'])
                self.ui_un_tag_requirement_action = 'Pass'

                self.web_element_click_xpath(page_elements.buttons['ok'])
                print('**-------->>> Job un-tag to requirement successfully')
                self.ui_un_tag_requirement = 'Pass'

            except Exception as error:
                api_logger.error(error)
