import fraction
def PGCD(a:int,b:int):
    if b != 0: 
        return PGCD(b,a % b)
    else: 
        return a
        
def PPMC(a:int,b:int):
    return (a*b)/PGCD(a,b)
def PPMC(a,b):
    num = (a.numerateur*b.numerateur)/PGCD(a.numerateur,b.numerateur)
    den = (a.denominateur*b.denominateur)/PGCD(a.denominateur,b.denominateur)
    return fraction.Fraction(num,den)

def SurDenominateurCommun(frac1,frac2):
    ppmc = PPMC(frac1.denominateur,frac2.denominateur)
    if ppmc > frac1.denominateur:
        mult1 = ppmc.diviser(frac1)
    else:
        mult1 = frac1.diviser(ppmc)
    if ppmc > frac1.denominateur:
        mult2 = ppmc.diviser(frac2)
    else:
        mult2 = frac2.diviser(ppmc)
    frac1 = frac1.multiplier(mult1)
    frac2 = frac2.multiplier(mult2)
    return frac1,frac2
    