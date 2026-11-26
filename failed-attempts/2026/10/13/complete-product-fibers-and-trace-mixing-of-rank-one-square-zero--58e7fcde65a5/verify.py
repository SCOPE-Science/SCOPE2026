"""Direct finite-field enumeration of rank-one square-zero word fibers."""
from collections import Counter
from itertools import product

def field(q):
    if q==4:
        def add(a,b): return a^b
        def mul(a,b):
            p=0
            if b&1: p^=a
            if b&2: p^=a<<1
            if p&8: p^=0b1100  # x^3=(x+1)x= x^2+x; fixed polynomial reduction
            if p&4: p^=0b111  # x^2 = x+1 in GF(4)
            return p
        return add,mul
    def add(a,b): return (a+b)%q
    def mul(a,b): return (a*b)%q
    return add,mul

def matmul(a,b,n,add,mul):
    return tuple(sum_mod([mul(a[i*n+k],b[k*n+j]) for k in range(n)],add) for i in range(n) for j in range(n))

def sum_mod(vals,add):
    t=0
    for v in vals:t=add(t,v)
    return t

def make_C(q,n,add,mul):
    vectors=[v for v in product(range(q),repeat=n) if any(v)]
    C=set()
    for u in vectors:
        for v in vectors:
            if sum_mod((mul(u[i],v[i]) for i in range(n)),add)==0:
                C.add(tuple(mul(u[i],v[j]) for i in range(n) for j in range(n)))
    expected=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert len(C)==expected,(q,n,len(C),expected)
    return C

def theory(q,n,r,b,add):
    h=q**(n-1); J=q**(n-2); D=q**n-1
    C=D*(h-1)//(q-1)
    L=h*(h-1); R=-(q-1)*J
    if not any(b): return C**r-C*L**(r-1)
    # all produced nonzero products are rank-one by construction;
    # the direct enumerator checks support by matching every observed matrix
    tr=sum_mod((b[i*n+i] for i in range(n)),add)
    numerator=(h-1)*L**(r-1) + (h*(q-1) if tr==0 else -(h-1))*R**(r-1)
    assert numerator%D==0,(q,n,r,tr,numerator,D)
    return numerator//D

def check(q,n,max_r):
    add,mul=field(q)
    C=make_C(q,n,add,mul)
    z=(0,)*(n*n)
    dist={x:1 for x in C}
    total_targets=(q**n-1)**2//(q-1)
    for r in range(1,max_r+1):
        assert sum(dist.values())==len(C)**r
        assert dist.get(z,0)==theory(q,n,r,z,add)
        for b,count in dist.items():
            assert count==theory(q,n,r,b,add),(q,n,r,b,count,theory(q,n,r,b,add))
        # Each unattained rank-one trace stratum must have predicted 0, and forbidden other ranks too.
        # Rank-one target exhaustive via vector dyads, independent of C generation.
        all_rank1=set()
        vectors=[v for v in product(range(q),repeat=n) if any(v)]
        for u in vectors:
            for v in vectors:
                all_rank1.add(tuple(mul(u[i],v[j]) for i in range(n) for j in range(n)))
        assert len(all_rank1)==total_targets
        for b in all_rank1:
            assert dist.get(b,0)==theory(q,n,r,b,add),(q,n,r,b,dist.get(b,0),theory(q,n,r,b,add))
        assert set(dist).issubset(all_rank1|{z})
        if r<max_r:
            d={}
            for a,count in dist.items():
                for x in C:
                    y=matmul(a,x,n,add,mul)
                    d[y]=d.get(y,0)+count
            dist=d
    print('PASS',q,n,'lengths',1,'..',max_r,'square_zero_factors',len(C),'rank_one_targets',total_targets)

if __name__=='__main__':
    for q,n,r in [(2,2,5),(3,2,5),(4,2,4),(5,2,4),(2,3,4),(3,3,3),(4,3,3),(2,4,3)]:
        check(q,n,r)
    print('VERIFY_OK')
