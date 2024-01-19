class StateStack:
    def __init__(self):
        self.stack = []

    def push_state(self, state):
        self.stack.append(state)

    def pop_state(self):
        if self.stack:
            self.stack.pop()

    def current_state(self):
        if self.stack:
            return self.stack[-1]

    def handle_events(self):
        if self.current_state():
            self.current_state().handle_events()

    def update(self):
        if self.current_state():
            self.current_state().update()

    def render(self):
        if self.current_state():
            self.current_state().render()

    def run(self):
        while self.stack:
            self.handle_events()
            self.update()
            self.render()
