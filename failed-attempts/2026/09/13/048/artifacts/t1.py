from eisen import *
# sanity: euclidean remainder smaller
import random
random.seed(1)
for _ in range(2000):
    a=(random.randint(-50,50),random.randint(-50,50))
    b=(random.randint(-20,20),random.randint(-20,20))
    if eeq(b,ZERO): continue
    q,r=edivmod(a,b)
    assert eeq(esub(a,eadd(emul(q,b),r)),ZERO),(a,b,q,r)
    assert enorm(r)<enorm(b),(a,b,r)
print("euclid ok")
# cubic reciprocity sanity on small primes
primes=enum_primary_primes(5000)
print("eligible count:",len(primes))
assert all(is_primary(pi) for pi,N in primes)
small=[p for p in primes if p[1]<150]
nchk=0
for i,(p1,n1) in enumerate(small):
    for j,(p2,n2) in enumerate(small):
        if i==j: continue
        if enorm(p1)==enorm(p2) and eeq(emul(p1,econj(p2)),(enorm(p1),0)): continue
        s1=cubic_symbol(p1,p2); s2=cubic_symbol(p2,p1)
        assert s1==s2,(p1,p2,s1,s2)
        nchk+=1
print("reciprocity checks:",nchk)
