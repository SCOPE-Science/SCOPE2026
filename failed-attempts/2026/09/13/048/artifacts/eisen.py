import math
ONE=(1,0); ZERO=(0,0); OMEGA=(0,1); W2=(-1,-1)
UNITS=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
def eadd(p,q): return (p[0]+q[0],p[1]+q[1])
def esub(p,q): return (p[0]-q[0],p[1]-q[1])
def eneg(p): return (-p[0],-p[1])
def emul(p,q):
    a,b=p; c,d=q
    return (a*c-b*d, a*d+b*c-b*d)
def enorm(p): return p[0]*p[0]-p[0]*p[1]+p[1]*p[1]
def econj(p): return (p[0]-p[1],-p[1])
def eeq(p,q): return p[0]==q[0] and p[1]==q[1]
def edivmod(a,b):
    assert not eeq(b,ZERO)
    N=enorm(b); num=emul(a,econj(b))
    q=(int(math.floor(num[0]/N+0.5)),int(math.floor(num[1]/N+0.5)))
    return q,esub(a,emul(q,b))
def emod(a,m): return edivmod(a,m)[1]
def edivides(m,a): return eeq(emod(a,m),ZERO)
def epowmod(base,e,pi):
    r=ONE; b=emod(base,pi)
    while e>0:
        if e&1: r=emod(emul(r,b),pi)
        b=emod(emul(b,b),pi); e>>=1
    return r
def econg(a,b,pi): return edivides(pi,esub(a,b))
def cubic_symbol(alpha,pi):
    if edivides(pi,alpha): return None
    N=enorm(pi); assert (N-1)%3==0,(alpha,pi,N)
    v=epowmod(alpha,(N-1)//3,pi)
    if econg(v,ONE,pi): return 0
    if econg(v,OMEGA,pi): return 1
    if econg(v,W2,pi): return 2
    raise AssertionError(f"bad sym {alpha} mod {pi}: v={v}")
def is_primary(a): return (a[0]-1)%3==0 and (a[1]%3)==0
def primary_associate(a):
    for u in UNITS:
        c=emul(u,a)
        if is_primary(c): return c
    raise AssertionError(f"no prim assoc {a}")
def e2str(a): return f"{a[0]}+{a[1]}w"
def sieve(n):
    bs=bytearray(b'\x01')*(n+1); out=[]
    for i in range(2,n+1):
        if bs[i]:
            out.append(i)
            if i*i<=n:
                for j in range(i*i,n+1,i): bs[j]=0
    return out
def find_factor_split(p):
    r=int(math.isqrt(p))+1
    for a in range(-r-1,r+2):
        for b in range(-r-1,r+2):
            if a*a-a*b+b*b==p: return (a,b)
    raise AssertionError(f"no factor {p}")
def enum_primary_primes(nbound):
    primes=sieve(nbound-1); out=[]
    for p in primes:
        if p==3: continue
        if p%3==1:
            f=find_factor_split(p); g=econj(f)
            out.append((primary_associate(f),p)); out.append((primary_associate(g),p))
        else:
            if p*p<nbound: out.append(((-p,0),p*p))
    seen=set(); res=[]
    for pi,N in out:
        if pi in seen: continue
        seen.add(pi); res.append((pi,N))
    return res
