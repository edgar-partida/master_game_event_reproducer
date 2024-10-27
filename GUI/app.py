import tkinter as tk
import threading
from backend.events_recorder import EventRecorder

class App:

    def __init__(self, master):
        self.master = master
        master.title("Master Game Events Reproducer")

        self.recorder = EventRecorder()

        self.record_button = tk.Button(master, text="Record Clicks", command=self.on_record_button)
        self.record_button.pack(pady=10)

        self.replay_button = tk.Button(master, text="Replay Clicks", command=self.on_replay_button)
        self.replay_button.pack(pady=10)
        

    def on_record_button(self):
        threading.Thread(target=self.recorder.start_recording).start()

    def on_replay_button(self):
        self.recorder.replay_events('mouse_events.json')
