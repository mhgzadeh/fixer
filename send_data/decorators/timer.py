from datetime import datetime


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(f'\tElapsed Time: {hours}: {minutes}: {seconds}\n')
        return result

    return wrapper