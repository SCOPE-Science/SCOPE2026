"""Exact finite-field verification of Frobenius membership for Moore determinants.
Usage: python verify_moore.py
Public reproducibility: only Python 3 standard library is required.
"""
from itertools import permutations
from collections import defaultdict

def moore(n, q, p):
    # The Moore determinant det(X_i**(q**j)), rows i, columns j.
    terms = defaultdict(int)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        exp=tuple(q**perm[i] for i in range(n))
        terms[exp]+= (-1)**inversions
    return {k:v%p for k,v in terms.items() if v%p}

def multiply(a,b,p,bound):
    result=defaultdict(int)
    for u,cu in a.items():
        for v,cv in b.items():
            w=tuple(i+j for i,j in zip(u,v))
            if max(w)<bound:
                result[w]=(result[w]+cu*cv)%p
    return {k:v for k,v in result.items() if v%p}

def nu(n,q,p,s):
    bound=p**s
    f=moore(n,q,p)
    a={(0,)*n:1}
    N=0
    while a:
        a=multiply(a,f,p,bound)
        if a:
            N+=1
        else:
            return N
    raise AssertionError('unreachable')

def main():
    tests=[(2,2,2,[1,2,3,4]),(2,3,3,[1,2,3]),
           (3,2,2,[2,3,4,5]),(3,3,3,[2,3,4]),
           (4,2,2,[3,4,5]),(2,4,2,[2,3,4]),(3,4,2,[4,5])]
    for n,q,p,s_values in tests:
        for s in s_values:
            D=q**(n-1)
            expected=max(0,p**s//D-1) if p**s>=D else 0
            # At s with p**s<D the determinant already lies in the Frobenius ideal.
            got=nu(n,q,p,s)
            assert got==expected,(n,q,p,s,got,expected)
            print(f'PASS n={n} q={q} p={p} s={s} nu={got}')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':main()

# Additional independent census: an n-tuple of elements of F_{q^s}
# is viewed as an n-by-s matrix over F_q; scalar projectivization
# divides each rank's count by q^s-1.

def matrix_rank(rows, p, s):
    a=[list(x) for x in rows]
    rank=0
    for col in range(s):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]%p),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[(u*inv)%p for u in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                c=a[i][col]
                if c:a[i]=[(v-c*u)%p for v,u in zip(a[i],a[rank])]
        rank+=1
    return rank

def gaussian(n,r,q):
    from math import prod
    numerator=prod(q**n-q**i for i in range(r))
    denominator=prod(q**r-q**i for i in range(r))
    return numerator//denominator

def arithmetic_census():
    from itertools import product
    for n,p,s in [(3,2,1),(3,2,2),(3,2,3),(4,2,2),(3,3,2)]:
        field_elems=list(product(range(p),repeat=s))
        hist={}
        for vectors in product(field_elems,repeat=n):
            r=matrix_rank(vectors,p,s)
            if r:hist[r]=hist.get(r,0)+1
        divisor=p**s-1
        projective={r:c//divisor for r,c in hist.items()}
        expected={r:gaussian(n,r,p)*__import__('math').prod(p**s-p**i for i in range(1,r)) for r in range(1,min(n,s)+1)}
        assert projective==expected,(n,p,s,projective,expected)
        print(f'PASS projective rank distribution n={n} q={p} s={s}: {projective}')
    print('ARITHMETIC_CHECKS_PASSED')

if __name__=='__main__':arithmetic_census()
