from itertools import product, permutations
from math import factorial
from fractions import Fraction

def parts(n, m=1):
    if n==0:
        yield []
    else:
        for d in range(m,n+1):
            for tail in parts(n-d,d):
                yield [d]+tail

def formula(r,k):
    s=Fraction(0,1)
    for lam in parts(r):
        md={d:lam.count(d) for d in set(lam)}
        z=1
        ell=len(lam)
        prodv=1
        for d,m in md.items():
            z*=d**m*factorial(m)
            F=sum(e*md.get(e,0) for e in range(1,d+1) if d%e==0)
            prodv*=F**(k*m)
        s += Fraction(2**((k-1)*ell)*prodv,z)
    assert s.denominator==1
    return s.numerator

def perm_apply(p,x): return p[x]
def perm_inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)

def act_elem(p, elem):
    w,u=elem
    return tuple(p[i] for i in w),u

def conj(p, endo):
    # g^{-1} f g on generators x, represented with left function convention:
    # x -> p[x] -> f[p[x]] -> p^{-1} on output letters
    inv=perm_inv(p)
    return tuple(act_elem(inv, endo[p[x]]) for x in range(len(p)))

def brute(r,k):
    us=list(product(range(2), repeat=k-1))
    layer=[(w,u) for w in product(range(r),repeat=k) for u in us]
    endos=list(product(layer, repeat=r))
    perms=list(permutations(range(r)))
    unseen=set(endos); count=0
    while unseen:
        f=unseen.pop(); orb={conj(p,f) for p in perms}
        unseen.difference_update(orb); count+=1
    return count

for r in range(1,4):
  for k in (1,2):
    a=formula(r,k); b=brute(r,k)
    print(r,k,a,b)
    assert a==b
print('k=1 seq', [formula(r,1) for r in range(1,7)])
print('k=2 seq', [formula(r,2) for r in range(1,7)])
print('VERIFY_OK')
