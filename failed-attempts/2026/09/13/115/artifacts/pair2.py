import numpy as np, sympy as sp, json
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
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2,3,0)}
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1,3,0)}
def mat(f):
    M=[[0]*5 for _ in range(5)]
    for j in range(5):
        for d in f[j]: M[d%5][j]+=1
    return M
print('same M:', mat(f_phi)==mat(f_psi))
M=mat(f_phi)
for r in M: print(r)
Mn=np.array(M)
for k in range(1,21):
    if bool(((np.linalg.matrix_power(Mn,k))>0).all()):
        print('primitive: M^%d>0'%k); break
x=sp.symbols('x'); print('charpoly:', sp.Matrix(M).charpoly(x).as_expr())
print('det:', sp.Matrix(M).det())
print('PF eig:', max(abs(e) for e in np.linalg.eigvals(Mn.astype(float))))
# automorphism check: both are th o cyc; cyc order 5, th adjusts only a1... recompute inverse via Nielsen: f = L o sig where L(a1)=a1 u (u fixed by nothing). Use generic inverse finder: L^{-1}(a1)=a1 U^{-1}; for phi U=a2a3a4a1 -> L^{-1}(a1)=a1 A1A4A3A2; then f^{-1}=sig^{-1} L^{-1}
U_phi=neg((1,2,3,0)); U_psi=neg((2,1,3,0))  # U^{-1} as direction words
print('U_phi^-1:',showw(U_phi),' U_psi^-1:',showw(U_psi))
Linv_phi={0:(0,)+U_phi,1:(1,),2:(2,),3:(3,),4:(4,)}
Linv_psi={0:(0,)+U_psi,1:(1,),2:(2,),3:(3,),4:(4,)}
def comp(g,h):  # g o h on single directions
    return {d:apply(g,apply(h,(d,))) for d in range(5)}
# sig^{-1}: a1->a5,a2->a1,a3->a2,a4->a3,a5->a4
sinv={0:(4,),1:(0,),2:(1,),3:(2,),4:(3,)}
g_phi=comp(sinv,Linv_phi); g_psi=comp(sinv,Linv_psi)
for f,g,nm in [(f_phi,g_phi,'phi'),(f_psi,g_psi,'psi')]:
    ok=all(apply(g,apply(f,(i,)))==(i,) and apply(f,apply(g,(i,)))==(i,) for i in range(5))
    ok2=all(apply(g,apply(f,(i+5,)))==(i+5,) for i in range(5))
    print(nm,'automorphism:',ok and ok2)
    if ok: print('  g(a1)=',showw(g[0]))
# Df on all 10 directions
def Df(f,d): return f[d][0] if d<5 else neg(f[d-5])[-1]
for f,nm in [(f_phi,'phi'),(f_psi,'psi')]:
    imgs=[Df(f,d) for d in range(10)]
    print(nm,'Df imgs:',[show(d) for d in imgs],'bijective:',len(set(imgs))==10)
