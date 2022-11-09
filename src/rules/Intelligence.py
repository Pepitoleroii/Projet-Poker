import random

class AI:

    def __init__(self, AIT):
        self.AIT = AIT # AI Thread associé à cette instance
        self.id = self.AIT.id
        self.info = None
        self.me = None

    def get_info(self, info):
        info = info[3:]
        info = info.split("###")
        info[0] = info[0].split("##")
        info[1] = info[1].split("##")
        for i in range(len(info[0])):
            info[0][i] = info[0][i].split("#")
        for i in range(len(info[0])):
            info[0][i] = {
                "id": info[0][i][0], 
                "pseudo": info[0][i][1], 
                "money": int(info[0][i][2]), 
                "mise": int(info[0][i][3]), 
                "isAI": bool(int(info[0][i][4])), 
                "isDealer": bool(int(info[0][i][5])), 
                "isPlaying": bool(int(info[0][i][6]))}
        res = {"players": info[0], "main": info[1][:2], "board": info[1][2:], "mise": int(info[2]), "pot": int(info[3]), "blinde": int(info[4])}
        me = None
        for player in res["players"]:
            if player["id"] == self.id:
                me = player
        self.info, self.me = res, me

class Naive(AI):

    def __init__(self, AIT):
        super().__init__(AIT)
        self.pseudo = "Aleatoire"
    
    def decision(self):
        if self.info["mise"] == 0:
            possible = ["COUCHER", "MISE", "CHECK"]
        elif self.me["mise"] == self.info["mise"]:
            possible = ["COUCHER", "RELANCE", "CHECK"]
        else:
            possible = ["SUIVRE", "COUCHER", "RELANCE"]
        choix = randint(0,2)
        choix = possible[choix]
        if choix == "MISE":
            mini_value = min(self.info["blinde"], self.me["money"])
            maxi_value = max(mini_value, round(0.1 * self.me["money"]))
            value = randint(1, maxi_value)
            choix = f"MISE {value}"
        if choix == "RELANCE":
            mini_value = self.info["mise"] * 2
            maxi_value = max(min(self.info["blinde"], self.me["money"]), round(0.1 * self.me["money"]))
            if mini_value > maxi_value:
                return self.decision()
            value = randint(mini_value, maxi_value)
            choix = f"RELANCE {value}" 
        return choix       



def AI(type, AIT):
    if type == "naive":
        return Naive(AIT)