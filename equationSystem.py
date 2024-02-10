import Utils

class EquationSystem:
    def __init__(self,equation1,equation2,equation3=None):
        self.equation1 = equation1
        self.equation2 = equation2
        self.equation3 = equation3
        self.X = None
        self.Y = None
        if equation3 == None:
            self.Z = 0
        self.temp = []
    def estresoluble(self):
        if self.equation3 != None:
            return (self.equation1.facteurZ != None) & (self.equation2.facteurZ != None) & (self.equation1.facteurZ!=None)
        return True
    

    def trouverpour(self,inconnue,equation,other1,other2):
        match inconnue:
            case "X","x":
                self.X = equation.trouverX(other1,other2)
            case "Y","y":
                self.Y = equation.trouverY(other1,other2)
            case "Z","z":
                self.Z = equation.trouverZ(other1,other2)

    def resoudre(self):
    # 0) Si le système ne peut pas être résolu
        if self.estresoluble() ==False: return
    # 1) On s'assure d'avoir le même facteur pour x dans les deux équations
        ppmc = Utils.PPMC(self.equation1.facteurX,self.equation2.facteurX)
    # 2) On multiplie chaque équation pour avoir le même facteur de x
        mult1 = ppmc.diviser(self.equation1.facteurX)
        self.equation1 = self.equation1.multiplier(mult1)
        # self.equation1.afficher()
        mult2 = ppmc.diviser(self.equation2.facteurX)
        self.equation2 = self.equation2.multiplier(mult2)
        # self.equation2.afficher()
    # 3) On créé une fonction en soustrayant la seconde à la première
        func3 = self.equation1.soustraire(self.equation2)
        func3.afficher()
    # on en déduit Y
        self.Y = func3.trouverY(0,self.Z).value()
        # print(self.Y)
    # on en déduit X
        self.X = self.equation1.trouverX(self.Y,self.Z).value()
        # print(self.X)

        return
