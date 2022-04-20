from queue import Queue
from Stream import Stream


class NameNotFoundError(Exception):
    pass


class Scheduler:
    def __init__(self, config):
        self.all_streams = {}
        self.active_streams = Queue()
        self.config = config
        for name, stream_data in config["streams"].items():
            stream = Stream(stream_data["address"], stream_data["priority"], name, stream_data["is_active"])
            self.all_streams[name] = stream
            if stream.is_active:
                self.active_streams.put_nowait(stream)

    def start_stream(self, name):
        if name not in self.all_streams.keys():
            raise NameNotFoundError()
        stream = self.all_streams[name]
        stream.start()
        self.active_streams.put_nowait(stream)
        self.config["name"]["is_active"] = True

    def stop_stream(self, name):
        if name not in self.all_streams.keys():
            raise NameNotFoundError()
        stream = self.all_streams[name]
        stream.stop()
        stream.priority_counter = -1
        self.config["name"]["is_active"] = False