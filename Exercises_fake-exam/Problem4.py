if __name__=="__main__":
 print("Script is running directly")

#Use sympy to solve the equation d^2y(x)/dx^2 + 9y(x)+x=0 Check that it's correct (still using sympy). Hint: you can access the right hand side of solution expression with .rhs.

#Then set the constants equal to 1 and integrate the obtained function numerically using scipy over the interval [0,10] Hint: you can use symply's lambdify function to turn sympy's expression into a function you can use later for scipy.

import sympy as sp
y = sp.Function('y')
x = sp.symbols('x')
expr=sp.diff(y(x),x,2) + 9*y(x) +x
#Solving the equation:
ysolv = sp.dsolve(sp.Eq(expr,0))
ysolv=ysolv.rhs

#Set the constants equal to 1:
ysolv.subs('C1',1)
ysolv.subs('C2',1)
print(ysolv)
