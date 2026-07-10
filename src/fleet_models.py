# src/fleet_models.py

from abc import ABC, abstractmethod
from utils import log_mission, LowFuelError

class SpaceAsset(ABC):

    @abstractmethod
    def calculate_range(self, mileage):
        return self._tank_capacity * mileage

class ShipWallet(SpaceAsset):

    def __init__(self, fuel_reserves, tank_capacity, cargo_capacity, crew_members):
           self.__fuel_reserves = fuel_reserves
           self._tank_capacity = tank_capacity
           self._cargo_capacity = cargo_capacity
           self._crew_members = crew_members

    def calculate_range(self, mileage):
        print(f"Range of SpaceShip is {self._tank_capacity * mileage} Miles")

    def fuel_filling(self, fuel):
        if fuel < 0:
            print("----Fuel quantity can't be of negative value.----")

        elif fuel > self._tank_capacity:
            print(f"[Warning]:Overloading!!\nFuel loaded in spaceship is exceeding it's {self._tank_capacity}L limit.\nTurn off the pipelines immediately...!")

        elif fuel == self._tank_capacity:
            print("-----Filling fuel into the spaceship's fuel tank.-----")
            print("[Message]:Spaceship tank has been filled to it's limit.")
            print(f"Fuel reserves left are {self.__fuel_reserves - fuel}L")

        else:
            print("-----Filling fuel into the spaceship's fuel tank.-----")
            print(f"{fuel}L of fuel has been loaded to the spaceship")
            print(f"Fuel reserves left are {self.__fuel_reserves - fuel}L")

        if fuel < 500000 and fuel > 0:
            raise LowFuelError("[Warning]: You're soon gonna run out of Fuel...!")
    
    @property
    def reserves(self):
        print(f"We have {self.__fuel_reserves}L of fuels reserves with {self._tank_capacity}L of tank capacity of spaceship.")
        
    @reserves.setter
    def reserves(self, fuel_reserves):
        self.__fuel_reserves = fuel_reserves
            
    def __str__(self):
        return f"SpaceShip have a loading capacity of {self._cargo_capacity}L with fuel tank capacity of {self._tank_capacity}L and {self._crew_members} crew members."

    def __len__(self):
        return self._crew_members

    def __add__(self, other):
        return f"Spaceship have a Cargo Capacity of {self._cargo_capacity + other._cargo_capacity}L"

    @log_mission
    def mission_timestamp(self):
        pass

    def mission_launch(self):
        print("----All data set everything verified----\n----We're ready to launch in 10 seconds.----")
        for i in range(10,-1, -1):
            print(i)
        print("Here we go...!")

class AdityaSolarProbe(ShipWallet):

    def calculate_range(self, mileage):
        print(f"Range of Aditya Solar Probe is {self._tank_capacity * mileage} Miles")

    def __str__(self):
        return f"Aditya Space Probe have a loading capacity of {self._cargo_capacity}L with fuel tank capacity of {self._tank_capacity}L and {self._crew_members} crew members."

    def __len__(self):
        return self._crew_members
    
class DeepSpaceCargo(ShipWallet):

    def calculate_range(self, mileage):
        print(f"Range of Deep Space Cargo is {self._tank_capacity * mileage}Miles")

    def __str__(self):
        return f"Deep Space Cargo have a loading capacity of {self._cargo_capacity}L with fuel tank capacity of {self._tank_capacity}L and {self._crew_members} crew members."

    def __len__(self):
        return self._crew_members