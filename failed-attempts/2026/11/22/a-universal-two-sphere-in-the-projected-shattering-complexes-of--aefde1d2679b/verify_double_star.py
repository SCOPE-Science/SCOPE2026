"""Exhaustive vertex-projected shattering check for proper ternary double-star colourings."""
from itertools import product, combinations
from math import comb

def check(a,b):
    n=a+b+2
    edges=[(0,1)]+[(0,i) for i in range(2,2+a)]+[(1,i) for i in range(2+a,n)]
    good=[x for x in product(range(3),repeat=n) if all(x[i]!=x[j] for i,j in edges)]
    assert len(good)==3*(2**(n-1))
    num=0; coeff=[0]*(n+1)
    for k in range(n+1):
        for S in combinations(range(n),k):
            observed=False
            # Use full exact trace sets for each fixed queried target colour assignment.
            proj={tuple(x[i] for i in S) for x in good}
            for target in product(range(3),repeat=k):
                trace={tuple(int(row[i]==target[i]) for i in range(k)) for row in proj}
                if len(trace)==(1<<k):
                    observed=True; break
            expected=not (0 in S and 1 in S and any(2<=i<2+a for i in S) and any(2+a<=i<n for i in S))
            assert observed==expected,(a,b,S,observed,expected)
            if observed: coeff[k]+=1; num+=1
    predicted=[]
    for k in range(n+1):
        x=comb(a+b,k)+2*(comb(a+b,k-1) if 0<=k-1<=a+b else 0) if 0<=k<=a+b else 2*(comb(a+b,k-1) if 0<=k-1<=a+b else 0)
        if 0<=k-2<=a: x+=comb(a,k-2)
        if 0<=k-2<=b: x+=comb(b,k-2)
        if k==2:x-=1
        predicted.append(x)
    assert coeff==predicted,(coeff,predicted)
    return n,len(good),num,coeff

if __name__=='__main__':
    for pair in ((1,1),(1,2),(2,2),(2,3),(3,3)):
        print(pair,check(*pair),flush=True)
    print('PASS: exhaustive independent proper-colouring traces and polynomial checks')
