from models import *
import random


names = ['Kostya', 'Segrey', 'Ivan Ivanovich', 'Petr', 'Evgeniya', 'Ekaterina']

for name in names:
    Data.create(name=name, age=random.randint(1, 100))