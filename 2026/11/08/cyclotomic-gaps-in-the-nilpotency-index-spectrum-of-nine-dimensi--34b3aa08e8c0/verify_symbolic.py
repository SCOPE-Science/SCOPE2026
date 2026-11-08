"""Universal PBW power-identity verification over Z[lambda,a,b,c,d,e,f,g,h].
Pure standard-library integer polynomial arithmetic; no computer-algebra dependency.
"""

NVAR=9
ZERO=(0,)*NVAR

def const(c):return {} if c==0 else {ZERO:c}

def ind(i):
    m=[0]*NVAR;m[i]=1
    return {tuple(m):1}

def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items():out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}

def neg(p):return {m:-c for m,c in p.items()}

def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            e=tuple(x+y for x,y in zip(m,n))
            out[e]=out.get(e,0)+c*d
    return {m:c for m,c in out.items() if c}

def power(p,r):
    z=const(1)
    for _ in range(r):z=mul(z,p)
    return z

def product(P,Q):
    out={}
    for (i,j),A in P.items():
        for (r,v),B in Q.items():
            if i+r>=3 or j+v>=3:continue
            k=(i+r,j+v)
            t=mul(mul(A,B),power(lam,j*r))
            out[k]=add(out.get(k,{}),t)
    return {k:v for k,v in out.items() if v}

lam,a,b,c,d,e,f,g,h=[ind(i) for i in range(NVAR)]
W={(1,0):a,(0,1):b,(2,0):c,(1,1):d,(0,2):e,
   (2,1):f,(1,2):g,(2,2):h}
W2=product(W,W)
W3=product(W2,W)
W4=product(W3,W)
W5=product(W4,W)
S=add(const(1),lam,power(lam,2))
T=add(const(1),neg(lam),power(lam,2))
U=add(const(1),power(lam,2))
assert W2[(2,0)]==power(a,2)
assert W2[(0,2)]==power(b,2)
assert W2[(1,1)]==mul(add(const(1),lam),mul(a,b))
# Extract the a=b=0 specialization of the fourth homogeneous coefficient.
D4={mon:coeff for mon,coeff in W2[(2,2)].items() if mon[1]==0 and mon[2]==0}
assert D4==add(mul(lam,power(d,2)),mul(add(const(1),power(lam,4)),mul(c,e)))
E3={(2,1):mul(S,mul(power(a,2),b)),
    (1,2):mul(S,mul(a,power(b,2))),
    (2,2):mul(S,add(mul(T,add(mul(power(a,2),e),mul(power(b,2),c))),
                  mul(add(const(1),lam),mul(mul(a,b),d))))}
assert W3==E3,(W3,E3)
assert W4=={(2,2):mul(mul(S,U),mul(power(a,2),power(b,2)))}
assert W5=={}
print('VERIFY_OK_QCI_SYMBOLIC')
