from time import time, gmtime
from functools import wraps

# ==============================================================================#
# Print execute time of the function                                            #
# ==============================================================================#
class Timer:
    def __init__(self, message='', interval=500):
        self.message = f' {message}' if message else message
        self.interval = interval

    def __call__(self, func):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            start_time = time()
            result = func(self, *args, **kwargs)
            time_split = gmtime(time() - start_time)
            print(f'>>{self.message} time: {time_split.tm_hour:02}:{time_split.tm_min:02}\'{time_split.tm_sec:.3f}')
            return result

        return decorator
