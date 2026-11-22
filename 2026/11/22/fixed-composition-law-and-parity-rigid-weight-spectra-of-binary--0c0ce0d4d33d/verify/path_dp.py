"""Independent exact weighted killed-walk and shape/moment checks."""
from collections import defaultdict
from math import comb
from fractions import Fraction


def candidate(m):
    # Coefficient array of the two-signed reflected-walk formula.
    a = defaultdict(int)
    for j in range(m):
        a[2*j+1] += 2*comb(m-1,j)**2
    for j in range(m-1):
        a[2*j+2] += 2*comb(m-1,j)*comb(m-1,j+1)
    return dict(a)


def positive_walk_dp(m):
    # Positive walks: first pair is (1,0) (weight u), then 4 pair choices.
    curr={(1,1):1}  # (height, Hamming weight) : multiplicity
    for _ in range(1,m):
        next_states=defaultdict(int)
        for (h,k),v in curr.items():
            for left,right in ((0,0),(0,1),(1,0),(1,1)):
                h2=h+left-right
                if h2>0:
                    next_states[(h2,k+left+right)]+=v
        curr=next_states
    out=defaultdict(int)
    for (_,k),v in curr.items():out[k]+=2*v
    return dict(out)


def verify():
    for m in range(1,41):
        a=candidate(m)
        assert positive_walk_dp(m)==a, ('walk',m)
        total=sum(a.values())
        assert total == comb(2*m,m), ('total',m)
        assert all(a[k] == a[2*m-k] for k in range(1,2*m)), ('symmetry',m)
        mean=Fraction(sum(k*v for k,v in a.items()),total)
        var=Fraction(sum((k-m)**2*v for k,v in a.items()),total)
        assert mean==m
        assert var==Fraction(m*(m-1),2*m-1), ('variance',m)
        for k in range(2,2*m-1):
            delta=a[k]**2-a[k-1]*a[k+1]
            if k%2==0:assert delta==0,('even equality',m,k)
            else:assert delta>0,('odd strict',m,k)
        b=defaultdict(int)
        for k,v in a.items():b[k]+=v;b[k+1]+=v
        for k in range(2,2*m):
            assert b[k]**2>b[k-1]*b[k+1],('odd-length strict',m,k)
    print('PASS: independent weighted walks, totals, symmetry, variance, and log-concavity for m=1..40')

if __name__=='__main__':verify()
