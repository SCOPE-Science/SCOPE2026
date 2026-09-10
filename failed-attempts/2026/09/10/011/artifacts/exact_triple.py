"""EXACT (rational) effectivity test for m4=0 invariant classes B=dH-m3E3.
All data over Q: Phi4=x^3y+y^3z+z^3x, Phi6=xy^5+yz^5+zx^5-5x^2y^2z^2 (paper Sec 2.4),
Phi14=BH(Phi4,Phi6)/9 with BH bordered Hessian. Triple rep point q=[1:1:1].
Taylor conditions at q (affine z=1): exact integer linear algebra.
"""
from fractions import Fraction as F
from itertools import product

# poly as dict {(i,j,k):F}
def padd(a,b): return {e:a.get(e,F(0))+b.get(e,F(0)) for e in set(a)|set(b)}
def pmul(a,b):
    c={}
    for e1,v1 in a.items():
        for e2,v2 in b.items():
            e=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2])
            c[e]=c.get(e,F(0))+v1*v2
    return {e:v for e,v in c.items() if v!=0}
def ppow(a,n):
    r={(0,0,0):F(1)}
    for _ in range(n): r=pmul(r,a)
    return r
def pdiff(p,var):
    q={}
    for (i,j,k),v in p.items():
        if var==0 and i>0: q[(i-1,j,k)]=q.get((i-1,j,k),F(0))+v*i
        if var==1 and j>0: q[(i,j-1,k)]=q.get((i,j-1,k),F(0))+v*j
        if var==2 and k>0: q[(i,j,k-1)]=q.get((i,j,k-1),F(0))+v*k
    return q
def peval(p,pt):
    return sum(v*(pt[0]**e[0])*(pt[1]**e[1])*(pt[2]**e[2]) for e,v in p.items())

x={(1,0,0):F(1)}; y={(0,1,0):F(1)}; z={(0,0,1):F(1)}
def pw(n,e):
    r={(0,0,0):F(1)}
    base={e:F(1)}
    for _ in range(n): r=pmul(r,base)
    return r
Phi4=padd(padd(pmul(pw(3,(1,0,0)),{(0,1,0):F(1)}),pmul(pw(3,(0,1,0)),{(0,0,1):F(1)})),pmul(pw(3,(0,0,1)),{(1,0,0):F(1)}))
# Phi6 explicit
t1=pmul({(1,0,0):F(1)},pw(5,(0,1,0))); t2=pmul({(0,1,0):F(1)},pw(5,(0,0,1))); t3=pmul({(0,0,1):F(1)},pw(5,(1,0,0)))
t4={(2,2,2):F(-5)}
Phi6=padd(padd(t1,t2),padd(t3,t4))
# bordered Hessian -> Phi14 = det/9
H=[[pdiff(pdiff(Phi4,a),b) for b in range(3)] for a in range(3)]
G6=[pdiff(Phi6,a) for a in range(3)]
# 4x4 det via expansion (exact)
import itertools
M4=[[None]*4 for _ in range(4)]
for a in range(3):
    for b in range(3): M4[a][b]=H[a][b]
    M4[a][3]=G6[a]; M4[3][a]=G6[a]
M4[3][3]={(0,0,0):F(0)}
def pdet(M):
    n=len(M); tot={}
    for sgn in itertools.permutations(range(n)):
        # sign
        inv=sum(1 for a in range(n) for b in range(a+1,n) if sgn[a]>sgn[b])
        s=F(-1) if inv%2 else F(1)
        term={(0,0,0):s}
        for a in range(n): term=pmul(term,M[a][sgn[a]])
        tot=padd(tot,term)
    return tot
BH=pdet(M4)
Phi14={e:v/F(9) for e,v in BH.items() if v!=0}
def deg(p): return max(sum(e) for e in p)
print("deg Phi4,Phi6,Phi14:",deg(Phi4),deg(Phi6),deg(Phi14))
print("Phi4(q):",peval(Phi4,((1,1,1))), " Phi6(q):",peval(Phi6,((1,1,1))), " Phi14(q):",peval(Phi14,((1,1,1))))
# dehomogenize z=1 -> poly in u=x-1,v=y-1: substitute x=u+1 etc. Taylor coeff of u^i v^j
def jet_rows(poly2d, m):
    # poly2d dict {(i,j):F} in (x,y) affine; shift x=1+u,y=1+v: coeff of u^a v^b = sum_{i>=a,j>=b} c(i,j) C(i,a) C(j,b)
    from math import comb
    rows=[]
    for a in range(m):
        for b in range(m-a):
            rows.append({(a,b):1})  # placeholder
    # build matrix rows directly
    R=[]
    for a in range(m):
        for b in range(m-a):
            R.append((a,b))
    return R
def affshift(poly):
    # z=1: q={(i,j):v}
    q={}
    for (i,j,k),v in poly.items(): q[(i,j)]=q.get((i,j),F(0))+v
    # shift: coeff u^a v^b
    from math import comb
    r={}
    for (i,j),v in q.items():
        for a in range(i+1):
            for b in range(j+1):
                r[(a,b)]=r.get((a,b),F(0))+v*comb(i,a)*comb(j,b)
    return r
A4=affshift(Phi4); A6=affshift(Phi6); A14=affshift(Phi14)
def affmul(a,b):
    c={}
    for e1,v1 in a.items():
        for e2,v2 in b.items():
            e=(e1[0]+e2[0],e1[1]+e2[1]); c[e]=c.get(e,F(0))+v1*v2
    return c
def affpow(a,n):
    r={(0,0):F(1)}
    for _ in range(n): r=affmul(r,a)
    return r
def basis(d):
    out=[]
    a=0
    while 4*a<=d:
        b=0
        while 4*a+6*b<=d:
            r=d-4*a-6*b
            if r%14==0: out.append((a,b,r//14))
            b+=1
        a+=1
    return out
def rank_exact(rows):
    M=[list(r) for r in rows]
    if not M: return 0
    nr,nc=len(M),len(M[0])
    rk=0; rr=0
    for c in range(nc):
        piv=None
        for r in range(rr,nr):
            if M[r][c]!=0: piv=r;break
        if piv is None: continue
        M[rr],M[piv]=M[piv],M[rr]
        inv=M[rr][c]
        M[rr]=[v/inv for v in M[rr]]
        for r in range(nr):
            if r!=rr and M[r][c]!=0:
                f=M[r][c]; M[r]=[rv-f*qv for rv,qv in zip(M[r],M[rr])]
        rr+=1; rk+=1
    return rk
print(f"{'d':>4} {'m3':>3} {'dimT':>4} {'ncond(raw)':>9} {'rank':>4} {'actual':>6} edim")
for d,m3 in [(10,2),(20,4),(30,6),(40,8),(60,0+12),(42,8),(18,0),(28,5),(56,10)]:
    bas=basis(d); n=len(bas)
    polys=[affmul(affmul(affpow(A4,a),affpow(A6,b)),affpow(A14,c)) for (a,b,c) in bas]
    ders=[(a,b) for s in range(m3) for a in range(s+1) for bb in [s-a] for b in [bb]]
    rows=[[p.get(dd,F(0)) for p in polys] for dd in ders]
    # transpose to row-per-condition? rank same
    rk=rank_exact(rows)
    from math import floor
    # cond_3(m3)
    cn=sum((m3-1-3*j)//2+1 for j in range((m3-1)//3+1)) if m3>0 else 0
    e=max(n-cn,0)
    print(f"{d:>4} {m3:>3} {n:>4} {len(ders):>9} {rk:>4} {n-rk:>6} {e}")
print("EXACT_TRIPLE_OK")
