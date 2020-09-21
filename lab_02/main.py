from lab_python_oop import Rectangle as rec
from lab_python_oop import circle as cir
from lab_python_oop import Square as sq
import requests

rec = rec.Rectangle(3, 2, 'blue')
print(rec)
circle = cir.Circle(5, 'green')
print(circle)
square = sq.Square(4, 'red')
print(square)

requst = requests.get('https://www.bmstu.ru')
print('Result of requsts: ' + str(requst.status_code))


