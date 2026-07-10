# src/main.py

from fleet_models import ShipWallet, AdityaSolarProbe, DeepSpaceCargo

spaceship = ShipWallet(5000000, 3000000, 800000, 5)
spaceship.reserves
print(spaceship)
spaceship.reserves = 5500000
spaceship.fuel_filling(3000000)
ship1 = AdityaSolarProbe(3000000, 1500000, 3000000, 2)
print(ship1)
ship2 = DeepSpaceCargo(3000000, 1800000, 3500000, 3)
print(ship2)
print(ship1 + spaceship)
print(len(spaceship))
ship1.calculate_range(25)
spaceship.mission_launch()
spaceship.mission_timestamp()