"""Rank-3 cyclic test: L=Z^3, omega = cyclic quiver adjacency (e1->e2->e3->e1).
omega(e1,e2)=1, omega(e2,e3)=1, omega(e3,e1)=1 (antisym). Initial walls F_i=E(-z^{e_i}).
Solve for outgoing q_v at low degrees via ordered loop product.
Order of walls around S^2 loop: use generic loop crossing F1,F2,F3 then outgoing walls grouped.
Simplification: work in degree-truncated algebra; unknown q_v solved triangularly by degree.
Loop order: take path gamma crossing: F1, F2, F3, then all outgoing in reverse angular order.
For low degrees only (1,1,0),(1,0,1),(0,1,1),(1,1,1) matter. Angular order of rays in a transverse
2-plane section: test consistency defect with one representative loop ordering and solve.
This is heuristic for the decision gate; exact order only affects signs which we fix by residual check.
"""
import sys; sys.path.insert(0,'output/artifacts')
import itertools
import sympy as sp
t=sp.Symbol('t')
# omega matrix
W={(0,1):1,(1,2):1,(2,0):1}
def om(a,b):
    s=0
    for i in range(3):
        for j in range(3):
            wij=W.get((i,j),0)-W.get((j,i),0)
            s+=a[i]*b[j]*wij
    return s
def add3(a,b): return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def mul(F,G,N):
    H={}
    for a,ca in F.items():
        for b,cb in G.items():
            c=(a[0]+b[0],a[1]+b[1],a[2]+b[2])
            if sum(c)<=N:
                H[c]=sp.simplify(H.get(c,0)+ca*cb*t**om(a,b))
    return H
def sinv(F,N):
    H={(0,0,0):sp.Integer(1)}
    keys=[k for k in itertools.product(range(N+1),repeat=3) if 0<sum(k)<=N]
    keys.sort(key=sum)
    for m in keys:
        s=0
        for a0 in range(m[0]+1):
         for a1 in range(m[1]+1):
          for a2 in range(m[2]+1):
           a=(a0,a1,a2)
           b=(m[0]-a0,m[1]-a1,m[2]-a2)
           if b==m: continue
           ca=F.get(a,0); cb=H.get(b,0)
           if ca!=0 and cb!=0: s+=ca*cb*t**om(a,b)
        H[m]=sp.simplify(-s)
    return {k:v for k,v in H.items() if sp.simplify(v)!=0}
from qscat import E_series
def E3(p,v,N):
    # p dict shift->int; reduce to rank-2 solver by mapping? Instead build directly with om above.
    # log coeffs as in qscat but with vector multiples
    from qscat import E_log_coeffs
    tot=sum(v); M=N//tot
    X={}
    for j,c in p.items():
        if c==0: continue
        Xj=E_log_coeffs(j,tot,M)
        for m,cc in Xj.items(): X[m]=sp.simplify(X.get(m,0)+c*cc)
    Xc={m:sp.simplify(X.get(m,0)) for m in range(1,M+1)}
    Fm={0:sp.Integer(1)}
    for m in range(1,M+1):
        s=0
        for k in range(1,m+1): s+=k*Xc.get(k,0)*Fm.get(m-k,0)
        Fm[m]=sp.simplify(s/m)
    F={(0,0,0):sp.Integer(1)}
    for m in range(1,M+1): F[(m*v[0],m*v[1],m*v[2])]=sp.simplify(Fm[m])
    return F
N=3
e1=(1,0,0);e2=(0,1,0);e3=(0,0,1)
F1=E3({0:1},e1,N);F2=E3({0:1},e2,N);F3=E3({0:1},e3,N)
F1i=sinv(F1,N);F2i=sinv(F2,N);F3i=sinv(F3,N)
# unknowns at deg2: (1,1,0),(1,0,1),(0,1,1); deg3: (1,1,1) + permutations of deg3 with a zero
deg2=[(1,1,0),(1,0,1),(0,1,1)]
# loop order heuristic: ...F3 F2 F1 then outgoing...; solve each q from defect of product P=F3*F2*F1*F1i*F2i*F3i with unknowns inserted adjacent.
# Simpler: P = G * F3*F2*F1 * F1i*F2i*F3i where G = product of unknown walls in fixed order.
# Solve triangularly: at deg d, P_d defect gives q (single wall per degree-2 ray).
order=deg2+[(1,1,1),(2,1,0),(1,2,0),(2,0,1),(1,0,2),(0,2,1),(0,1,2)]
Ess={}
Q={}
for v in order:
    if sum(v)>N: continue
    G={(0,0,0):sp.Integer(1)}
    for w,S in Ess.items(): G=mul(G,S,N)  # order among knowns fixed; fine at these degrees (they commute to this order? checked by residual)
    P=dict(F1i); P=mul(dict(F2i),P,N); P=mul(dict(F3i),P,N)
    P=mul(dict(F1),P,N); P=mul(dict(F2),P,N); P=mul(dict(F3),P,N)
    P=mul(G,P,N)
    D=sp.simplify(P.get(v,0))
    qv=sp.simplify(-(t-t**(-1))*D)
    print(v,"defect P=",sp.together(D),"qv=",sp.together(qv),flush=True)
    Q[v]=qv
print("done heuristic")
