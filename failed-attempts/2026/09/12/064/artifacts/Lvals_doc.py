import mpmath as mp
mp.mp.dps=60
# Documented (non-rigorous) L-values: a_n from exact point counts; Dokchitser tail (heuristic).
a1,a2,a3,a4,a6=1,1,1,-10,-10
def Frhs(x): return x**3+a2*x**2+a4*x+a6
def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def ap(p):
    if p==3: return -1
    if p==5: return 1
    return -sum(legendre((a1*x+a3)**2+4*Frhs(x),p) for x in range(p))
def sieve(N):
    b=[True]*(N+1);o=[]
    for i in range(2,N+1):
        if b[i]:
            o.append(i)
            for j in range(i*i,N+1,i): b[j]=False
    return o
P=sieve(6000); AP={p:ap(p) for p in P}
def kron(d,p):
    a=d%p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def apT(p):
    if p==23: return 0
    return kron(-23,p)*AP[p]
def mkan(apf,bad,add):
    def ppow(p,k):
        if p in add: return 0
        if p in bad: return bad[p]**k
        t=apf(p);u0,u1=1,t
        if k==0: return 1
        if k==1: return t
        for j in range(2,k+1): u0,u1=u1,t*u1-p*u0
        return u1
    def an(n):
        m=n;r=1;d=2
        while d*d<=m:
            if m%d==0:
                c=0
                while m%d==0: m//=d;c+=1
                r*=ppow(d,c)
            d+=1 if d==2 else 2
        if m>1: r*=ppow(m,1)
        return r
    return an
anE=mkan(AP.get,{3:-1,5:1},set()); anT=mkan(apT,{3:-1,5:-1},{23})
def L(an,N,w,M):
    s=mp.mpf('0')
    for n in range(1,M+1):
        c=an(n)
        if c: s+=mp.mpf(c)/n*mp.e**(-2*mp.pi*n/mp.sqrt(N))
    return (1+w)*s
for M in [500,1000,2000,4000]:
    print("M=",M,"L(E,1)=",L(anE,15,1,M))
for M in [1000,2000,4000,6000]:
    print("M=",M,"L(tw,1)=",L(anT,7935,1,M))
