"""Independent verifier for lane-363 fallback certificate (stdlib only).
Checks, from the logged word data alone:
 (a) Nielsen-move history replays to the claimed images (automorphism property built in);
 (b) transition matrix M, det=+-1, M^3>0 (primitive/irreducible + expanding);
 (c) char poly x^4-2x^3-x+1, PF root enclosure [2.117,2.118] w/ sign change + CW interval;
 (d) Df map, gates, no taken illegal turn (no period-1 iNP with taken illegal turn),
     local-Whitehead-closure connectivity (Bestvina-Handel full-irreducibility input);
 (e) no cyclotomic factor x^k-1 (k<=12) shared with char poly (abelian-level atoroidality screen).
Prints VERIFY_OK on success.
"""
import itertools
from fractions import Fraction
G = 'abcd'
N = {g:i for i,g in enumerate(G)}
HIST = [(0,2),(3,0),(2,3),(1,3)]
PERM = (1,2,0,3)
IMAGES = ['bad','cd','ad','db']
def appT(words,x,y):
    out=[]
    for w in words:
        nw=[]
        for l in w:
            if l==x: nw.extend([x,y])
            else: nw.append(l)
        out.append(nw)
    return out
def matmul(X,Y): return [[sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def mpow(Mm,k):
    R=[[1 if i==j else 0 for j in range(4)] for i in range(4)]
    for _ in range(k): R=matmul(Mm,R)
    return R
def det4(Mm):
    s=0
    for p in itertools.permutations(range(4)):
        inv=sum(1 for i in range(4) for k in range(i+1,4) if p[i]>p[k])
        t=Mm[0][p[0]]*Mm[1][p[1]]*Mm[2][p[2]]*Mm[3][p[3]]
        s+= t if inv%2==0 else -t
    return s
# (a)
words=[[i] for i in range(4)]
for (x,y) in HIST: words=appT(words,x,y)
words=[[PERM[l] for l in w] for w in words]
got=[''.join(G[l] for l in w) for w in words]
assert got==IMAGES, (got,IMAGES)
assert all(2<=len(w)<=4 for w in words)
# (b)
M=[[0]*4 for _ in range(4)]
for j,w in enumerate(words):
    for l in w: M[l][j]+=1
assert M==[[1,0,1,0],[1,0,0,1],[0,1,0,0],[1,1,1,1]], M
assert abs(det4(M))==1
M3=mpow(M,3)
assert all(c>0 for row in M3 for c in row), M3
assert M3==[[2,1,1,1],[4,3,3,2],[2,1,2,1],[7,4,5,4]], M3
# (c) charpoly
poly=[Fraction(0)]*5
for p in itertools.permutations(range(4)):
    inv=sum(1 for i in range(4) for k in range(i+1,4) if p[i]>p[k])
    sgn=1 if inv%2==0 else -1
    cur=[Fraction(1)]
    for i in range(4):
        if p[i]==i:
            m=Fraction(M[i][p[i]])
            nxt=[Fraction(0)]*(len(cur)+1)
            for k2,c2 in enumerate(cur):
                nxt[k2]+=c2*(-m); nxt[k2+1]+=c2
            cur=nxt
        else:
            m=Fraction(-M[i][p[i]])
            cur=[c2*m for c2 in cur]
    for k2,c2 in enumerate(cur): poly[k2]+=sgn*c2
assert list(poly)==[Fraction(1),Fraction(-1),Fraction(0),Fraction(-2),Fraction(1)], poly
def peval(q,x):
    s=Fraction(0)
    for k,c in enumerate(q): s+=c*x**k
    return s
assert peval(poly,Fraction(2117,1000))<0 and peval(poly,Fraction(2118,1000))>0
# strict increase on [2.117,2.118] via derivative lower bound: p'(x)=4x^3-6x^2-1; p'(2.117)>0 and p''>0 there
# p''(x)=12x^2-12x=12x(x-1)>0 for x>1, so p' increasing on interval; check p'(lo)>0:
lo=Fraction(2117,1000)
assert 4*lo**3-6*lo**2-1>0
# CW rational enclosure
vr=[Fraction(11769,100000),Fraction(1741,6250),Fraction(6577,50000),Fraction(47221,100000)]
assert all(v>0 for v in vr)
Mv=[sum(Fraction(M[i][j])*vr[j] for j in range(4)) for i in range(4)]
rats=[Mv[i]/vr[i] for i in range(4)]
assert min(rats)>Fraction(2117,1000) and max(rats)<Fraction(2118,1000), rats
# (d)
firsts=[w[0] for w in words]; lasts=[w[-1] for w in words]
assert len(set(firsts))==4
D={j:firsts[j] for j in range(4)}; D.update({4+j:4+lasts[j] for j in range(4)})
assert D=={0:1,1:2,2:0,3:3,4:7,5:7,6:7,7:5}, D
from collections import defaultdict
fib=defaultdict(list)
for d,im in D.items(): fib[im].append(d)
ill={tuple(sorted((a,b))) for im,ds in fib.items() for i,a in enumerate(ds) for b in ds[i+1:]}
assert ill=={(4,5),(4,6),(5,6)}, ill
T=set()
for w in words:
    for i in range(len(w)-1): T.add(tuple(sorted((4+w[i],w[i+1]))))
assert T=={(0,5),(1,7),(3,4),(3,6)}, T
assert T & ill==set()
cur=set(T)
for _ in range(80):
    nxt=set(cur)
    for (x,y) in cur: nxt.add(tuple(sorted((D[x],D[y]))))
    if nxt==cur: break
    cur=nxt
assert len(cur)==10, cur
adj={i:set() for i in range(8)}
for (x,y) in cur:
    if x!=y: adj[x].add(y); adj[y].add(x)
seen={0};stack=[0]
while stack:
    u=stack.pop()
    for v in adj[u]:
        if v not in seen: seen.add(v); stack.append(v)
assert len(seen)==8, seen
# (e) cyclotomic screen via exact integer polynomial gcd (sympy-free Euclidean algorithm)
def polymod_gcd(a,b):
    # monic-ish exact gcd over QQ using Fractions
    def norm(p):
        p=list(p)
        while len(p)>1 and p[-1]==0: p.pop()
        return p
    def divmod_p(a,b):
        a=norm(a); b=norm(b)
        if len(a)<len(b): return ([Fraction(0)],a)
        q=[Fraction(0)]*(len(a)-len(b)+1)
        r=list(a)
        while len(r)>=len(b) and any(r):
            c=r[-1]/b[-1]; k=len(r)-len(b)
            q[k]+=c
            for i in range(len(b)): r[k+i]-=c*b[i]
            r=norm(r)
        return (q,r)
    a=[Fraction(v) for v in norm(a)]; b=[Fraction(v) for v in norm(b)]
    while any(b):
        _,r=divmod_p(a,b); a,b=b,r
    return a
P=[1,-1,0,-2,1]  # const..x^4 as ints
for k in range(1,13):
    Q=[Fraction(0)]*(k+1); Q[0]=Fraction(-1); Q[k]=Fraction(1)
    g=polymod_gcd([Fraction(v) for v in P],Q)
    deg=len([v for v in g]) -1 if not (len(g)==1 and g[0]==0) else -1
    # normalize: constant gcd => degree 0
    assert deg==0, (k,g)
print("VERIFY_OK")
