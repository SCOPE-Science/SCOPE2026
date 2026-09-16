"""FINAL verified su(3)_2 computation: Kac-Walton fusion (exact) + Kac-Peterson S (exact prefactor).
Two independent routes agree: Verlinde(S) == Kac-Walton Q. Asserts: MF, twists, no bosons."""
from collections import defaultdict, deque
from fractions import Fraction as F
import mpmath as mp

WTS=[(0,0),(1,0),(0,1),(2,0),(0,2),(1,1)]
names=['1','X','Xb','g','gb','Y']

# ---- exact classical diagrams via Kostant (verified dims) ----
def pfunc(beta):
    n=0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if (2*i-j+k,-i+2*j+k)==beta: n+=1
    return n
def gen_weyl():
    s1=lambda q:(-q[0],q[0]+q[1]); s2=lambda q:(q[0]+q[1],-q[1])
    els={((1,0),(0,1)):1}; dq=deque([((1,0),(0,1))])
    while dq:
        m=dq.popleft()
        for g,dg in [(s1,-1),(s2,-1)]:
            h=(g(m[0]),g(m[1]))
            if h not in els: els[h]=els[m]*dg; dq.append(h)
    out=[]
    for (e1,e2),d in els.items():
        out.append((lambda p,e1=e1,e2=e2:(e1[0]*p[0]+e2[0]*p[1],e1[1]*p[0]+e2[1]*p[1]),d))
    assert len(out)==6
    return out
W=gen_weyl()
def WDof(lam):
    out={}
    for x in range(-6,7):
        for y in range(-6,7):
            mu=(x,y); mpr=(mu[0]+1,mu[1]+1); s=0
            for act,d in W:
                wlp=act((lam[0]+1,lam[1]+1))
                beta=(wlp[0]-mpr[0],wlp[1]-mpr[1])
                if (2*beta[0]+beta[1])%3 or (beta[0]+2*beta[1])%3: continue
                m_=(2*beta[0]+beta[1])//3; n_=(beta[0]+2*beta[1])//3
                if m_>=0 and n_>=0: s+= d*pfunc(beta)
            if s: out[mu]=s
    assert sum(out.values())==(lam[0]+1)*(lam[1]+1)*(lam[0]+lam[1]+2)//2,(lam,out)
    return out
WD={lam:WDof(lam) for lam in WTS}
def tensor(mu,nu):
    tot=defaultdict(int)
    for w1,m1 in WDof(mu).items():
        for w2,m2 in WDof(nu).items():
            tot[(w1[0]+w2[0],w1[1]+w2[1])]+=m1*m2
    rem=dict(tot); dec={}
    while any(v>0 for v in rem.values()):
        cands=sorted([k for k,v in rem.items() if v>0],key=lambda k:(k[0]+k[1],k[0]),reverse=True)
        top=next(c for c in cands if c[0]>=0 and c[1]>=0)
        m=rem[top]; dec[top]=dec.get(top,0)+m
        for w,c_ in WDof(top).items(): rem[w]=rem.get(w,0)-m*c_
    return dec
def reduce_alcove(lam):
    a,b=lam[0]+1,lam[1]+1
    T=[(5*m,5*n) for m in range(-2,3) for n in range(-2,3) if (m+2*n)%3==0 and (2*m+n)%3==0]
    sols=[]
    for act,d in W:
        q=act((a,b))
        for t in T:
            r=(q[0]+t[0],q[1]+t[1])
            if r[0]>=1 and r[1]>=1 and r[0]+r[1]<=4: sols.append(((r[0]-1,r[1]-1),d))
    if not sols:
        return None  # orbit hits alcove wall <=> quantum dimension 0 (e.g. (3,0),(2,1): verified qdim=0)
    assert len(set(sols))==1,(lam,sols)
    return sols[0]
Q={}
for i,mu in enumerate(WTS):
    for j,nu in enumerate(WTS):
        if j<i: continue
        acc=defaultdict(int)
        for lam,c in tensor(mu,nu).items():
            r=reduce_alcove(lam)
            if r is None: continue
            acc[WTS.index(r[0])]+=r[1]*c
        assert all(v>=0 for v in acc.values()),(i,j,dict(acc))
        Q[(i,j)]=dict(acc)
N3={}
for i in range(6):
    for j in range(6):
        a,b=(i,j) if i<=j else (j,i)
        for k in range(6): N3[(i,j,k)]=Q[(a,b)].get(k,0)
bad=sum(1 for a in range(6) for b in range(6) for c in range(6) for d_ in range(6)
        if sum(N3[(a,b,x)]*N3[(x,c,d_)] for x in range(6))!=sum(N3[(b,c,x)]*N3[(a,x,d_)] for x in range(6)))
mx=max(v for dd in Q.values() for v in dd.values())
print("Kac-Walton products:"); [print(f"  {names[i]} x {names[j]} = "+" + ".join(f"{v}{names[k]}" for k,v in sorted(d.items()))) for (i,j),d in Q.items()]
print("max N =",mx,"(MULTIPLICITY-FREE)" if mx==1 else "(NMF!)"," assoc violations:",bad)
assert mx==1 and bad==0
def hfrac(w):
    a,b=w; return F(2*a*(a+2)+a*(b+2)+b*(a+2)+2*b*(b+2),30)
print("h =",[str(hfrac(w)) for w in WTS])
print("bosonic =",[n for w,n in zip(WTS,names) if hfrac(w).denominator==1])
assert all(hfrac(w).denominator!=1 for w in WTS[1:])

# ---- Kac-Peterson S, correct Weyl set + prefactor i/(5 sqrt3), sign fixed by S00>0 ----
mp.mp.dps=40
def ip(p,q): return (mp.mpf(2)*p[0]*q[0]+p[0]*q[1]+p[1]*q[0]+mp.mpf(2)*p[1]*q[1])/3
mats=[((1,0),(0,1),1),((-1,1),(0,1),-1),((1,0),(1,-1),-1),((0,-1),(1,-1),1),((-1,1),(-1,0),1),((0,-1),(-1,0),-1)]
acts2=[(lambda p,e1=e1,e2=e2:(e1[0]*p[0]+e2[0]*p[1],e1[1]*p[0]+e2[1]*p[1]),d) for e1,e2,d in mats]
c=mp.j/(5*mp.sqrt(3))
R=[[sum(det*mp.e**(-2*mp.pi*mp.j*ip(a((l[0]+1,l[1]+1)),(m[0]+1,m[1]+1))/5) for a,det in acts2) for m in WTS] for l in WTS]
S=[[-c*R[i][j] for j in range(6)] for i in range(6)]
print("S00 =",S[0][0])
print("unit dev:",max(abs(sum(S[i][k]*mp.conj(S[j][k]) for k in range(6))-(1 if i==j else 0)) for i in range(6) for j in range(6)))
bad2=0; mxr=0
for i in range(6):
    for j in range(i,6):
        for k in range(6):
            v=sum(S[i][t]*S[j][t]*mp.conj(S[k][t])/S[0][t] for t in range(6))
            r=int(mp.nint(v.real)); mxr=max(mxr,abs(complex(v)-r))
            if r!=Q[(i,j)].get(k,0): bad2+=1; print("MISMATCH",names[i],names[j],names[k],complex(v))
print("Verlinde-vs-KacWalton mismatches:",bad2,"max rounding dev:",mxr)
assert bad2==0 and mxr<1e-9
print("CONCLUSION: su(3)_2 modular category is MULTIPLICITY-FREE (max N=1), one Z3 grading line {1,g,gb}, no nontrivial bosons.")
