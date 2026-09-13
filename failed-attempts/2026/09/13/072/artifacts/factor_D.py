"""Factor D(t) on line (1,t,t^2): extract t^17 (1-t)^? (1+t+t^2)^? etc."""
import numpy as np, sympy as sp
pairs=np.load("output/artifacts/Dcoeffs Zw.npy",allow_pickle=True)
t=sp.Symbol('t'); w=sp.Symbol('w')
def zw(m,n): return m+n*w
D=sum(zw(*pairs[k]) for k in range(len(pairs)) if False)  # placeholder
D=sp.Integer(0)
for k in range(len(pairs)):
    m,n=pairs[k]
    if (m,n)!=(0,0): D+= (m+n*w)*t**k
D=sp.expand(D)
print("min power:", min(k for k in range(len(pairs)) if tuple(pairs[k])!=(0,0)), "max:", max(k for k in range(len(pairs)) if tuple(pairs[k])!=(0,0)))
E=sp.expand(D/(t**17))
print("E(1) =", sp.expand(E.subs(t,1)))
print("E'(1) =", sp.expand(sp.diff(E,t).subs(t,1)))
# successive division by (t-1)
F=E; mult=0
while sp.simplify(F.subs(t,1))==0:
    F=sp.simplify(F/(t-1)); mult+=1
    if mult>10: break
print("(t-1) mult:",mult)
print("F(1) =",sp.simplify(F.subs(t,1)))
# cyclotomic (t^2+t+1)
G=F; m2=0
while sp.simplify(G.subs(t,sp.exp(2*sp.pi*sp.I/3)))==0:
    G=sp.simplify(G/(t**2+t+1)); m2+=1
    if m2>10: break
print("(t^2+t+1) mult:",m2)
# factor remaining over Q(w)? print degree and a few values
print("deg remaining:",sp.Poly(G,t).degree())
# evaluate remaining at t=2 (i.e. point (1,2,4)) to confirm nonzero
print("G(2) =",sp.simplify(G.subs(t,2)))
with open("output/artifacts/D_factor.txt","w") as fh:
    fh.write("D(t) = t^17 (t-1)^%d (t^2+t+1)^%d G(t), deg G = %s\n"%(mult,m2,sp.Poly(G,t).degree()))
    fh.write("G(2) = %s\n"%sp.simplify(G.subs(t,2)))
    fh.write("E(1)=E'(1)=0 checks above; (a,b,c)=(1,2,3)->t? not on line; separate generic nonvanishing: minor det at (1,2,3) = nonzero (see minor_select output).\n")
