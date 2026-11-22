"""Direct finite checks for square-zero Yang--Baxter automorphism theorem.
Only standard library. Run python verification.py (p=2,n<=3; p=3,n=2).
"""
from itertools import product, permutations
from collections import Counter
from fractions import Fraction
from math import factorial


def check(p,n,r):
    assert 2*r<=n and r>=1
    points=list(product(range(p),repeat=n))
    idx={x:i for i,x in enumerate(points)}
    def add(x,y):return tuple((a+b)%p for a,b in zip(x,y))
    # matrix a sends basis r..2r-1 into basis 0..r-1, zero elsewhere
    def alpha(x):return tuple((x[i+r] if i<r else 0) for i in range(n))
    test=[[(idx[add(y,alpha(x))]) for y in points] for x in points]
    count=0
    hist=Counter()
    N=len(points)
    for perm in permutations(range(N)):
        # necessary condition at y=zero for every x; cheap short circuit
        if any(perm[test[i][0]] != test[perm[i]][perm[0]] for i in range(N)):
            continue
        if any(perm[test[i][j]] != test[perm[i]][perm[j]] for i in range(N) for j in range(N)):
            continue
        count+=1
        hist[sum(k==perm[k] for k in range(N))]+=1
    s=p**(n-2*r)
    gl=1
    for j in range(r):gl*=p**r-p**j
    expect=(p**r)**(p**(n-r))*factorial(s)**(p**r)*gl
    assert count==expect,(p,n,r,count,expect)
    # test exact aggregate fixed point count from the finite PGF theorem
    # r=1 in these exhaustive cases; GL_1(p) has identity and other scalars.
    if r==1:
        expected=Counter()
        for mult,d in ((1,1),(p-2,0)):
            # base permutation of every beta-fixed fiber, W-translation independently
            # use exact combinatorial factorial moments expansion
            k=p**d
            # PGF for fixed POINTS (one successful fixed coset = p^d fixed points)
            # sum_{j=0}^s ((t^k-1)/k)^j/j!, raised to k
            pol=[Fraction(0)]*(s+1)
            for j in range(s+1):
                factor=Fraction(1,k**j*factorial(j))
                from math import comb
                for h in range(j+1):
                    pol[h]+=factor*comb(j,h)*(-1)**(j-h)
            conv={0:Fraction(1)}
            for _ in range(k):
                nc=Counter()
                for a,ca in conv.items():
                    for h,ch in enumerate(pol):nc[a+h]+=ca*ch
                conv=nc
            for h,prob in conv.items():
                expected[h*k]+=Fraction(mult,gl)*prob
        assert {f:v for f,v in expected.items() if v}=={f:Fraction(v,count) for f,v in hist.items()},(expected,hist)
    print(f'CHECKED p={p} n={n} rank={r} |Aut|={count}; fixed_histogram={dict(sorted(hist.items()))}')

if __name__=='__main__':
    check(2,2,1)
    check(2,3,1)
    check(3,2,1)
    print('YB_SQUARE_ZERO_AUTOMORPHISMS_VERIFIED')
