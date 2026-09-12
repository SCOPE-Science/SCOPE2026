"""Lane-1229 certificate, fixed Tietze substitution."""
from math import gcd
from fractions import Fraction

def red(w):
    st=[]
    for g,e in w:
        if st and st[-1][0]==g and st[-1][1]==-e: st.pop()
        else: st.append((g,e))
    return st
def mul(*ws):
    out=[]
    for w in ws: out.extend(w)
    return red(out)
def inv(w): return [(g,-e) for (g,e) in reversed(w)]
def wstr(w):
    d={(0,1):'x0',(1,1):'x1',(2,1):'x2',(0,-1):'X0',(1,-1):'X1',(2,-1):'X2'}
    return ''.join(d[t] for t in w) or '1'

s1={0:[(0,1),(1,1),(0,-1)],1:[(0,1)],2:[(2,1)]}
s2={0:[(0,1)],1:[(1,1),(2,1),(1,-1)],2:[(1,1)]}
s1i={0:[(1,1)],1:[(1,-1),(0,1),(1,1)],2:[(2,1)]}
s2i={0:[(0,1)],1:[(2,1)],2:[(2,-1),(1,1),(2,1)]}
def apply(auto,w):
    out=[]
    for g,e in w:
        out.extend(auto[g] if e==1 else inv(auto[g]))
    return red(out)
def compose(A,B): return {g: apply(A,B[g]) for g in (0,1,2)}
def is_id(a): return all(red(a[g])==[(g,1)] for g in (0,1,2))
print("A1 s1*s1i=id:",is_id(compose(s1,s1i))," s1i*s1=id:",is_id(compose(s1i,s1)))
print("A2 s2*s2i=id:",is_id(compose(s2,s2i))," s2i*s2=id:",is_id(compose(s2i,s2)))
L=compose(compose(s1,s2),s1); Rr=compose(compose(s2,s1),s2)
print("A3 braid s1s2s1=s2s1s2 in Aut(F3):",all(red(L[g])==red(Rr[g]) for g in (0,1,2)))
def pmul(p,q): return tuple(p[q[i]] for i in range(3))
P={'s1':(1,0,2),'s2':(0,2,1),'s1i':(1,0,2),'s2i':(0,2,1)}
bp=(0,1,2)
for g in ['s1','s2i','s1','s2i']: bp=pmul(P[g],bp)
print("B1 closure permutation:",bp,"knot(3-cycle):",bp in [(1,2,0),(2,0,1)])
beta={0:[(0,1)],1:[(1,1)],2:[(2,1)]}
for g in ['s1','s2i','s1','s2i']:
    beta=compose({'s1':s1,'s2':s2,'s1i':s1i,'s2i':s2i}[g],beta)
rels=[mul(beta[g],[(g,-1)]) for g in (0,1,2)]
for i,r in enumerate(rels): print(f"B2 r{i}={wstr(r)} len={len(r)}")
print("B3 writhe=",0,"(<=4 crossings => crossing number <=4)")
# Tietze: r1 = x0 x2 X0 X1 = 1. So x1 = x0 x2 X0, X1 = X0 x2 X0... verify carefully:
# r1 = x0 x2 X0 X1 = 1  =>  X1 = X0 X2 x0,  x1 = x0 x2 X0.
x1s=[(0,1),(2,1),(0,-1)]
X1s=inv(x1s)
print("C1 check r1==x0 x2 X0 X1:", wstr(mul([(0,1)],[(2,1)],[(0,-1)],[(1,-1)]))==wstr(rels[1]))
print("C1 subst: x1=",wstr(x1s)," X1=",wstr(X1s))
print("C1 r1 with subst:",wstr(mul([(0,1)],[(2,1)],[(0,-1)],X1s)))
def subst(w):
    out=[]
    for g,e in w:
        if g==1: out.extend(x1s if e==1 else X1s)
        else: out.append((g,e))
    return red(out)
