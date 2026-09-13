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
# corrected inverses: f^{-1} = sig^{-1} th^{-1}, th^{-1}(a1)=a1 A3 A2 (phi)
g_phi={0:(4,7,6),1:(0,),2:(1,),3:(2,),4:(3,)}
g_psi={0:(4,6,7),1:(0,),2:(1,),3:(2,),4:(3,)}
for f,g,nm in [(f_phi,g_phi,'phi'),(f_psi,g_psi,'psi')]:
    ok=all(apply(g,apply(f,(i,)))==(i,) and apply(f,apply(g,(i,)))==(i,) for i in range(5))
    # also verify g maps are homomorphisms inverses on inverses
    ok2=all(apply(g,apply(f,(i+5,)))==(i+5,) for i in range(5))
    print(nm,'automorphism:',ok and ok2)
M=[[0,0,0,0,1],[1,0,0,0,1],[0,1,0,0,1],[0,0,1,0,0],[0,0,0,1,0]]
Mn=np.array(M)
for k in range(1,21):
    if bool(((np.linalg.matrix_power(Mn,k))>0).all()):
        print('primitive: M^%d > 0'%k); break
else: print('NOT primitive up to 20')
print('charpoly:', sp.Matrix(M).charpoly(sp.symbols('x')).as_expr())
print('PF eig:', max(abs(e) for e in np.linalg.eigvals(Mn)))
