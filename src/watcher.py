import math, time, src.run as run

def watcher(original_function, name, interval=1, repeat=math.inf):
    """Backend function for watcher decorator"""
    def collector(interval, repeat, name):
        """Backend function for dealing with watcher timing"""
        count = 0
        while count < repeat:
            count += 1
            run.data[name] = {"data":original_function(), "offset": int(time.time()) - run.data['lastSync']}
            time.sleep(interval)
    run.collectors[name] = {"function":collector, "interval": interval, "repeat": repeat}

def newWatcher(interval=1, repeat=math.inf):
    """
    Decorator for watcher
    Usage: @newWatcher(interval=1, repeat=math.inf)
    """
    def functionCollector(original_function):
        watcher(original_function, original_function.__name__, interval, repeat)
    return functionCollector
