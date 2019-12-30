#!/usr/bin/python
import Screen


class Screen3D(Screen.Screen):
    def __init__(self, height, width, brand, resolution, handlers=list(), glasses=False):
        super().__init__(height, width, brand, resolution, handlers)
        self.glasses = glasses

    def __repr__(self):
        return "{} glasses:{}".format(super().__repr__(), self.glasses)

    def process_handlers(self):
        super().process_handlers()
        self.handlers.append("end")


if __name__ == "__main__":
    s = Screen3D(height=300, width=200, brand="Pilot", resolution="1920*1080", glasses=True)
    s.add_handler("Optic")
    s.process_handlers()
    print(s)
