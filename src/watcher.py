import time, math

def watcher(original_function, name, interval=1, repeat=math.inf):
    """Backend function for watcher decorator"""
    count = 0
    while count < repeat:
        time.sleep(interval)
        return_value = original_function()
        count += 1

def newWatcher(interval=1, repeat=math.inf):
    """
    Decorator for watcher
    Usage: @newWatcher(interval=1, repeat=math.inf)
    """
    def functionCollector(original_function):
        watcher(original_function, original_function.__name__, interval, repeat)
    return functionCollector
