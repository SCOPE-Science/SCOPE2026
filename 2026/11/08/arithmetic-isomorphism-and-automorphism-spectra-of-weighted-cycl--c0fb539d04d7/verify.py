"""Independent finite-group exponent-action checks for weighted cyclic evolution algebras.

All weights are represented by exponents in the cyclic multiplicative group of size q-1.
This avoids relying on a particular finite-field polynomial basis.
"""
from collections import Counter
from itertools import product
from math import gcd


def transform(word, m, shift, scales):
    n=len(word)
    # First move basis indices by shift, then scale each corresponding natural basis.
    # For the output basis e'_i=omega^{scales[i]} e_{i+shift}, its weight is
    # a_{i+shift} omega^{2 scales[i]-scales[i+1]}.
    return tuple((word[(i+shift)%n]+2*scales[i]-scales[(i+1)%n])%m for i in range(n))


def orbit_counts(n, m):
    # Generate the same full monomial orbit by the n elementary scalings and the rotation.
    words=set(product(range(m),repeat=n)); dist=Counter()
    while words:
        w=next(iter(words)); frontier=[w]; words.remove(w); size=0
        while frontier:
            x=frontier.pop(); size+=1
            y=x[1:]+x[:1]
            if y in words:
                words.remove(y);frontier.append(y)
            for i in range(n):
                a=list(x)
                a[i]=(a[i]+2)%m
                a[(i-1)%n]=(a[(i-1)%n]-1)%m
                y=tuple(a)
                if y in words:
                    words.remove(y);frontier.append(y)
        assert n*m**n%size==0
        aut=n*m**n//size
        dist[aut]+=1
    return dict(dist)


def prediction(n,m):
    g=gcd(m,2**n-1);seen=set(); dist=Counter()
    for a in range(g):
        if a in seen:continue
        orbit=set(); z=a
        while z not in orbit:
            orbit.add(z);z=2*z%g
        seen |=orbit
        assert n%len(orbit)==0
        dist[g*n//len(orbit)]+=1
    return dict(dist)


def check_phi4_operator(n):
    assert n%2==0 and n>=2
    m=3
    a=[0]*(n-1)+[1] # 1 is a fixed primitive cube-root exponent
    def F_exp(i):
        if i<n-2:return ((i+2)%n,0)
        if i==n-2:return (0,1)
        return (1,2)
    # Verify F(e_i)^2=F(e_i^2) as exponent-and-index equalities.
    for i in range(n):
        j,t=F_exp(i)
        rhs_index, rhs_t=F_exp((i+1)%n)
        lhs=(j+1)%n, (2*t+a[j])%m
        rhs=(rhs_index,(rhs_t+a[i])%m)
        assert lhs==rhs,(n,i,lhs,rhs)
    # Follow all basis images through powers, checking order 3n/2 and F^(n/2).
    def power(k,i):
        out=i;v=0
        for _ in range(k):
            out,d=F_exp(out);v=(v+d)%3
        return out,v
    for i in range(n):
        assert power(n//2,i)==(i,1 if i%2==0 else 2)
        assert power(3*n//2,i)==(i,0)
    assert any(power(n//2,i)!=(i,0) for i in range(n))



def check_direct_f4_dimension_two():
    """Directly enumerate all invertible F4-linear maps, not just monomial ones."""
    def multiply(x, y):
        if x==0 or y==0:return 0
        # F4* = <omega>, encoding 1=omega^0, 2=omega, 3=omega^2.
        return 1 + ((x-1)+(y-1))%3
    def square(v, a):
        # e0^2=a0 e1 and e1^2=a1 e0 over characteristic two.
        return (multiply(multiply(v[1],v[1]),a[1]),
                multiply(multiply(v[0],v[0]),a[0]))
    def lin(M,v):
        return (multiply(M[0][0],v[0]) ^ multiply(M[0][1],v[1]),
                multiply(M[1][0],v[0]) ^ multiply(M[1][1],v[1]))
    mats=[]
    for A,B,C,D in product(range(4), repeat=4):
        if multiply(A,D)==multiply(B,C):continue
        mats.append(((A,B),(C,D)))
    assert len(mats)==180
    words=list(product((1,2,3),repeat=2))
    counts={}
    for a in words:
        matched=set()
        for b in words:
            for M in mats:
                x=lin(M,(1,0)); y=lin(M,(0,1))
                # True mixed products in the b-algebra.
                mixed=(multiply(b[1],multiply(x[1],y[1])),
                       multiply(b[0],multiply(x[0],y[0])))
                if mixed!=(0,0):continue
                if square(x,b)!=lin(M,(0,a[0])):continue
                if square(y,b)!=lin(M,(a[1],0)):continue
                matched.add(b);counts[(a,b)]=counts.get((a,b),0)+1
    # There are three normalized invariant-zero words and six nonzero words.
    # In dimension two, the two isomorphism classes have orbit sizes 3 and 6.
    groups=[]
    remaining=set(words)
    while remaining:
        a=next(iter(remaining))
        orbit={b for b in words if (a,b) in counts}
        assert orbit<=remaining
        aut=counts[(a,a)]
        groups.append((len(orbit),aut))
        remaining-=orbit
    assert sorted(groups)==[(3,6),(6,3)],groups
    assert all(counts[(a,b)]==counts[(a,a)] for (a,b) in counts)
    return len(mats)

def main():
    tests=0
    for n in range(2,9):
        for m in range(1,9):
            if m**n>50000:continue
            actual=orbit_counts(n,m)
            expected=prediction(n,m)
            assert actual==expected,(n,m,actual,expected)
            tests+=1
            if m==3:
                if n%2==0:assert actual=={3*n:1,3*n//2:1}
                else:assert actual=={n:1}
    for n in range(2,101,2):check_phi4_operator(n)
    direct=check_direct_f4_dimension_two()
    print('VERIFY_OK',tests,'independent orbit enumerations, 50 exact F4 operator checks, and', direct, 'direct GL2(F4) maps checked')

if __name__=='__main__':main()
