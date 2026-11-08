"""Direct basis-identity check for rank-one averaging maps on finite spin factors.
Run with Python 3; no dependencies beyond standard library.
"""
from itertools import product

def mul(x,y,diag,p):
    return ((x[0]*y[0]+sum(t*x[i+1]*y[i+1] for i,t in enumerate(diag)))%p,)+tuple((x[0]*y[i]+x[i]*y[0])%p for i in range(1,len(x)))

def formula(p,diag):
    d=len(diag)
    q=p
    def Q(v):return sum(diag[i]*v[i]*v[i] for i in range(d))%p
    count1=sum(Q(v)==1 for v in product(range(p),repeat=d))
    count0=sum(Q(v)==0 for v in product(range(p),repeat=d))-1
    assert count0%(p-1)==0
    return (p**(d+1)-1) + (p-1)*count1 + (p**(d-1)-1)*count0//(p-1), (p**(d+1)-1,(p-1)*count1,(p**(d-1)-1)*count0//(p-1))

def direct(p,diag):
    d=len(diag); n=d+1; basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    c=[0,0,0]; nil2=[0,0,0]
    for v in product(range(p),repeat=n):
        # Unique representative of each nonzero projective image line.
        if not any(v) or next(x for x in v if x)!=1:continue
        a2=mul(v,v,diag,p)
        av=[mul(v,e,diag,p) for e in basis]
        cls=0 if v[1:]==(0,)*d else 2 if v[0]==0 else 1
        for phi in product(range(p),repeat=n):
            if not any(phi):continue
            coeff=[sum(phi[k]*av[j][k] for k in range(n))%p for j in range(n)]
            # The original rank-one identity on all basis pairs:
            # P(e_i)P(e_j)=P(P(e_i)e_j), and the symmetric second equality.
            if any(any((phi[i]*phi[j]*a2[k]-phi[i]*coeff[j]*v[k])%p for k in range(n))
                   for i in range(n) for j in range(n)):
                continue
            c[cls]+=1
            if sum(x*y for x,y in zip(phi,v))%p==0:nil2[cls]+=1
    expected,types=formula(p,diag)
    assert tuple(c)==types,(p,diag,c,types)
    assert sum(c)==expected
    return f"GF({p}) diagonal={diag}: exact all basis identities count={sum(c)}; image strata={tuple(c)}; P^2=0 strata={tuple(nil2)}"

if __name__=='__main__':
    for p,diag in [(3,(1,1,1)),(3,(1,1,2)),(5,(1,1,1)),(5,(1,1,2)),(3,(1,1,1,1))]:
        print(direct(p,diag))
    print('SPIN_AVERAGING_DIRECT_ORIGINAL_IDENTITIES_OK')
