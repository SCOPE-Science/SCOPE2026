"""Standalone exact reproducibility checks for the major-index/consecutive-pattern extremum."""
from itertools import permutations
from fractions import Fraction
from math import factorial

def reduce_pattern(xs):
    order = sorted(xs)
    ranks = {v:i+1 for i,v in enumerate(order)}
    return tuple(ranks[v] for v in xs)

def theoretical(n, sigma):
    m=len(sigma)
    N=n-m+1
    assert n>=m>=2
    v=Fraction(0)
    for start in range(1,N+1):
        for k in range(1,m):
            v += (start+k-1)*(int(sigma[k-1]>sigma[k])-Fraction(1,2))
        if start>1:
            v += (start-1)*Fraction(m+1-2*sigma[0],2*(m+1))
        if start<N:
            v += (start+m-1)*Fraction(2*sigma[-1]-m-1,2*(m+1))
    return v/factorial(m)

def upper(n,m):
    N=n-m+1
    return Fraction((m-1)*n*(N*(m-1)+2),4*(m+1)*factorial(m))

def assert_all():
    count=0
    for n in range(2,8):
        sums={m:{p:0 for p in permutations(range(1,m+1))} for m in range(2,n+1)}
        allmaj=0
        for pi in permutations(range(1,n+1)):
            maj=sum(i for i in range(1,n) if pi[i-1]>pi[i]);allmaj+=maj
            for m in range(2,n+1):
                for j in range(n-m+1):
                    sums[m][reduce_pattern(pi[j:j+m])] += maj
        mu=Fraction(allmaj,factorial(n))
        assert mu==Fraction(n*(n-1),4);count+=1
        for m in range(2,n+1):
            bound=upper(n,m)
            for sig,total in sums[m].items():
                ec=Fraction(total,factorial(n))-mu*Fraction(n-m+1,factorial(m))
                assert ec==theoretical(n,sig), (n,m,sig,ec,theoretical(n,sig));count+=1
                assert -bound<=ec<=bound;count+=1
                assert (ec==bound)==(sig==tuple(range(m,0,-1)));count+=1
                assert (ec==-bound)==(sig==tuple(range(1,m+1)));count+=1
    # Independent exact check of the ascent-defect charging and positive coefficients
    for m in range(2,9):
        for sig in permutations(range(1,m+1)):
            asc=[j for j in range(1,m) if sig[j-1]<sig[j]]
            assert m-sig[0]<=sum(m-j for j in asc);count+=1
            assert sig[-1]-1<=sum(asc);count+=1
    for m in range(2,20):
        for n in range(m,60):
            N=n-m+1
            A=Fraction(N*(N-1),2)
            B=Fraction((N-1)*(N+2*m-2),2)
            for j in range(1,m):
                W=Fraction(N*(N+2*j-1),2)
                delta=(m+1)*W-A*(m-j)-B*j
                assert delta==Fraction(N*(N-1),2)+j*(2*N+m-1)
                assert delta>0
                count+=1
    # Two exact examples of opposing pattern signs within same number of descents
    assert theoretical(6,(1,3,2))==Fraction(7,12)
    assert theoretical(6,(2,3,1))==Fraction(-1,6)
    print(f"PASS {count} exact assertions")
if __name__=='__main__':assert_all()
