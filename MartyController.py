from PyQt6.QtCore import Qt


class MartyController:
    def __init__(self, marty):
        self.my_marty = marty

    def divide_angle(self, original_angle, max_angle=45):
        iterations = original_angle // max_angle
        last_angle = original_angle % max_angle
        return [max_angle * (1 if original_angle > 0 else -1)] * abs(iterations) + [last_angle]
        #to do verifier cas avec virgule et négatif
    def move_forward(self):
        self.my_marty.walk(2, 'auto', 0)

    def move_backward(self):
        for angle in self.divide_angle(180):
            self.my_marty.walk(2, 'auto', 180)

    def turn_right(self):
        for angle in self.divide_angle(90):
            self.my_marty.walk(2, 'auto', angle)

    def turn_left(self):
        for angle in self.divide_angle(-90):
             self.my_marty.walk(2, 'auto', 90)

    def manage_eyes(self):
        self.my_marty.eyes('angry', 2, False)

    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def key_press_event(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.move_backward()
        elif event.key() == Qt.Key.Key_D:
            self.turn_right()
        elif event.key() == Qt.Key.Key_Q:
            self.turn_left()

    def close(self):
        self.my_marty.close()
    def baterry_percentage(self):
        battery_percentage = self.my_marty.get_battery_remaining()