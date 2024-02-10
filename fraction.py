import Utils

class Fraction:
    def __init__(self,numerateur,denominateur=1):
        self.numerateur = numerateur
        self.denominateur = denominateur
    
    def value(self):
        return self.numerateur/self.denominateur
    def soustraire(self,otherFraction):
        if(self.denominateur==otherFraction.denominateur):
            frac1,frac2 = self,otherFraction
        else:
            frac1,frac2 = Utils.SurDenominateurCommun(self,otherFraction)
        return Fraction(frac1.numerateur-frac2.numerateur,frac1.denominateur)
    def additioner(self,otherFraction):
        if(self.denominateur==otherFraction.denominateur):
            frac1,frac2 = self,otherFraction
        else:
            frac1,frac2 = Utils.SurDenominateurCommun(self,otherFraction)
        return Fraction(frac1.numerateur+frac2.numerateur,frac1.denominateur)

    def multiplier(self,multiplier):
        if multiplier == None:
            return self
        if isinstance(multiplier,int) or isinstance(multiplier,float):
            multiplier = Fraction(multiplier)
        nouveaunumerateur = self.numerateur*multiplier.numerateur
        nouveaudenominateur = self.denominateur*multiplier.denominateur
        nouvellefraction = Fraction(nouveaunumerateur,nouveaudenominateur)
        return nouvellefraction.factoriser()
    def diviser(self,diviseur):
        if isinstance(diviseur,int):
            diviseur = Fraction(1,diviseur)
        return self.multiplier(Fraction(diviseur.denominateur,diviseur.numerateur))

    def texte(self):
        if(self.denominateur==1):
            return str(self.value())
        return "("+str(self.numerateur)+"/"+str(self.denominateur)+")"

    def factoriser(self):
        pgcd = Utils.PGCD(self.numerateur,self.denominateur)

        return Fraction(self.numerateur/pgcd,self.denominateur/pgcd)
    