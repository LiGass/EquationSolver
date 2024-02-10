import equation
import equationSystem

eq1 = equation.Equation(20,4,1)
eq2 = equation.Equation(70,10,5)
eq1.afficher()
eq2.afficher()
system = equationSystem.EquationSystem(eq1,eq2)
system.resoudre()