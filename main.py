import csv
from pathlib import Path

warnings = []
class CwarningSign:
    def __init__(self, Symptom, WarningSign, CopingStrategy, PeoplePlaces, Grounding):
        self.Symptom = Symptom
        self.WarningSign = WarningSign
        self.CopingStrategy = CopingStrategy
        self.PeoplePlaces = PeoplePlaces
        self.Grounding = Grounding

    def toString(self): #for debug
        print(self.Symptom)
        print(self.WarningSign)
        print(self.CopingStrategy)
        print(self.PeoplePlaces)
        print(self.Grounding)

    def writeString(self):
        string = f"\n{self.Symptom},{self.WarningSign},{self.CopingStrategy},{self.PeoplePlaces},{self.Grounding}"
        return string

def parseFile(sFile):
    path = Path(f"./{sFile}")
    if path.is_file() is True:
        with open(path, mode="r") as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                sy = row.get("Symptom")
                if sy is None:
                    continue
                ws = row.get("WarningSign")
                if ws is None:
                    continue
                cs = row.get("CopingStrategy")
                if cs is None:
                    continue
                pp = row.get("PeoplePlaces")
                if pp is None:
                    continue
                ground = row.get("GroundingTools")
                if ground is None:
                    continue
                warnings.append(CwarningSign(sy, ws, cs, pp, ground))
        file.close()
    else:
        print("file not found!")

def hascomma(stuff):
    for i in stuff:
        if i is ",":
            return True
    return False

def askForInput(sFile):#a comma will destory the integrity of the csv file.  we must check for it.
    sym = ","
    ws = ","
    cs = ","
    pp = ","
    ground = ","
    while hascomma(sym) is True:
        sym = input("Please enter a symptom: ")
    while hascomma(ws) is True:
        ws = input("Please enter a warning sign:  ")
    while hascomma(cs) is True:
        cs = input("Please enter a coping strategy:  ")
    while hascomma(pp) is True:
        pp = input("Please enter people places:  ")
    while hascomma(ground) is True:
        ground = input("Please enter grounding ideas:  ")
    newWarning = CwarningSign(sym, ws, cs, pp, ground)
    writeToFile(sFile, newWarning)

def writeToFile(sFile, warningSign):
    path = Path(f"./{sFile}")
    print(path)
    with open(path, mode="a") as file:
        num = file.write(warningSign.writeString())
        print(num)
    file.close()


if __name__ == '__main__':
    parseFile("WarningSigns.txt")
    for warn in warnings:
        print(f"Symptom:  {warn.Symptom}  Warning Sign: {warn.WarningSign} Coping Strategy:  {warn.CopingStrategy}  People/Places:  {warn.PeoplePlaces} Ground Tools:  {warn.Grounding}")
    inp = input("Would you like to enter a warning sign?  ").lower()
    if inp == 'yes':
        askForInput("WarningSigns.txt")

