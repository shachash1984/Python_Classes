#!/usr/bin/python


class Screen:
    # class variable
    serial_number = 10000001
    unique_handlers = {"AC"}

    # instance methods
    def __init__(self, height, width, brand, resolution, handlers=list()):
        self.height = height
        self.width = width
        self.brand = brand
        self.resolution = resolution
        self.handlers = handlers
        self.serial_number_id = Screen.serial_number
        self.post_init()

    def post_init(self):
        for item in self.handlers:
            Screen.add_handler_to_class(item)
        Screen.increment_serial_counter()

    @classmethod
    def add_handler_to_class(cls, handler):
        Screen.unique_handlers.add(handler)

    @classmethod
    def remove_handler_from_class(cls, handler):
        if handler in cls.unique_handlers:
            cls.unique_handlers.remove(handler)

    @classmethod
    def increment_serial_counter(cls):
        Screen.serial_number += 1

    def __repr__(self):
        return "serial number:{} height:{} width:{} brand:{} resolution:{} handlers:{}".format(self.serial_number_id,
                                                                                               self.height, self.width,
                                                                                               self.brand,
                                                                                               self.resolution,
                                                                                               self.handlers)

    def add_handler(self, handler):
        self.handlers.append(handler)
        Screen.add_handler_to_class(handler)

    def remove_handler(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)
        Screen.remove_handler_from_class(handler)

    def process_handlers(self):
        for i in range(0, len(self.handlers)):
            self.handlers[i] += "_Used"


    @property
    def prop_brand(self):
        return self.brand

    @prop_brand.setter
    def prop_brand(self, brand):
        self.brand = brand

    @property
    def prop_resolution(self):
        return self.resolution

    @prop_resolution.setter
    def prop_resolution(self, resolution):
        self.resolution = resolution


if __name__ == "__main__":
    lgTV = Screen(70, 90, "LG", "3840*2140", ["USB"])
    lgTV.add_handler("HDMI")
    print(lgTV)
    lgTV.remove_handler("USB")
    lgTV.add_handler("MiniDP")
    lgTV.remove_handler("MiniDP")
    print(lgTV)

    samsung = Screen(60, 40, "Samsung", "1920*1080", ["DP"])

    print(samsung)
    print(str(Screen.unique_handlers))
    print("brand: " + lgTV.prop_brand)
    lgTV.prop_brand = "MAG"
    print("brand: " + lgTV.prop_brand)

    print("resolution: " + lgTV.prop_resolution)
    lgTV.prop_resolution = "1920*1080"
    print("resolution: " + lgTV.prop_resolution)









