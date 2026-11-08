"""Exact finite verification of simultaneous divisor/progression coprime matching."""
from fractions import Fraction
from math import gcd
from itertools import product


def factors(n):
    f={}; t=n; p=2
    while p*p<=t:
        if t%p==0:
            e=0
            while t%p==0: t//=p; e+=1
            f[p]=e
        p+=1
    if t>1:f[t]=1
    return f


def divisor_list(n):
    ds=[1]
    for p,e in factors(n).items():
        ds=[d*p**j for d in ds for j in range(e+1)]
    return sorted(ds)


def obstruction(n,p):
    fs=factors(n); e=fs.get(p,0)
    if not e:return 0
    N=1
    for t in fs.values():N*=t+1
    T=N//(e+1)
    return min(p,max(0,e+1-p)*T)


def simultaneous_density(ns):
    ps=set().union(*(set(factors(n)) for n in ns))
    d=Fraction(1)
    for p in ps:
        d*=Fraction(p+1-max(obstruction(n,p) for n in ns),p+1)
    return d


def criterion(ns,a,b):
    for n in ns:
        fs=factors(n)
        N=1
        for e in fs.values():N*=e+1
        for p,e in fs.items():
            count=sum((a+b*j)%p==0 for j in range(N))
            if count*(e+1)>N:return False
    return True


def perfect_matching(n,a,b):
    ds=divisor_list(n)
    arr=[a+b*j for j in range(len(ds))]
    taken=[-1]*len(ds)
    def augment(k,seen):
        for i,d in enumerate(ds):
            if not seen[i] and gcd(arr[k],d)==1:
                seen[i]=True
                if taken[i]==-1 or augment(taken[i],seen):
                    taken[i]=k
                    return True
        return False
    for i in range(len(ds)):
        if not augment(i,[False]*len(ds)):return False
    return True


def residue_density(ns):
    primes=set().union(*(set(factors(n)) for n in ns))
    modulus=1
    for p in primes:modulus*=p
    valid=0; total=0
    for a,b in product(range(modulus),repeat=2):
        if all(a%p or b%p for p in primes):
            total+=1
            valid+=criterion(ns,a,b)
    return Fraction(valid,total)


def isprime(p):return p>=2 and all(p%j for j in range(2,int(p**.5)+1))


def main():
    examples={
        (4,4):Fraction(2,3),
        (4,8):Fraction(1,3),
        (4,27):Fraction(1,2),
        (27,81):Fraction(1,2),
        (4,27,81):Fraction(1,3),
        (4,8,27,81):Fraction(1,6),
        (9,1,7):Fraction(1),
    }
    for ns,expected in examples.items():
        assert simultaneous_density(ns)==expected,(ns,simultaneous_density(ns),expected)
    suites=[(4,8),(4,9),(4,27),(8,27),(9,27),(27,81),(27,81,4),
            (27,81,8),(4,4,8),(1,2,3),(4,27,81,8),(16,27),(25,27),
            (4,81),(27,27,27),(8,12),(12,24),(18,36),(54,72)]
    for ns in suites:
        assert simultaneous_density(ns)==residue_density(ns),(ns,simultaneous_density(ns),residue_density(ns))
    checks=0
    small=[1,2,3,4,6,8,9,12,16,24,27,32,36,48]
    for n,m in product(small,repeat=2):
        for a in range(1,8):
            for b in range(1,8):
                if gcd(a,b)==1:
                    pred=criterion((n,m),a,b)
                    actual=perfect_matching(n,a,b) and perfect_matching(m,a,b)
                    assert pred==actual,(n,m,a,b,pred,actual)
                    checks+=1
    primes=[p for p in range(2,60) if isprime(p)]
    vals=[]
    for k in (1,2,3,4):
        u=1.0
        for p in primes:
            u*=(1+p*(1-p**(-p))**k)/(p+1)
        vals.append(u)
    assert vals[1]>vals[0]**2
    print('EXACT_SAME_PRIME_EXAMPLES',{'4,8':str(simultaneous_density((4,8))),'27,81':str(simultaneous_density((27,81)))})
    print('CRT_LOCAL_CENSUSES',len(suites))
    print('PERFECT_MATCHING_COMPARISONS',checks)
    print('JOINT_EULER_PRODUCTS',*[f'{v:.12f}' for v in vals])
    print('POSITIVE_COVARIANCE',f'{vals[1]-vals[0]**2:.12f}')
    print('VERIFY_OK exact_rationals=yes independent_augmenting_path=yes')

if __name__=='__main__':main()
