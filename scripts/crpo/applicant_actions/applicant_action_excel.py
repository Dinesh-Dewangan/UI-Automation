import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class ApplicantActionsExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(ApplicantActionsExcelRead, self).__init__()

        self._applicant_name = 'Sprint{}'.format(self.sprint_version)

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['applicant_action_file'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_a = []
        self.xl_stage_a = []
        self.xl_status_a = []
        self.xl_mail_description_a = []
        self.xl_comment_a = []
        self.xl_sms_template_a = []
        self.xl_enable_link_a = []
        self.xl_reason_admit_card_a = []

        self.event_sprint_version_a = []

        # ------------- Iterate Excel sheet------------------------
        self.applicant_action_excel_read()

    def applicant_action_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_a.append(rows[0])
            if rows[1]:
                self.xl_stage_a.append(rows[1])
            if rows[2]:
                self.xl_status_a.append(rows[2])
            if rows[3]:
                self.xl_mail_description_a.append(rows[3])
            if rows[4]:
                self.xl_comment_a.append(rows[4])
            if rows[5]:
                self.xl_sms_template_a.append(rows[5])
            if rows[6]:
                self.xl_enable_link_a.append(rows[6])
            if rows[7]:
                self.xl_reason_admit_card_a.append(rows[7])

            for j in self.xl_event_name_a:
                event_name = j
                self.event_sprint_version_a = event_name.format(self.sprint_version)
