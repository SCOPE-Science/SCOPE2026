"""Substep 7: Nielsen-path / PNP brute-force bounded check (independent of gate argument)."""
def inv(d): return d+5 if d<5 else d-5
def neg(w): return tuple(inv(d) for d in reversed(w))
def red(w):
    st=[]
    for d in w:
        if st and st[-1]==inv(d): st.pop()
        else: st.append(d)
    return tuple(st)
def showw(w): return ''.join(('a' if d<5 else 'A')+str((d%5)+1) for d in w)
def apply(f,w):
    out=[]
    for d in w:
        out.extend(f[d] if d<5 else neg(f[d-5]))
    return red(tuple(out))
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2)}
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1)}
from itertools import product
def brute(f,nm):
    # all reduced edge-paths of length<=4 through vertex; check f^5(rho) ~ rho rel endpoints
    cnt=0
    for L in range(1,5):
        for w in product(range(10),repeat=L):
            if any(w[i+1]==inv(w[i]) for i in range(L-1)): continue
            rho=tuple(w); img=rho
            for k in range(5): img=apply(f,img)
            if img==rho: print(nm,'FIXED PATH len',L,showw(rho)); cnt+=1
    print(nm,'fixed-by-f^5 paths len<=4:',cnt)
brute(f_phi,'phi'); brute(f_psi,'psi')
