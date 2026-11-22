"""Independent finite checks for cubic Dickson collision theorem.
Run: python3 verify_cubic.py (Python standard library only).
The proof of the infinite theorem is in RESULT.md; these are finite checks.
"""
from collections import Counter
from itertools import product


def legendre(a,p):
    r=pow(a%p,(p-1)//2,p)
    return 0 if r==0 else (1 if r==1 else -1)


def predicted(p,k,c):
    assert p>=3 and p%2==1 and c%p
    if p==3:
        return p**k if c%3==1 else 3**(k+1)
    e=legendre(-3,p)
    i=1+legendre(-c*pow(3,-1,p),p)
    return p**(k-1)*(2*p-e+i*((k-1)*(p-1)-1))


def direct_histogram(p,k,c):
    n=p**k
    h=Counter((x*x*x+c*x)%n for x in range(n))
    return sum(v*v for v in h.values())


def direct_pairs(p,k,c):
    n=p**k
    return sum((x*x*x+c*x-y*y*y-c*y)%n==0
               for x,y in product(range(n),repeat=2))


def main():
    cases=0
    max_n=0
    for p,max_k in ((3,8),(5,5),(7,4),(11,3),(13,3),(17,2)):
        for k in range(1,max_k+1):
            for r in range(1,p):
                for c in (r,r+p,r+2*p):
                    got=direct_histogram(p,k,c)
                    want=predicted(p,k,c)
                    assert got==want,(p,k,c,got,want)
                    if p**k<=100:
                        assert direct_pairs(p,k,c)==want,(p,k,c)
                    cases+=1
                    max_n=max(max_n,p**k)
    for p in (5,7,11,13,17):
        for k in range(1,5):
            e=legendre(-3,p)
            n=p**k
            # Coefficient character classes have exact collision difference.
            cs=([c for c in range(1,p) if legendre(-c*pow(3,-1,p),p)==-1],
                [c for c in range(1,p) if legendre(-c*pow(3,-1,p),p)==1])
            diff=predicted(p,k,cs[1][0])-predicted(p,k,cs[0][0])
            assert diff==2*p**(k-1)*((k-1)*(p-1)-1)
    print('PASS complete target histograms:',cases,'cases; max modulus',max_n)
    print('PASS direct ordered-pair comparisons for every modulus <=100')
    print('PASS sharp coefficient-class differences for 5 primes, 4 depths')

if __name__=='__main__':
    main()
