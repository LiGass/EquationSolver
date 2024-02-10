import fraction

class Equation:
    def __init__(self,result,facteurX,facteurY,facteurZ=0, nom = "f"):
        if isinstance(facteurX,int):
            self.facteurX = fraction.Fraction(facteurX)
        else:
            self.facteurX = facteurX
        if isinstance(facteurY,int):
            self.facteurY = fraction.Fraction(facteurY)
        else:
            self.facteurY = facteurY
        if isinstance(facteurZ,int):
            self.facteurZ = fraction.Fraction(facteurZ)
        else:
            self.facteurZ = facteurZ
        if isinstance(result,int):
            self.result = fraction.Fraction(result)
        else:
            self.result = result
        self.nom = nom
        self.unknownCount = 2 if facteurZ==None else 3

    def afficher(self):
        if(self.unknownCount==2):
            print("("+self.nom+") =>     "+ self.facteurX.texte() +"*X + "+ self.facteurY.texte() +"*Y = "+self.result.texte())
        else:
            print("("+self.nom+") =>     "+ self.facteurX.texte() +"*X + "+ self.facteurY.texte() +"*Y + "+ self.facteurZ.texte() +"*Z = "+self.result.texte())

    def afficherpourY():
        return

    def multiplier(self,nombre):
        if isinstance(nombre,int):
            nombre = fraction.Fraction(nombre)
        if self.facteurZ == None:
            nouvelle = Equation(self.result.multiplier(nombre),self.facteurX.multiplier(nombre),self.facteurY.multiplier(nombre))
        else:
            nouvelle = Equation(self.result.multiplier(nombre),self.facteurX.multiplier(nombre),self.facteurY.multiplier(nombre),self.facteurZ.multiplier(nombre))
        return nouvelle

    def soustraire(self,otherEquation):
        result = self.result.soustraire(otherEquation.result)
        facteurX = self.facteurX.soustraire(otherEquation.facteurX)
        facteurY = self.facteurY.soustraire(otherEquation.facteurY)
        if(self.facteurZ!=None) & (otherEquation.facteurZ != None):
            facteurZ = self.facteurZ.soustraire(otherEquation.facteurZ)
        else:
            facteurZ=None
        return Equation(result,facteurX,facteurY,facteurZ)
        
    def trouverY(self,x,z):
        result = self.result.soustraire(self.facteurX.multiplier(x))
        result = result.soustraire(self.facteurX.multiplier(z))
        result = result.diviser(self.facteurY)
        return result
    def trouverX(self,y,z):
        result = self.result.soustraire(self.facteurY.multiplier(y))
        result = result.soustraire(self.facteurZ.multiplier(z))
        result = result.diviser(self.facteurX)
        return result
    def trouverZ(self,x,y):
        result = self.result.soustraire(self.facteurX.multiplier(x))
        result = result.soustraire(self.facteurY.multiplier(y))
        result = result.diviser(self.facteurZ)
        return result