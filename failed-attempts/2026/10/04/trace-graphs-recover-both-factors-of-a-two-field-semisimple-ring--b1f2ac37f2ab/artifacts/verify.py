from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a ^ b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        # F4 = F2[t]/(t^2+t+1), bits encode a0+a1*t.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)

def matrices(q):
    return list(product(range(q), repeat=4))

def trprod(F,A,C):
    # row-major 2x2 matrices: tr(AC)=a00*c00+a01*c10+a10*c01+a11*c11.
    s=0
    for x,y in ((A[0],C[0]),(A[1],C[2]),(A[2],C[1]),(A[3],C[3])):
        s=F.add(s,F.mul(x,y))
    return s

cache={}
def field_data(q):
    if q in cache:
        return cache[q]
    F=Field(q)
    M=matrices(q)
    zero=(0,0,0,0)
    kernels={}
    squaretrace={}
    for A in M:
        kernels[A]=sum(trprod(F,A,C)==0 for C in M)
        squaretrace[A]=trprod(F,A,A)
        if A==zero:
            assert kernels[A]==q**4
        else:
            assert kernels[A]==q**3
    # Explicit witnesses for both square-trace types.
    E12=(0,1,0,0)
    E11=(1,0,0,0)
    assert squaretrace[E12]==0
    assert squaretrace[E11]==1
    cache[q]=(F,M,zero,kernels,squaretrace)
    return cache[q]

def reconstruct(v, degrees):
    delta=min(degrees)
    B=delta+2
    assert (v+1)%B==0
    P=(v+1)//B
    N=0
    z=1
    while z < v+1:
        z*=P
        N+=1
    assert z==v+1
    n=math_isqrt(N)
    assert n*n==N
    T=sorted({(d+2)//B for d in degrees if (d+2)%B==0})
    vals=[x for x in T if x!=1]
    if len(vals)==1:
        factors=sorted([vals[0],vals[0]])
    else:
        assert len(vals)==2
        factors=sorted(vals)
    assert factors[0]*factors[1]==P
    return n,tuple(factors)

def math_isqrt(x):
    y=0
    while (y+1)*(y+1)<=x:
        y+=1
    return y

def check_pair(q,r):
    _,Mq,zq,kq,sq=field_data(q)
    _,Mr,zr,kr,sr=field_data(r)
    B=(q*r)**3
    v=(q*r)**4-1
    degrees=set()
    for A in Mq:
        for C in Mr:
            if A==zq and C==zr:
                continue
            orth=kq[A]*kr[C]
            selforth=(sq[A]==0 and sr[C]==0)
            d=orth-1-(1 if selforth else 0)
            degrees.add(d)
    predicted={B*s-c for s in {1,q,r} for c in (1,2)}
    assert degrees==predicted, (q,r,degrees,predicted)
    assert min(degrees)==B-2
    assert reconstruct(v,degrees)==(2,tuple(sorted((q,r))))
    print({"q":q,"r":r,"vertices":v,"degrees":sorted(degrees),"recovered":reconstruct(v,degrees)})

for q in (2,3,4,5):
    field_data(q)

for pair in ((2,2),(2,3),(2,4),(3,4),(3,5)):
    check_pair(*pair)

print("VERIFY_OK")
