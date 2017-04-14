from flask import *
import pyexcel
import mlab
import random
from models.GetIdea import GetIdea
import time

mlab.connect()

#open xlsx
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# records = pyexcel.iget_records(file_name="data.xlsx")
# sheet = pyexcel.get_sheet(file_name = "data.xlsx")
# print(sheet["B10"])

#def updata(records):
# for record in records:
#     Idea = record["IDEAS"]
#     ideas = GetIdea(Idea=Idea)
#     ideas.save()
# ideaa = []
# idea_load = GetIdea.objects()
# for idea in idea_load:
#     ideaa.append(idea["Idea"])
# i = random.randint(0, 12)
#
# idea1 = ideaa[i]

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    text = "nsadknasdwqioejndfdls"
    if request.method == "GET":
        return render_template("index.html", text=text)
    elif request.method == "POST":
        text = ""
        ideaa = []
        idea_load = GetIdea.objects()
        for idea in idea_load:
            ideaa.append(idea["Idea"])
        x = random.randint(0, 12)
        y = random.randint(0, 12)
        while y == x:
            y = random.randint(0, 12)
        z = random.randint(0, 12)
        while z == x or z == y:
            z = random.randint(0, 12)
        idea1 = ideaa[x]
        idea2 = ideaa[y]
        idea3 = ideaa[z]
        return render_template("index.html", idea1=idea1, idea2=idea2, idea3=idea3, text=text)


@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
