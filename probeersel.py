"""dimensie van een schaakbord = 8x8
ik ga er vanuit dat een positie een tuple is: (1,1) vb
keuze die we moeten maken is: beginnen we op 1 of op 0 te tellen voor de positie
ik stel voor op 0"""

def is_valid_position(position):
    if position[0] < 0:
        return False
    if position[0] > 7:
        return False
    if position[1] < 0:
        return False
    if position[1] > 7:
        return False
    return True

def get_all_valid__positions(positions)
    """hier komt geef je een lijst van posities mee: [(1,2), (2,3), ...]
    deze functie returnt enkel de correcte positions"""
    valid = []
    for position in positions:
        if is_valid_position(position):
            valid.append(position)
    return valid





class Chessman:
    def __init__(self, kind=None, identification=None, color=None, position = None):
        #kind = pion, koning, loper...
        #identification = pion1, pion2,pion3,...
        self.__kind = kind
        self.__identification = identification
        self.__color = color
        self.__position = position

    def get_kind(self):
        return self.__kind

    def get_identification(self):
        return self.__identification

    def get_color(self):
        return self.__color

    def get_possible_moves(self):
        #OP DE MOMENT HOU IK NOG GEEN REKENING MET HET FEIT DAT EEN PION NIET NAAR VOOR KAN
        #ALS ER AL EEN STUK STAAT!
        #stel we gaan er vanuit dat position een tuple is met de 2 coordinaten
        if self.__kind == "pion":
            #3 en 4 mogen enkel als hij een pion kan pakken van de tegenstander!
            option1 = (self.__position[0], self.__position[1] +1)
            option2 = (self.__position[0], self.__position[1] + 2)
            option3 = (self.__position[0]-1, self.__position[1] + 1)
            option4 = (self.__position[0]+1, self.__position[1] + 1)
            return get_all_valid__positions([option1, option2, option3, option4])

        elif self.__kind == "koning":
            option1 = (self.__position[0], self.__position[1] + 1)
            option2 = (self.__position[0], self.__position[1] -1)
            option3 = (self.__position[0]+1, self.__position[1])
            option4 = (self.__position[0]-1, self.__position[1])
            return get_all_valid__positions([option1, option2, option3, option4]) #hiermee houden we rekening met de grenzen van het veld.







