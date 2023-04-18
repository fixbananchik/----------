from slon import slon 
from kon import kon 
from ladia import ladia 
from ferz import ferz
from korol import korol 

figura = input("Введите фигуру, которой хотите походить ")
coordinates = input("Введиту координаты фигуры ")

if figura == "слон":
    slon(coordinates)

if figura == "конь":
    kon(coordinates)

if figura == "ладья":
    ladia(coordinates)

if figura == "ферзь":
    ferz(coordinates)

if figura == "король":
    korol(coordinates)