import random


class Human:

    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today the {day} day of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day, woman=None):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(
                f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}"
            )
        self.days_indexes(day)
        print(
            f"======================={self.name} does that: ==========================="
        )
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print(
                    "I want to chill, but there is so much mess...\n So I will clean the house"
                )
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

        if woman:
            interaction_dice = random.randint(1, 2)
            if interaction_dice == 1:
                self.love(woman)
            else:
                self.argue(woman)
        print("-----------------------------------------------")

    def love(self, woman):
        print(f"I'm going to spend time with {woman.name}!")
        self.gladness += 30
        woman.gladness += 30

    def argue(self, woman):
        print(f"I'm angry at {woman.name}!")
        self.gladness -= 20
        woman.gladness -= 20


class Woman(Human):

    def __init__(self, name="Woman", job=None, home=None, car=None):
        super().__init__(name, job, home, car)
        self.gladness = 60

    def fix_hair(self):
        self.gladness += 10
        self.satiety -= 10
        print("Time for making my hair glow!")

    def look_after(self, person):
        print(f"I will help {person.name}!")
        self.gladness -= 10
        person.gladness += 20

    def live(self, day, man=None):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(
                f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}"
            )
        self.days_indexes(day)
        dice = random.randint(1, 4)
        print(
            f"======================={self.name} does that: ==========================="
        )
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print(
                    "I want to chill, but there is so much mess...\n So I will clean the house"
                )
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

        if man:
            interaction_dice = random.randint(1, 2)
            if interaction_dice == 1:
                self.love(man)
            else:
                self.argue(man)

    def love(self, man):
        print(f"I'm going to spend time with {man.name}!")
        self.gladness += 30
        man.gladness += 30

    def argue(self, man):
        print(f"I'm angry at {man.name}!")
        self.gladness -= 20
        man.gladness -= 20

    print("-----------------------------------------------")


class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:

    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:

    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Developer": {
        "salary": 50,
        "gladness_less": 10
    },
    "Teacher": {
        "salary": 20,
        "gladness_less": 30
    },
    "Pilot": {
        "salary": 100,
        "gladness_less": 5
    }
}

brands_of_car = {
    "BMW": {
        "fuel": 100,
        "strength": 100,
        "consumption": 6
    },
    "AUDI": {
        "fuel": 90,
        "strength": 70,
        "consumption": 8
    },
    "Lada": {
        "fuel": 50,
        "strength": 40,
        "consumption": 10
    },
    "Ferrari": {
        "fuel": 80,
        "strength": 120,
        "consumption": 14
    }
}

nick = Human(name="Nick")
mary = Woman(name="Mary")

for day in range(1, 8):
    if nick.live(day, mary) == False:
        break
    else:
        mary.live(day, nick)
