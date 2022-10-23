import datetime

class FileLog:
    @staticmethod
    def save_message(url_path:str, error_message:str):
        with open('logs.txt', 'a+') as f:
            date_time = datetime.datetime.now()
            date_time_str = date_time.strftime('%Y-%m-%d %H:%m:%S')
            log_format = '%s\t%s\t%s\n' % (date_time_str, url_path, error_message)
            f.write(log_format)
