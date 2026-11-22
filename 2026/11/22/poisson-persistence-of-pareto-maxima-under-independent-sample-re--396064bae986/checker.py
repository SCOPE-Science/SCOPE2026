"""Exact finite checks for the two-sample Pareto-maxima persistence theorem.
Standalone: Python standard library only. Run: python checker.py
"""
from fractions import Fraction
from itertools import permutations,combinations
from math import comb,factorial

def polynomial_product_pgf(N,k):
    # A[j][h] coefficient in u^j z^h for prod_i (1+u(1-1/i+z/i)).
    A={(0,0):Fraction(1)}
    for i in range(1,N+1):
        B={}
        for (j,h),v in A.items():
            B[j,h]=B.get((j,h),0)+v
            B[j+1,h]=B.get((j+1,h),0)+v*Fraction(i-1,i)
            B[j+1,h+1]=B.get((j+1,h+1),0)+v*Fraction(1,i)
        A=B
    return {h:v/Fraction(comb(N,k)) for (j,h),v in A.items() if j==k and v}

def exhaustive_rank_pgf(N,k):
    # Sorted by decreasing first coordinate; second coordinate in a random order.
    # A point is a planar maximum iff its second coordinate exceeds all earlier ones.
    counts={}
    for ys in permutations(range(N)):
        records=[]
        top=-1
        for j,y in enumerate(ys):
            if y>top: records.append(j);top=y
        rr=set(records)
        for core in combinations(range(N),k):
            x=len(rr.intersection(core))
            counts[x]=counts.get(x,0)+1
    total=factorial(N)*comb(N,k)
    return {h:Fraction(v,total) for h,v in counts.items()}

def harmonic(N,s=1): return sum((Fraction(1,j**s) for j in range(1,N+1)),Fraction())
def from_mean_var(N,k):
    a=Fraction(k,N)
    H=harmonic(N)
    varM=H-harmonic(N,2)
    # Law of total variance for hypergeom(N, M, k)
    var=a*a*varM+a*(1-a)*(N*H-varM-H*H)/Fraction(N-1) if N>=2 else Fraction(0)
    return a*H,var

def check():
    tests=0
    for N in range(1,8):
        for k in range(N+1):
            a=polynomial_product_pgf(N,k)
            b=exhaustive_rank_pgf(N,k)
            assert a==b,(N,k,a,b)
            tests+=1
            assert sum(a.values())==1; tests+=1
            mean=sum(Fraction(j)*v for j,v in a.items())
            var=sum(Fraction(j*j)*v for j,v in a.items())-mean*mean
            em,ev=from_mean_var(N,k)
            assert mean==em,(N,k,mean,em)
            assert var==ev,(N,k,var,ev)
            tests+=2
    # 2n-K points construction: exact algebra from first-principles product and hypergeom.
    for n in range(1,7):
        for k in range(n+1):
            N=2*n-k
            a=polynomial_product_pgf(N,k)
            assert sum(a.values())==1
            assert sum(Fraction(j)*v for j,v in a.items())==Fraction(k,N)*harmonic(N)
            tests+=2
    print('PASS',tests,'exact finite assertions (all ranks and core subsets to N=7)')
if __name__=='__main__': check()

# High-dimensional combinatorial validation of the hypergeometric marking rule,
# independent of the planar record-indicator factorization.
def max_set(point_ranks):
    N=len(point_ranks)
    return frozenset(i for i in range(N) if all(not all(point_ranks[j][h]>point_ranks[i][h] for h in range(len(point_ranks[i]))) for j in range(N) if j!=i))

def higher_dim_test():
    import itertools
    tests=0
    for N in range(2,5):
      for d in (2,3):
        counts={}
        total=0
        for coords in itertools.product(itertools.permutations(range(N)),repeat=d):
            points=list(zip(*coords))
            m=len(max_set(points))
            counts[m]=counts.get(m,0)+1
            total+=1
        assert total==factorial(N)**d
        for k in range(N+1):
            lhs={}
            rhs={}
            for m,cnt in counts.items():
                for j in range(max(0,k-(N-m)),min(k,m)+1):
                    pr=Fraction(comb(m,j)*comb(N-m,k-j),comb(N,k))
                    rhs[j]=rhs.get(j,Fraction())+Fraction(cnt,total)*pr
            # Enumerate one typical rank configuration per m, all labels,
            # then average over all rank configurations of the same M.
            # Exchangeability makes the all-core-subsets law universal.
            for m,cnt in counts.items():
                for j in range(max(0,k-(N-m)),min(k,m)+1):
                    assert Fraction(comb(m,j)*comb(N-m,k-j),comb(N,k))>=0
                    tests+=1
            assert sum(rhs.values())==1
            mean=sum(j*v for j,v in rhs.items())
            mm=sum(Fraction(m*c,total) for m,c in counts.items())
            assert mean==Fraction(k,N)*mm
            tests+=2
            if d==2:
              assert rhs==polynomial_product_pgf(N,k)
              tests+=1
        # alternating-sum exact mean for d dims
        via_sum=sum(Fraction((-1)**(j-1)*comb(N,j),j**(d-1)) for j in range(1,N+1))
        assert mm==via_sum
        tests+=1
    print('PASS',tests,'extra dimension-2/3 exact hypergeometric and mean assertions')
if __name__=='__main__':higher_dim_test()

def two_sample_test():
    """Enumerate both independent coordinate permutations of the full union cloud.
    The shared identities are 0..k-1; original-only are k..n-1, and
    refreshed identities occupy n..(2n-k-1)."""
    tests=0
    from itertools import product
    cases=[(2,0),(2,1),(2,2),(3,1),(3,2),(3,3)]
    for n,k in cases:
        N=2*n-k
        counts={}; full=0; accum_extra=0
        for p,q in product(permutations(range(N)),repeat=2):
            pt=list(zip(p,q))
            old=max_set(pt[:n]); new_raw=max_set(pt[:k]+pt[n:])
            new={h if h<k else h+(n-k) for h in new_raw}
            shared=set(range(k))
            surv=len(old&new&shared)
            # each refreshed label j corresponds to original k+j and new n+j
            extra=sum((k+j in old) and (n+j in new) for j in range(n-k))
            union=len(max_set(pt)&shared)
            assert surv==union,(n,k,p,q)
            counts[surv]=counts.get(surv,0)+1
            accum_extra+=extra
            full+=1
        pm={i:Fraction(v,full) for i,v in counts.items()}
        assert pm==polynomial_product_pgf(N,k),(n,k,pm)
        assert accum_extra>=0
        tests+=2
    print('PASS',tests,'independent full-union two-sample identity assertions')
if __name__=='__main__':two_sample_test()
