"""Exact rational checks for two-community continuous-time weighted-median flow.

Run: python verify.py.  Standard library only.
These checks corroborate algebra and boundary behavior; the analytic proof
handles arbitrary finite part sizes, all admissible weights, and all real data.
"""
from fractions import Fraction as Q
from itertools import product
import random


def med(vals, weights):
    assert sum(weights) == 1
    options = sorted(set(vals))
    valid = [z for z in options
             if sum(w for v,w in zip(vals,weights) if v < z) <= Q(1,2)
             and sum(w for v,w in zip(vals,weights) if v > z) <= Q(1,2)]
    if len(valid) != 1:
        return None
    # A nontrivial interval of minimizers is possible with a singleton
    # observed value if half the weight lies on either side; reject that too.
    z=valid[0]
    below=sum(w for v,w in zip(vals,weights) if v<z)
    above=sum(w for v,w in zip(vals,weights) if v>z)
    if below >= Q(1,2) or above >= Q(1,2):
        return None
    return z


def check(a,b,wa,wb):
    u=med(a,wa); v=med(b,wb)
    if u is None or v is None:
        return 0
    c=(u+v)/2
    for q in (Q(1),Q(1,2),Q(2,3),Q(1,7),Q(1,19)):
        A=[c+(u-v)*q*q/2+(z-u)*q for z in a]
        B=[c-(u-v)*q*q/2+(z-v)*q for z in b]
        assert med(A,wa)==c+(u-v)*q*q/2
        assert med(B,wb)==c-(u-v)*q*q/2
        for x,z in zip(A,a):
            deriv=-(u-v)*q*q-(z-u)*q
            assert deriv==med(B,wb)-x
        for x,z in zip(B,b):
            deriv=(u-v)*q*q-(z-v)*q
            assert deriv==med(A,wa)-x
        assert all(A[i]-A[j]==q*(a[i]-a[j])
                   for i in range(len(a)) for j in range(len(a)))
        assert all(B[i]-B[j]==q*(b[i]-b[j])
                   for i in range(len(b)) for j in range(len(b)))
    return 1


def main():
    ncheck=0
    # Exhaustive small integer opinions with uniform, odd part sizes.
    for m,n in [(1,1),(1,3),(3,1),(3,3)]:
        wa=[Q(1,m)]*m; wb=[Q(1,n)]*n
        for vals in product((-1,0,1),repeat=m+n):
            ncheck+=check(list(map(Q,vals[:m])),list(map(Q,vals[m:])),wa,wb)
    # Deterministic heterogeneous row-weights and arbitrary part sizes.
    rng=random.Random(234028)
    for _ in range(450):
        m=rng.randint(1,8); n=rng.randint(1,8)
        a=[Q(rng.randint(-20,20),rng.randint(1,9)) for _ in range(m)]
        b=[Q(rng.randint(-20,20),rng.randint(1,9)) for _ in range(n)]
        ra=[rng.randint(1,10) for _ in range(m)]
        rb=[rng.randint(1,10) for _ in range(n)]
        wa=[Q(w,sum(ra)) for w in ra]
        wb=[Q(w,sum(rb)) for w in rb]
        ncheck+=check(a,b,wa,wb)
    # Non-unique median boundary on K_{2,2}; closest observed neighbor
    # opinions are selected (not projection onto the intervening interval).
    wa=wb=[Q(1,2),Q(1,2)]
    for q in (Q(1),Q(1,2),Q(1,4),Q(1,100)):
        h=q*q
        a=[Q(-3,2)+h/2,Q(3,2)-h/2]
        b=[Q(-3,2)-h/2,Q(3,2)+h/2]
        closest=lambda x,options: min(options,key=lambda z:(abs(z-x),z))
        assert [closest(x,b)-x for x in a]==[-h,h]
        assert [closest(x,a)-x for x in b]==[h,-h]
        assert a[0]<0<a[1] and b[0]<0<b[1]
    print(f'VERIFY_OK exact_cases={ncheck} boundary_cases=4')

if __name__=='__main__':
    main()
