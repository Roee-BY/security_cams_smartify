from threading import Thread
import cv2


class Stream:
    def __init__(self, address, priority, name, is_active):
        self.address = address
        self.priority = priority
        self.name = name
        self.stream = None
        self.is_active = is_active
        self.people_count_queue = {}
        self.last_detections = []
        self.curr_frame = None
        self.curr_frame_status = None
        self.priority_counter = priority

    def start(self):
        print("info | starting stream " + self.name + " at address " + self.adress + " with priority " + self.prioeity)
        self.stream = cv2.VideoCapture(self.address)
        self.curr_frame_status, self.curr_frame = self.stream.read()
        self.is_active = True
        t = Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()

    def update(self):
        while True:
            if not self.is_active:
                return
            self.curr_frame_status, self.curr_frame = self.stream.read()

    def stop(self):
        print("info | stopping stream " + self.name + " at address " + self.adress)
        self.is_active = False
        self.stream.release()
        self.stream = None

    def get_frame(self):
        if not self.is_active:
            raise Exception("Stream is not active!")
        return self.curr_frame.copy()
