"""Exact integer witness and auxiliary sensitivity checks for cyclic five-point medians."""
from fractions import Fraction
from random import Random

# All indices are zero based. Each row is a permutation of 1,...,n.
WITNESSES = {
 10: [4,8,10,1,5,7,2,3,9,6],
 11: [3,6,9,11,5,7,10,2,1,4,8],
 12: [7,11,9,1,12,4,5,2,6,3,10,8],
 13: [8,10,3,1,11,6,5,7,12,2,9,13,4],
 14: [10,12,4,14,5,9,3,6,1,8,2,13,7,11],
 15: [13,4,9,1,11,3,6,5,12,2,8,15,10,14,7],
 16: [6,12,9,13,16,4,14,7,11,5,15,2,1,8,3,10],
 17: [10,17,6,13,4,11,15,5,8,16,3,1,2,7,14,9,12],
 18: [6,1,4,18,11,14,9,13,10,12,8,17,3,7,15,16,2,5],
 19: [13,18,6,2,16,19,7,3,10,9,5,11,17,4,8,1,15,14,12],
}
GADGET = [31,44,7,92,38,40,4,60,25,32]

def median_index(a, i):
    n = len(a)
    return sorted(((a[(i+j)%n], (i+j)%n) for j in range(-2,3)))[2][1]

def median(a):
    return [a[median_index(a,i)] for i in range(len(a))]

def variation(a):
    return sum(abs(a[(i+1)%len(a)]-a[i]) for i in range(len(a)))

def witness(n):
    if 10 <= n < 20:
        a = WITNESSES[n]
        h = [int(i < n//2) for i in range(n)]
    elif n >= 20:
        a = GADGET + [q+100 for q in GADGET] + [1000+i for i in range(n-20)]
        h = [int(i<=4 or i>=15) for i in range(n)]
    else:
        raise ValueError('No saturation witness exists below ten vertices')
    return a,h

def exact_witness(n):
    a,h = witness(n)
    eps = Fraction(1,4)
    assert len(a)==len(h)==n and len(set(a))==n
    assert variation(h)==2
    y=[Fraction(z,1) for z in a]
    z=[y[i]+eps*h[i] for i in range(n)]
    m1=median(y);m2=median(z)
    assert variation([m2[i]-m1[i] for i in range(n)])==5*eps*variation(h)
    mask=[h[median_index(a,i)] for i in range(n)]
    assert variation(mask)==10
    return variation(mask)

def check_edge_selection_bound(a):
    n=len(a)
    idx=[median_index(a,i) for i in range(n)]
    for j in range(n):
        # Each selected-coordinate difference crosses a source edge no
        # more than five times. Representatives are lifted to nearby integers.
        used=0
        for i in range(n):
            s=next(i+k for k in range(-2,3) if (i+k)%n==idx[i])
            t=next(i+1+k for k in range(-2,3) if (i+1+k)%n==idx[(i+1)%n])
            lo,hi=sorted((s,t))
            if any(k%n==j for k in range(lo,hi)):
                used+=1
        assert used<=5,(n,j,used)

if __name__=='__main__':
    for n in range(10,20):
        exact_witness(n)
        print('EXACT_FINITE_WITNESS_PASS',n)
    for n in (20,21,22,25,31,50,101,200):
        exact_witness(n)
        print('EXACT_UNIFORM_GADGET_PASS',n)
    rng=Random(47)
    for n in range(5,28):
        for _ in range(100):
            a=rng.sample(range(5000),n)
            check_edge_selection_bound(a)
            b=rng.sample(range(5000),n)
            left=variation([p-q for p,q in zip(median(a),median(b))])
            right=5*variation([p-q for p,q in zip(a,b)])
            assert left<=right
        print('RANDOM_CHAMBER_AND_TWO_INPUT_UPPER_PASS',n)
    print('ALL_FIVE_POINT_CYCLIC_MEDIAN_EXACT_CHECKS_PASS')
