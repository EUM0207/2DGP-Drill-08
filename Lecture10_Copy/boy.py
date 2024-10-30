from pico2d import load_image

from state_machine import StateMachine

class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
                Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle}
            }
        )

    def update(self):
        #self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        #self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()


class Idle:
    @staticmethod
    def enter(boy):
        print('Boy Idle Enter')
    @staticmethod
    def exit(boy):
        print('Boy Idle Exit')
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.start_time > 1:
            boy.state_machine.add
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)

class Sleep:
    @staticmethod
    def enter(boy):
        boy.frame = 0
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                      3.141592 / 2, '', boy.x- 25, boy.y- 25, 100, 100)

class Run:
    @staticmethod
    def enter(boy):
        boy.action = 1
        boy.dir = 1
        boy.frame = 0
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x +=