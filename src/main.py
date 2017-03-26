
from ui.Console import Console
from repository.FileRepository import FileRepository
from controller.Controller import Controller
repo = FileRepository("C:\\Users\\Utilizator\\Desktop\\University\\Semester 1\\FP\\scramble\\input")
ctrl=Controller(repo)
ui=Console(ctrl)
ui.play()