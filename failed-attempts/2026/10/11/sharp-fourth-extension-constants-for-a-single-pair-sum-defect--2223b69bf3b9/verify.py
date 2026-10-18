from itertools import combinations
from fractions import Fraction


def gadd(z,w): return (z[0]+w[0], z[1]+w[1])
def gmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def gconj(z): return (z[0],-z[1])
def gabs2(z): return z[0]*z[0]+z[1]*z[1]

def defect_type(S,N):
    fibers={}
    for i,a in enumerate(S):
        for j in range(i,len(S)):
            b=S[j]
            fibers.setdefault((a+b)%N,[]).append((i,j))
    bad=[v for v in fibers.values() if len(v)>1]
    if len(bad)!=1 or len(bad[0])!=2 or any(len(v)>1 for v in fibers.values() if v is not bad[0]):
        return None
    p,q=bad[0]
    if p[0]==p[1] and q[0]!=q[1]: return ('M',p,q)
    if q[0]==q[1] and p[0]!=p[1]: return ('M',q,p)
    if p[0]!=p[1] and q[0]!=q[1]: return ('P',p,q)
    raise AssertionError('two diagonal collision in odd order')

def conv_energy(S,N,f):
    c={}
    for i,a in enumerate(S):
        for j,b in enumerate(S):
            s=(a+b)%N
            c[s]=gadd(c.get(s,(0,0)),gmul(f[i],f[j]))
    return sum(gabs2(z) for z in c.values())

def formula_energy(S,N,f,typ):
    x=[gabs2(z) for z in f]
    T=sum(x); Q=sum(v*v for v in x)
    A=2*T*T-Q
    kind,p,q=typ
    if kind=='P':
        z=gmul(gmul(f[p[0]],f[p[1]]), gconj(gmul(f[q[0]],f[q[1]])))
        A += 8*z[0]
    else:
        z=gmul(gmul(f[p[0]],f[p[0]]), gconj(gmul(f[q[0]],f[q[1]])))
        A += 4*z[0]
    return A

vectors=[[(1,0),(2,1),(-1,2),(3,-1),(1,-2),(2,0)],
         [(0,1),(1,-1),(2,2),(-2,1),(3,0),(-1,-2)]]
counts={'P':0,'M':0}; exact_checks=0
examples={}
for N in [5,7,9,11,13]:
    for m in range(3,min(6,N)+1):
        for S in combinations(range(N),m):
            typ=defect_type(S,N)
            if not typ: continue
            kind=typ[0]; counts[kind]+=1; examples.setdefault(kind,(N,S,typ))
            # In type P the two off-diagonal pairs must be disjoint.
            if kind=='P':
                _,p,q=typ
                assert len(set(p+q))==4
            for base in vectors:
                f=base[:m]
                assert conv_energy(S,N,f)==formula_energy(S,N,f,typ)
                exact_checks += 1

assert counts['P']>0 and counts['M']>0
# Exact scalar optimizations used by the proof.
u=Fraction(1,1)
assert Fraction(2,1)+u*u/Fraction(4,1)==Fraction(9,4)
xa,xb,xc=Fraction(3,7),Fraction(2,7),Fraction(2,7)
Fm=-(xa*xa+xb*xb+xc*xc)+4*xa*xb  # xb=xc, so sqrt(xb xc)=xb
assert Fm==Fraction(1,7)
assert Fraction(2,1)+Fm==Fraction(15,7)
# Strict localization check for all rational u-grid points below 1, for representative outside sizes.
for r in range(1,6):
    for k in range(0,100):
        u=Fraction(k,100)
        assert Fraction(2,1)+u*u/Fraction(4,1)-(1-u)*(1-u)/r < Fraction(9,4)
        assert Fraction(2,1)+u*u/Fraction(7,1)-(1-u)*(1-u)/r < Fraction(15,7)
print(f"VERIFY_OK P_sets={counts['P']} M_sets={counts['M']} exact_energy_checks={exact_checks} cyclic_orders=5,7,9,11,13")
