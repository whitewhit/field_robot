from typing_extensions import Self


class smartphone:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def type(self):
        print(f"The color of my smartphone is {self.color}, and my smartphone is {self.model} ")

        
cellphone = smartphone(" black "," samsung ")
cellphone.type()

phone = smartphone("blue","HTC")
phone.type()