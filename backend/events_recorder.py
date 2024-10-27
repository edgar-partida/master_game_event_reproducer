import json
import time
from pynput import mouse, keyboard

class EventRecorder:
    def __init__(self):
        self.events = []
        self.recording = False
        self.mouse_listener = None
        self.keyboard_listener = None
        self.mouse_controller = mouse.Controller()

    def on_click(self, x, y, button, pressed):
        if pressed and self.recording:
            current_time = time.time()
            event = {
                'x': x,
                'y': y,
                'button': str(button),
                'time': current_time
            }
            self.events.append(event)
            print(f'Click registered: {event}')  # For debugging

    def stop_recording(self, key):
        self.recording = False
        if self.mouse_listener is not None:
            self.mouse_listener.stop()
        if self.keyboard_listener is not None:
            self.keyboard_listener.stop()
        self.save_events('mouse_events.json')
        print("Recording stopped. Events saved.")

    def save_events(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.events, f)

    def replay_events(self, filename):
        print(f"Starting replying events for filename: {filename}")
        with open(filename, 'r') as f:
            recorded_events = json.load(f)

        if not recorded_events:
            print("No events to replay.")
            return

        last_time = recorded_events[0]['time']
        for event in recorded_events:
            time.sleep(event['time'] - last_time)  # Wait between events
            last_time = event['time']
            x, y = event['x'], event['y']
            button = event['button']
            
            # Move mouse and simulate click
            self.mouse_controller.position = (x, y)
            if 'left' in button:
                self.mouse_controller.click(mouse.Button.left, 1)
            elif 'right' in button:
                self.mouse_controller.click(mouse.Button.right, 1)
        print(f"Events completed for filename: {filename}")

    def start_recording(self):
        self.events = []  # Clear previous events
        self.recording = True
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.stop_recording)
        self.mouse_listener.start()
        self.keyboard_listener.start()
        print("Recording clicks... Press Esc to stop.")
