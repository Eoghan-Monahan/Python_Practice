class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer/self.time
        else:
            pass

    def show_state(self):
        print("I'm going {} kph".format(self.speed))


if __name__ == "__main__":
    car = Car()
    while True:
        action = input("What should i do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed? ").upper()
        if action not in "ABOS" or len(action) != 1:
            print("Invalid input.")
            continue
        if action == "A":
            car.accelerate()
        elif action == "B":
            car.brake()
        elif action == "O":
            print("We have gone {} km".format(car.odometer))
        elif action == "S":
            print(car.average_speed())

        car.step()
        car.show_state()
