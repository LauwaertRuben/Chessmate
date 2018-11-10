class chessman:
    def __init__(self, kind=None, identification=None, color=None):
        #kind = pion, koning, loper...
        #identification = pion1, pion2,pion3,...
        self.__kind = kind
        self.__identification = identification
        self.__color = color

    def get_kind(self):
        return self.__kind

    def get_identification(self):
        return self.__identification

    def get_color(self):
        return self.__color

    def get_possible_moves(self, position):
        #stel we gaan er vanuit dat position een tuple is met de 2 coordinaten
        if self.__kind == "pion":
            #3 en 4 mogen enkel als hij een pion kan pakken van de tegenstander!
            option1 = (position[0], position[1] +1)
            option2 = (position[0], position[1] + 2)
            option3 = (position[0]-1, position[1] + 1)
            option4 = (position[0]+1, position[1] + 1)
            return option1, option2, option3, option4

        if self.__kind == "koning":
            option1 = (position[0], position[1] + 1)
            option2 = (position[0], position[1] -1)
            option3 = (position[0]+1, position[1])
            option4 = (position[0]-1, position[1])
            return option1, option2, option3, option4



