import re
import logging


class FileProcessor(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def process(self, file_path):
        data = self.format_file_to_csv(file_path)
        self.store_new_file_as_csv(data)

    def format_file_to_csv(self, file_path):
        logging.info('Processing the data.')
        with open(file_path, encoding='utf8') as file:
            data = file.read()
            data = self.remove_bad_data(data)
            data = self.remove_encryption_message(data)
            data = self.change_dash_to_comma(data)
            data = self.remove_message_content(data)
            data = self.remove_empty_space_between_rows(data)
            return self.remove_minutes_from_time(data)

    def store_new_file_as_csv(self, data):
        logging.info('Creating a new file with the processed data.')
        with open('data_processed.csv', 'w', encoding='utf8') as file:
            file.write(data)

    def remove_encryption_message(self, data):
        return re.sub(r'.*end-to-end encryption.*\n', '', data, flags=re.MULTILINE)

    def remove_message_content(self, data):
        return re.sub(r'(: .*)', '', data, flags=re.MULTILINE)

    def remove_empty_space_between_rows(self, data):
        return re.sub(r'(, )', ',', data, flags=re.MULTILINE)

    def remove_minutes_from_time(self, data):
        return re.sub(r':\d{0,2}', '', data)

    def change_dash_to_comma(self, data):
        return re.sub(r'( - )', ',', data, flags=re.MULTILINE)

    def remove_bad_data(self, data):
        return re.sub(r'\n^(?!.*?(\d{0,2}/\d{0,2}/\d{0,2}, \d{0,2}:\d{0,2} [AP]M - .*?:.*\n)).*', '', data, flags=re.MULTILINE)