print("C1 r1-subst empty:", subst(rels[1])==[])
s0=subst(rels[0]); s2=subst(rels[2])
print("C2 s0=",wstr(s0),"len=",len(s0))
print("C3 s2=",wstr(s2),"len=",len(s2))
def expsum2(w): return (sum(e for g,e in w if g==0),sum(e for g,e in w if g==2))
print("C4 expsum rows:",expsum2(s0),expsum2(s2))
def fox(w,gen):
    d={}; tot=0
    for (g,e) in w:
        if g==gen:
            if e==1: d[tot]=d.get(tot,0)+1
            else: d[tot-1]=d.get(tot-1,0)-1
        tot+=e
    return {k:v for k,v in d.items() if v!=0}
def lstr(p):
    if not p: return "0"
    return "+".join(f"{v}t^{k}" for k,v in sorted(p.items()))
u0=fox(s0,0); u2=fox(s2,0)
print("D1 d(s0)/dx0 =",lstr(u0))
print("D2 d(s2)/dx0 =",lstr(u2))
def to_poly(p):
    m=min(p.keys()); return [Fraction(p.get(m+i,0)) for i in range(max(p.keys())-m+1)]
def strip(c):
    c=list(c)
    while len(c)>1 and c[-1]==0: c.pop()
    return c
def pdivmod(a,b):
    a=list(a); da=len(a)-1; db=len(b)-1
    if da<db: return ([Fraction(0)],a)
    q=[Fraction(0)]*(da-db+1); lc=b[-1]
    while len(a)-1>=db and not (len(a)==1 and a[0]==0):
        c=a[-1]/lc; k=len(a)-1-db; q[k]=c
        for i in range(db+1): a[k+i]-=c*b[i]
        a=strip(a)
    return (q,a)
def pgcd(a,b):
    a=strip(a); b=strip(b)
    while not (len(b)==1 and b[0]==0):
        _,r=pdivmod(a,b); a=b; b=r
    return a
G=pgcd(to_poly(u0),to_poly(u2)); Gmonic=[g/G[-1] for g in G]
print("D3 gcd (monic) =",[str(g) for g in Gmonic],"degree",len(Gmonic)-1)
print("D4 equals t^2-3t+1:", [Fraction(g) for g in Gmonic]==[Fraction(1),Fraction(-3),Fraction(1)])
def bareiss(A):
    n=len(A)
    if n==0: return 1
    M=[row[:] for row in A]; prev=1
    for k in range(n-1):
        if M[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if M[i][k]!=0: piv=i; break
            if piv is None: return 0
            M[k],M[piv]=M[piv],M[k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
            M[i][k]=0
        prev=M[k][k]
    return M[n-1][n-1]
import itertools
def minors_gcd(M,k):
    m=len(M); n=len(M[0]); g=0
    for rs in itertools.combinations(range(m),k):
        for cs in itertools.combinations(range(n),k):
            g=gcd(g,bareiss([[M[i][j] for j in cs] for i in rs]))
    return abs(g)
def snf(M):
    m=len(M); n=len(M[0]); r=0
    for k in range(1,min(m,n)+1):
        if minors_gcd(M,k)!=0: r=k
    ds=[minors_gcd(M,k) for k in range(1,r+1)]
    iv=[ds[0]]+[ds[i]//ds[i-1] for i in range(1,len(ds))]
    return r,iv
def expsum3(w): return [sum(e for g,e in w if g==j) for j in (0,1,2)]
Rm=[expsum3(r) for r in rels]
print("E1 abelian relation matrix:",Rm)
rk,iv=snf(Rm); print(f"E2 H1(complement): rank={3-rk} inv={iv} => {'Z' if (3-rk==1 and all(v==1 for v in iv)) else 'UNEXPECTED'}")
Rf=Rm+[[1,0,0]]
rk2,iv2=snf(Rf); print(f"E3 H1(+1 filling): free={3-rk2} inv={iv2} => {'0 INTEGRAL HOMOLOGY SPHERE' if (3-rk2==0 and all(v==1 for v in iv2)) else 'UNEXPECTED'}")
print("CERTIFICATE COMPLETE")
