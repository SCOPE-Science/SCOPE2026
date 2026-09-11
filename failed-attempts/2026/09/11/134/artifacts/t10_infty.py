import sympy as sp
X0,X1,Y0,Y1,t=sp.symbols('X0 X1 Y0 Y1 t')
F=-t*X0**2*Y0**2-t*X0*X1*Y0**2-t*X0*X1*Y1**2-t*X1**2*Y0*Y1+X0*X1*Y0*Y1
# Chart X1=0 (x=inf), X0=1: F| = -t*Y0**2
print("F(1,0,Y)=",sp.expand(F.subs({X0:1,X1:0})))
# zeros require Y0=0 => point ([1:0],[0:1]); check gradient there
dF=[sp.diff(F,v) for v in (X0,X1,Y0,Y1)]
print("grad at (1,0,0,1):",[sp.expand(g).subs({X0:1,X1:0,Y0:0,Y1:1}) for g in dF])
# Chart Y1=0 (y=inf), Y0=1: F| = -t*X0**2-t*X0*X1
print("F(X,1,0)=",sp.expand(F.subs({Y0:1,Y1:0})))
# zeros: -t*X0*(X0+X1)=0 => [0:1] or [1:-1]; gradients
print("grad at (0,1,1,0):",[sp.expand(g).subs({X0:0,X1:1,Y0:1,Y1:0}) for g in dF])
print("grad at (1,-1,1,0):",[sp.expand(g).subs({X0:1,X1:-1,Y0:1,Y1:0}) for g in dF])
# corner ([1:0],[1:0])
print("grad at (1,0,1,0):",[sp.expand(g).subs({X0:1,X1:0,Y0:1,Y1:0}) for g in dF])
print("F at corner:",sp.expand(F).subs({X0:1,X1:0,Y0:1,Y1:0}))
