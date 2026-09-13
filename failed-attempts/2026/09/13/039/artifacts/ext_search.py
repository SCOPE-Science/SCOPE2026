# Search polynomial sections x(t), deg<=d, over F49 for candidate model M1.
# F49 = F7[w]/(w^2+1)? check irreducible: squares mod7 = {0,1,2,4}; -1=6 not square -> w^2+1 irr. good.
p=7
def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def neg(a): return ((-a[0])%p,(-a[1])%p)
def inv(a):
    d=(a[0]*a[0]+a[1]*a[1])%p
    return ((a[0]*pow(d,-1,p))%p,(-a[1]*pow(d,-1,p))%p)
def is_sq(a):
    # a^{(49-1)/2}==1?
    # brute: exists b b^2=a
    for x in range(p):
        for y in range(p):
            if mul((x,y),(x,y))==a: return True
    return False
def sqrt(a):
    for x in range(p):
        for y in range(p):
            if mul((x,y),(x,y))==a: return (x,y)
    return None
At=[(1,0),(5,0),(3,0)]
Bt=[(2,0),(1,0),(1,0),(6,0),(2,0)]
A=[(0,0)]*9
for i,a in enumerate(At): A[i+2]=a
B=[(0,0)]*13
for i,b in enumerate(Bt): B[i+3]=b
ZERO=(0,0); ONE=(1,0)
def pmul(f,g):
    h=[ZERO]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        if a==ZERO: continue
        for j,b in enumerate(g):
            if b==ZERO: continue
            h[i+j]=add(h[i+j],mul(a,b))
    return h
def ppow(f,n):
    r=[ONE]
    for _ in range(n): r=pmul(r,f)
    return r
def trim(f):
    f=list(f)
    while len(f)>1 and f[-1]==ZERO: f.pop()
    return f
import itertools
F49=[(x,y) for x in range(p) for y in range(p)]

def find_y(xc):
    X=list(xc)
    X3=ppow(X,3); AX=pmul(A,X)
    n=max(len(X3),len(AX),len(B))
    R=[ZERO]*n
    for i in range(len(X3)): R[i]=add(R[i],X3[i])
    for i in range(len(AX)): R[i]=add(R[i],AX[i])
    for i in range(len(B)): R[i]=add(R[i],B[i])
    R=trim(R)
    d=len(R)-1
    if d%2==1: return None
    m=d//2
    if not is_sq(R[d]): return None
    yl=sqrt(R[d])
    y=[ZERO]*(m+1); y[m]=yl
    for k in range(2*m-1,-1,-1):
        ju=k-m
        known=ZERO
        for i in range(m+1):
            j=k-i
            if j<0 or j>m: continue
            if (i==m and j==ju) or (j==m and i==ju): continue
            known=add(known,mul(y[i],y[j]))
        s=R[k] if k<len(R) else ZERO
        if ju<0 or ju>=m:
            if known!=s: return None
        else:
            rhs=add(s,neg(known))
            y[ju]=mul(rhs,inv(mul((2,0),yl)))
    # verify
    yy=[ZERO]*(2*m+1)
    for i in range(m+1):
        for j in range(m+1):
            yy[i+j]=add(yy[i+j],mul(y[i],y[j]))
    if trim(yy)!=R: return None
    return y

def show(v): return ''.join('(%d,%d)'%t for t in v)
# deg<=2 first
import time
t0=time.time()
ns=0
sols=[]
for xc in itertools.product(F49, repeat=3):
    y=find_y(list(xc))
    if y is not None:
        ns+=1; sols.append((xc,y))
        print("SEC deg<=2 x=",show(xc),"y=",show(y))
print("done deg<=2 n=",ns,"t=",time.time()-t0)
