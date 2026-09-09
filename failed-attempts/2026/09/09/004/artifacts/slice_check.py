# Slice obstruction audit for family w_m: Fox-Milnor (Delta must factor as f(t)f(t^-1)) + signature bound via Seifert matrix from braid word (standard algorithm) + det.
import sys; sys.path.insert(0,'output/artifacts')
import sympy as sp
t=sp.Symbol('t')
w0=[1,1,1,-2,-1,-1,-1,-2]
# factor check over ZZ: attempt f*f^rev with deg m+2? and f(1)=+-1
def Dpoly(m):
    from burau import alexander
    w=w0[:4]+[-1]*(2*m)+w0[4:]
    return sp.expand(alexander(w,3))
for m in range(5):
    d=Dpoly(m)
    e=sp.expand(d*t**{0:2,1:4,2:6,3:8,4:10}[m])
    print(f"m={m} D*t^k={e} D(1)={d.subs(t,1)} det={abs(complex(d.subs(t,-1)))}")
    print("  factor:", sp.factor(e))
