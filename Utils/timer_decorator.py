from time import strftime, time, gmtime
from functools import wraps

# ==============================================================================#
# Print execute time of the function                                            #
# ==============================================================================#
class Timer:
    def __init__(self, message=''):
        if message:
            self.message = ' ' + message
        else:
            self.message = message

    def __call__(self, func):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            start_time = time()
            result = func(self, *args, **kwargs)
            time_split = gmtime(time() - start_time)
            print(f'>>{self.message} time: {strftime("%H:%M:%S", time_split}')
            return result

        return decorator
