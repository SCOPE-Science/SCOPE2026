import numpy as np, sympy as sp
def inv(d): return d+5 if d<5 else d-5
def neg(w): return tuple(inv(d) for d in reversed(w))
def red(w):
    st=[]
    for d in w:
        if st and st[-1]==inv(d): st.pop()
        else: st.append(d)
    return tuple(st)
def show(d): return ('a' if d<5 else 'A')+str((d%5)+1)
def showw(w): return ''.join(show(d) for d in w)
def apply(f,w):
    out=[]
    for d in w:
        out.extend(f[d] if d<5 else neg(f[d-5]))
    return red(tuple(out))
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2)}
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1)}
# f = th' o sig; f^{-1} = sig^{-1} o th'^{-1}; th'^{-1}(a1)=a1 A3 A2 (phi)
# sig^{-1}(a1 A3 A2) = a5 A2 A1 ; for psi th'^{-1}(a1)=a1 A2 A3 -> sig^{-1} = a5 A1 A2
g_phi={0:(4,6,5),1:(0,),2:(1,),3:(2,),4:(3,)}
g_psi={0:(4,5,6),1:(0,),2:(1,),3:(2,),4:(3,)}
for f,g,nm in [(f_phi,g_phi,'phi'),(f_psi,g_psi,'psi')]:
    ok=all(apply(g,apply(f,(i,)))==(i,) and apply(f,apply(g,(i,)))==(i,) for i in range(5))
    ok2=all(apply(g,apply(f,(i+5,)))==(i+5,) for i in range(5))
    print(nm,'automorphism:',ok and ok2)
    for i in range(5): print(' ',show(i),'->inv->',showw(g[i]))
