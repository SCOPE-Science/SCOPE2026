"""Exact finite validations of a joint descent/inversion shuffle limit.
Only Python standard library is needed. Scientific proof is separate from these tests.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import permutations, product
from math import factorial, comb

checks=0

def ck(a,b,msg=''):
    global checks
    assert a==b,(msg,a,b)
    checks+=1

def stats(perm):
    n=len(perm)
    return (sum(perm[i]>perm[i+1] for i in range(n-1)),
            sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))

def shuffled_from_perm(perm,k):
    return perm[:k]+tuple(sorted(perm[k:]))

def prefix(perm,k):
    n=len(perm)
    d=sum(perm[i]>perm[i+1] for i in range(max(0,k-1)))
    inv=sum(perm[i]>perm[j] for i in range(k) for j in range(i+1,n))
    return d,inv

def moment_cov(vals):
    n=len(vals)
    mx=sum(x for x,y in vals)/n
    my=sum(y for x,y in vals)/n
    return sum((x-mx)*(y-my) for x,y in vals)/n

for n in range(2,8):
    ps=list(permutations(range(1,n+1)))
    for k in range(1,n+1):
        H=[];V=[]; fullD=[]
        for p in ps:
            h,v=prefix(p,k)
            H.append(h);V.append(v)
            d,i=stats(shuffled_from_perm(p,k))
            ck(v,i,'inversion coupling')
            if k<n: ck(d-h, int(p[k-1]>min(p[k:])), 'boundary coupling')
            fullD.append(d)
        m=len(ps)
        Eh=F(sum(H),m); Ev=F(sum(V),m)
        Ed=F(sum(fullD),m)
        ck(Eh,F(k-1,2),'conditional mean H')
        ck(Ev,F(k*(2*n-k-1),4),'conditional mean I')
        ck(Ed,F(k-1,2)+(F(n-k,n-k+1) if k<n else 0),'conditional mean D')
        cov=F(sum(h*v for h,v in zip(H,V)),m)-Eh*Ev
        ck(cov,F(k-1,4),'conditional covariance')
        var=F(sum(v*v for v in V),m)-Ev*Ev
        ck(var,sum((F((n-i)*(n-i+2),12) for i in range(1,k+1)),F()),'conditional inversion variance')
        cfull=F(sum(d*v for d,v in zip(fullD,V)),m)-Ed*Ev
        ck(cfull,Ed/2,'conditional full covariance equals half mean descent')

# Direct shuffle-sequence enumeration vs independently chosen occupancy K and uniform permutation.
for n in range(2,6):
    ps=list(permutations(range(1,n+1)))
    for r in range(1,5):
        counts=Counter()
        occupancy=Counter()
        for hist in product(range(1,n+1),repeat=r):
            deck=tuple(range(1,n+1))
            for v in hist:
                deck=(v,)+tuple(x for x in deck if x!=v)
            counts[stats(deck)]+=1
            occupancy[len(set(hist))]+=1
        mixture=Counter()
        for k,w in occupancy.items():
            for perm in ps:
                mixture[stats(shuffled_from_perm(perm,k))]+=F(w,len(ps))
        keys=set(counts)|set(mixture)
        for key in keys:
            ck(F(counts[key]),mixture[key],f'conditional coupling n={n}, r={r}, {key}')
        # Exact law-of-total-covariance identity for every finite time.
        z=F(n**r); totD=sum(F(d*v,z) for (d,i),v in counts.items());totI=sum(F(i*v,z) for (d,i),v in counts.items())
        cov=sum(F(d*i*v,z) for (d,i),v in counts.items())-totD*totI
        distK={k:F(w,z) for k,w in occupancy.items()}
        dfn=lambda k:F(k+1,2)-F(1,n-k+1)
        ifn=lambda k:F(k*(2*n-k-1),4)
        mixed_cov=sum(p*dfn(k)*ifn(k) for k,p in distK.items())-sum(p*dfn(k) for k,p in distK.items())*sum(p*ifn(k) for k,p in distK.items())
        ck(cov,totD/2+mixed_cov,'finite covariance decomposition')
        assert cov>0
        checks+=1

# Symbolic polynomial check by binomial expansion not requiring sympy
from fractions import Fraction
# V_G= (integral_0^a(1-2x)^2 dx + (1-a)*a*a)/12
for a in [F(1,7),F(1,2),F(2,3),F(9,10)]:
    v= (a-2*a*a+F(4,3)*a*a*a+(1-a)*a*a)/12
    ck(v,(1-(1-a)**3)/36,'limiting inversion variance')
print('PASS:',checks,'exact finite assertions')
