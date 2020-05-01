from datetime import datetime
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
            print(self.__dict__)
            start_time = datetime.now()
            result = func(self, *args, **kwargs)
            time_split = datetime.now() - start_time
            print(f'>>{self.message} stime: {time_split}')
            return result

        return decorator
