"""Independent finite-level checks for periodic hierarchical bond percolation.
Run: python3 verify.py (Python standard library only).
"""
from fractions import Fraction as Q
from itertools import product


def renormalize(p, x):
    return 1 - (1-p)*(1-x*x)**2


def elementary_enumeration(p, x):
    # Five independent bonds: four descendant connectivities and one shortcut.
    probs = [x]*4+[p]
    total=Q(0)
    for bits in product((0,1), repeat=5):
        weight=Q(1)
        for bit,prob in zip(bits,probs):
            weight*=prob if bit else 1-prob
        if bits[4] or (bits[0] and bits[1]) or (bits[2] and bits[3]):
            total+=weight
    return total


def h(x):
    return (1-x)*(1+x)**2


def iterate(schedule, q, count):
    x=float(q)
    for i in range(count):
        x=renormalize(float(schedule[i%len(schedule)]),x)
    return x


def main():
    n=0
    for p in [Q(0),Q(1,5),Q(3,10),Q(1,2),Q(1)]:
        for q in [Q(0),Q(1,7),Q(1,3),Q(3,5),Q(1)]:
            assert renormalize(p,q)==elementary_enumeration(p,q)
            n+=1
    # Sharp maximum identity of the auxiliary cubic, checked at exact rationals.
    for j in range(201):
        x=Q(j,200)
        assert Q(32,27)-h(x)==(3*x-1)**2*(3*x+5)/27
        assert h(x)<=Q(32,27)
        n+=2
    # The mean-matched alternating and homogeneous schedules diverge qualitatively.
    alternating=[Q(3,10),Q(0)]
    homogeneous=[Q(3,20),Q(3,20)]
    assert (1-alternating[0])*(1-alternating[1]) < Q(729,1024)
    assert sum(alternating)==sum(homogeneous)
    assert renormalize(Q(3,20),Q(1,3))-Q(1,3)==-Q(2,405)
    n+=3
    for q in [0., 0.1, 0.3, 0.9]:
        assert iterate(alternating,q,4000)>1-1e-13
        n+=1
    assert 0.26 < iterate(homogeneous,0,10000)<0.27
    n+=1
    # Critical homogeneous profile has the nontrivial fixed point 1/3.
    assert renormalize(Q(5,32),Q(1,3))==Q(1,3)
    assert Q(1)-Q(5,32)==Q(27,32)
    n+=2
    print(f"PASS: {n} independent exact-rational/numerical assertions")

if __name__ == '__main__':
    main()
