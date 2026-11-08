"""Independent finite-field checks for the null-direction affine X-ray spectrum.
Run: python check_null_xray.py (numpy required only for the optional direct Gram test).
This is finite evidence; the general theorem follows from the written proof.
"""
from itertools import product
from collections import Counter

def field(q):
    if q in (3, 5):
        add = lambda a,b: (a+b)%q
        mul = lambda a,b: a*b%q
        inv = lambda a: pow(a,-1,q)
        return add,mul,inv
    if q == 9:
        # F_3[t]/(t^2+1): integer a+3b represents a+b*t.
        def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def mul(a,b): return (((a%3)*(b%3)+2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        def power(a,n):
            x=1
            for _ in range(n): x=mul(x,a)
            return x
        inv=lambda a:power(a,7)
        return add,mul,inv
    raise ValueError(q)

def square_character(a,q,mul):
    if a==0: return 0
    squares={mul(b,b) for b in range(1,q)}
    return 1 if a in squares else -1

def neg_one(q,add):
    return next(i for i in range(q) if add(1,i)==0)

def quad_value(v,diag,add,mul):
    r=0
    for a,x in zip(diag,v): r=add(r,mul(a,mul(x,x)))
    return r

def dot(w,v,diag,add,mul):
    r=0
    for a,x,y in zip(diag,w,v):r=add(r,mul(a,mul(x,y)))
    return r

def directions(q,diag,add,mul,inv):
    d=len(diag); ds=set()
    for v in product(range(q),repeat=d):
        if all(x==0 for x in v) or quad_value(v,diag,add,mul)!=0:continue
        t=next(x for x in v if x)
        ds.add(tuple(mul(inv(t),x) for x in v))
    return sorted(ds)

def formula(q,diag,add,mul):
    d=len(diag);minus=neg_one(q,add)
    det=1
    for x in diag:det=mul(det,x)
    sign=mul(det,minus if ((d//2 if d%2==0 else (d-1)//2)%2) else 1)
    eps=square_character(sign,q,mul)
    P=(q**(d-2)-1)//(q-1)
    if d%2==0:
        Nzero=(q**(d-1)-1)//(q-1)+eps*q**((d-2)//2)
        Niso=P+eps*q**((d-2)//2)
        Nother=P
        Miso=q**(d-1)+eps*(q-1)*q**((d-2)//2)-1
        Mother=(q-1)*(q**(d-1)-eps*q**((d-2)//2))
        cnt=Counter()
        cnt[Nzero]+=1;cnt[Niso]+=Miso;cnt[Nother]+=Mother
        return cnt,eps
    Nzero=(q**(d-1)-1)//(q-1)
    cnt=Counter()
    cnt[Nzero]+=1;cnt[P]+=q**(d-1)-1
    k=q**((d-3)//2)
    cnt[P+k]+=(q-1)//2*(q**(d-1)+q*k)
    cnt[P-k]+=(q-1)//2*(q**(d-1)-q*k)
    return cnt,eps

def check(q,diag):
    add,mul,inv=field(q)
    ds=directions(q,diag,add,mul,inv)
    actual=Counter()
    for w in product(range(q), repeat=len(diag)):
        actual[sum(dot(w,v,diag,add,mul)==0 for v in ds)]+=1
    expected,eps=formula(q,diag,add,mul)
    assert actual==expected,(q,diag,actual,expected)
    # Nonnegative direction weighting cannot improve the normal-operator condition number.
    if 0 not in expected:
        weights=[1+(7*i+3)%11 for i in range(len(ds))]
        total=sum(weights)
        weighted_min=min(sum(weights[i] for i,v in enumerate(ds) if dot(w,v,diag,add,mul)==0)
                         for w in product(range(q),repeat=len(diag)) if any(w))
        assert weighted_min * len(ds) <= total * min(expected)
    print('COUNT_AND_WEIGHT_PASS',q,len(diag),diag[-1],'Witt sign',eps,
          'directions',len(ds),'multipliers',sorted(expected.items()))
    return ds

for q,dspec in [(3,[3,4,5]),(5,[3,4]),(9,[3,4])]:
    add,mul,inv=field(q)
    nonsquare=next(x for x in range(1,q) if square_character(x,q,mul)==-1)
    for d in dspec:
        for a in (1,nonsquare):
            # q=9,d=4 has 6561 frequencies and approximately 100 directions.
            check(q,[1]*(d-1)+[a])

try:
    import numpy as np
except ImportError:
    print('OPTIONAL_NUMPY_GRAM_TEST_SKIPPED')
else:
    for diag in ([1,1,1],[1,1,1,2]):
        q=3;d=len(diag);add,mul,inv=field(q)
        ds=directions(q,diag,add,mul,inv)
        pts=list(product(range(q),repeat=d)); idx={x:i for i,x in enumerate(pts)}
        rowsets=set()
        for v in ds:
            for x in pts:
                rowsets.add(tuple(sorted(idx[tuple((x[i]+t*v[i])%q for i in range(d))] for t in range(q))))
        T=np.zeros((len(rowsets),len(pts)),dtype=np.int16)
        for j,ids in enumerate(rowsets):T[j,list(ids)]=1
        Gram=T.T@T
        got=np.linalg.eigvalsh(Gram)
        pred,_=formula(q,diag,add,mul)
        want=sorted([q*eig for eig,mult in pred.items() for _ in range(mult)])
        assert np.allclose(got,want,atol=1e-8)
        print('DIRECT_INCIDENCE_GRAM_PASS',q,d,len(rowsets),len(pts))
print('NULL_RAY_FOURIER_VERIFICATION_PASS')
