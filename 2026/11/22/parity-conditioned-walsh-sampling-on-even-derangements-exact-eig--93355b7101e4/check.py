"""Exact small-case checks for even-derangement first Walsh-band sampling."""
from itertools import permutations
from fractions import Fraction
from math import factorial

def derangement_count(n):
    return sum((-1)**k * (factorial(n)//factorial(k)) for k in range(n+1))

def even_parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

def run():
    tests=0
    for n in range(4,9):
        ps=[p for p in permutations(range(n)) if all(p[i]!=i for i in range(n)) and even_parity(p)]
        e=len(ps); d=derangement_count; s=(-1)**(n-1)
        assert 2*e==d(n)+s*(n-1); tests+=1
        # Direct samples: count every prescribed pair of off-diagonal edges once.
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        hist={(u,v):0 for u in edges for v in edges}
        one={u:0 for u in edges}
        for p in ps:
            es=[(i,p[i]) for i in range(n)]
            for u in es: one[u]+=1
            for u in es:
                for v in es: hist[u,v]+=1
        a=Fraction(d(n-2)-s*(n-3),2*e)
        b=Fraction(d(n-2)+d(n-3)+s,2*e)
        c=Fraction(d(n-2)+2*d(n-3)+d(n-4),2*e)
        for u in edges:
            i,j=u
            assert Fraction(one[u],e)==Fraction(1,n-1);tests+=1
            for v in edges:
                k,l=v
                if i==k or j==l:target=Fraction(1,n-1) if u==v else 0
                elif u==(l,k):target=a
                elif k==j or l==i:target=b
                else:target=c
                assert Fraction(hist[u,v],e)==target,(n,u,v,target,hist[u,v]);tests+=1
        alpha=Fraction(1,n-1)+c
        beta=a-2*b+c
        assert beta==Fraction(d(n-4)-s*(n-1),d(n)+s*(n-1));tests+=1
        lp=alpha+beta;lm=alpha-beta
        ds=n*(n-3)//2;da=(n-1)*(n-2)//2
        assert ds*lp+da*lm==Fraction(n*(n-2),n-1);tests+=1
        # Test the covariance operator on explicit zero-row/column matrices.
        for seed in range(8):
            raw=[[0 if i==j else ((i+3*j+seed*7)**2%17)-8 for j in range(n)] for i in range(n)]
            # Exact orthogonal projection onto the zero-row/column subspace
            # obtained by symmetrically eliminating the potential component:
            # make row/column-zero test vectors as cycle incidence differences.
            a0,b0,c0,d0=0,1,2,3
            raw=[[0 for j in range(n)] for i in range(n)]
            if seed%2==0:
                # Oriented four-cycle with zero row/column sums.
                for i,j,v in [(a0,b0,1),(a0,d0,-1),(c0,b0,-1),(c0,d0,1)]:raw[i][j]=v
            else:
                # Directed alternating six-cycle, no diagonal cells.
                for i,j,v in [(0,1,1),(0,2,-1),(1,2,1),(1,0,-1),(2,0,1),(2,1,-1)]:raw[i][j]=v
            assert all(sum(r)==0 for r in raw)
            assert all(sum(raw[i][j] for i in range(n))==0 for j in range(n))
            for i,j in edges:
                # centered covariance on U: E[(X_ij-p)Z] = E[X_ij Z]
                observed=Fraction(sum((int(p[i]==j))*sum(raw[k][p[k]] for k in range(n)) for p in ps),e)
                expected=alpha*raw[i][j]+beta*raw[j][i]
                assert observed==expected,(n,seed,i,j,observed,expected);tests+=1
        print('n=',n,'even derangements=',e,'lambda_sym=',lp,'lambda_skew=',lm)
    print('PASS; exact assertions:',tests)

if __name__=='__main__':run()
