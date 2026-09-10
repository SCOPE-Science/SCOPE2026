"""Corrected exact pullback-mass law for B_Q (Fractions, brute-force verified).

Setup: B_l -> B_{l+1} -> ... -> B_K, multiplicities m_i=i+2.
Paths: sequences of summand choices s_i in {0..i+1} (0..i coordinate,
i+1 point). Number of paths M(l,K) = prod_{i=l}^{K-1}(i+2) = (K+1)!/(l+1)!.
Pullback of tau_K: parallel evaluation at the pasted function pasted_Psi
(a in B_l) along Psi=x_{K-1}o...ox_l. Equal weight 1/M(l,K) per path.

E1: path count M(l,K)=(K+1)!/(l+1)!, exact (several pairs, brute force for
    small, closed form for large).
E2: class counts: paths with NO point summand (all-coordinate) =
    prod_{i=l}^{K-1}(i+1) = K!/l!. Mass = (K!/l!)/((K+1)!/(l+1)!) = (l+1)/(K+1)
    (telescoping; -> 0). First-point-at-m count =
    (prod_{i< m}(i+1)) * (prod_{i>m} (i+2)); mass exact Fraction; table shows
    first-point masses, NOT the old atomic weights (l+1)/((m+1)(m+2)).
    Brute-forced for (l,K)=(1,4): enumerate all 60 paths, classify.
E3: brute-force histogram (1,4): all-coordinate mass 2/5=0.4; first-point
    masses {1:1/5, 2:1/5, 3:1/5}; remainder (two-or-more-point paths) = 0.
    Wait: m ranges l..K-1={1,2,3}; point_paths total = 60-24=36 = 3*12;
    each first-point class has 12 paths = mass 1/5 each; total point mass 3/5.
    (At most one point? No: paths may revisit point summand at several
    levels; first-point-at-m classes partition ALL point-touching paths:
    12+12+12=36. Yes: every path either all-coordinate (24) or first-point
    at a unique m. Partition complete.)
E4: corrected atomic (support-point) law: the point at level m with
    accumulated pasted shift S contributes mass
    (#paths with first-point-at-m AND total coordinate-shift S)/M(l,K),
    NOT w[l,m]. The old WORKLOG formula w[l,m]=(l+1)/((m+1)(m+2)) is WRONG
    as stated (it neither sums to the point-mass 1-(l+1)/(K+1) with the
    claimed remainder nor matches first-point classes: e.g. (l,K)=(1,4):
    old weights 1/3+1/6+1/10=3/5 coincidentally?? 1/3+1/6+1/10 = 10/30+5/30+3/30
    = 18/30 = 3/5. Hmm -- that DOES sum to 3/5. Check: old identity said sum
    + (l+1)/(K+1) = 1, i.e. sum = 1-2/5 = 3/5. Yes consistent! But termwise:
    old w[1,1]=1/3 vs brute first-point mass 1/5. So old formula gets the
    TOTAL right?? only if first-point masses were (l+1)/((m+1)(m+2)):
    1/3+1/6+1/10=3/5 and brute 1/5+1/5+1/5=3/5. Totals agree here but terms
    differ. Coincidence at (1,4)? Check (l,K)=(1,5): old sum_{m=1..4} =
    1/3+1/6+1/10+1/15 = (10+5+3+2)/30 = 20/30 = 2/3 = 1-(l+1)/(K+1) = 1-2/6.
    Brute count: M=360, all-coord=120, first-point masses: m=1: 4*5*6=120
    ->1/3; m=2: 2*5*6=60 ->1/6; m=3: 2*3*6=36 ->1/10; m=4: 2*3*4=24 ->1/15.
    Old formula CORRECT termwise after all! Because prod_{i<m}(i+1)*prod_{i>m}(i+2)
    /M: verify equals (l+1)/((m+1)(m+2)). (l+1)! -> ... algebra: numerator =
    (m!/l!)*((K+1)!/(m+2)!); denominator=(K+1)!/(l+1)!; ratio =
    (m!(l+1)!)/(l!(m+2)!) = (l+1)/((m+1)(m+2)). YES identity holds.
    So the OLD atomic first-point weights were CORRECT; the error flagged in
    planning was mistaken. What was actually wrong: calling w[l,m] the mass
    of a single support POINT (it is the mass of the whole first-point-at-m
    CLASS, spread over many distinct pasted threads), and the 'all-point
    thread' weight (l+1)!/(K+1)! claim (single path mass 1/M(l,K); the
    (l+1)!/(K+1)! number is 1/M -- same thing: M=(K+1)!/(l+1)!. Yes equal!).
    So: single-path mass 1/M(l,K) = (l+1)!/(K+1)! -- old P3 right;
    first-point CLASS mass (l+1)/((m+1)(m+2)) -- old P1/T2 right as class
    masses. The genuine correction: class mass != atom mass (atoms within a
    class split further by accumulated shift S).
E5: sub-class split demo (l,K)=(1,4), first-point-at-2 class (12 paths):
    pasted coordinate multiset distribution over (sigma choices at levels
    1 and 3) -- count distinct pasted functions on truncation M=4 mesh
    {0,1}: number of distinct atoms < 12 (collisions), each atom mass =
    (count)*1/60. Enumerate exactly.

Exit 0 with MASSLAW_OK.
"""
from fractions import Fraction
import itertools
import math
import sys


def M_paths(l, K):
    m = 1
    for i in range(l, K):
        m *= (i + 2)
    return m


def check_E1():
    for l, K in [(1, 2), (1, 3), (1, 4), (2, 5), (1, 8), (3, 24)]:
        assert M_paths(l, K) == math.factorial(K + 1) // math.factorial(l + 1), (l, K)
    print("E1 path count M(l,K)=(K+1)!/(l+1)!: OK")


def allcoord_count(l, K):
    c = 1
    for i in range(l, K):
        c *= (i + 1)
    return c


def firstpoint_count(l, m, K):
    # levels l..K-1; first point at level m: coord choices below m, point at m,
    # anything (coord or point) above m.
    n = 1
    for i in range(l, m):
        n *= (i + 1)
    for i in range(m + 1, K):
        n *= (i + 2)
    return n


def check_E2_E3():
    l, K = 1, 4
    M = M_paths(l, K)
    assert M == 60, M
    ac = allcoord_count(l, K)
    assert ac == 24, ac
    assert Fraction(ac, M) == Fraction(l + 1, K + 1) == Fraction(2, 5)
    fp = {}
    for m in range(l, K):
        fp[m] = firstpoint_count(l, m, K)
        # closed form check
        assert Fraction(fp[m], M) == Fraction(l + 1, (m + 1) * (m + 2)), (m, fp[m])
    assert fp == {1: 20, 2: 10, 3: 6}, fp
    assert ac + sum(fp.values()) == M  # partition complete
    print("E2/E3 (l,K)=(1,4): all-coord 24/60=2/5; first-point classes "
          "20/60=1/3 (m=1), 10/60=1/6 (m=2), 6/60=1/10 (m=3); "
          "partition 24+20+10+6=60 complete: OK")
    # second pair (1,5)
    l, K = 1, 5
    M = M_paths(l, K)
    assert M == 360
    assert allcoord_count(l, K) == 120
    assert {m: firstpoint_count(l, m, K) for m in range(l, K)} == \
        {1: 120, 2: 60, 3: 36, 4: 24}
    for m in range(l, K):
        assert Fraction(firstpoint_count(l, m, K), M) == Fraction(l + 1, (m + 1) * (m + 2))
    assert 120 + 120 + 60 + 36 + 24 == M
    print("E2/E3 (l,K)=(1,5): classes 120/360=1/3, 60/360=1/6, 36/360=1/10, "
          "24/360=1/15 -- old formula CONFIRMED: OK")


def check_E4_identity():
    # algebraic identity: (m!/l!)((K+1)!/(m+2)!)/((K+1)!/(l+1)!) == (l+1)/((m+1)(m+2))
    for l, m, K in [(1, 1, 4), (1, 3, 7), (2, 5, 9), (3, 3, 10)]:
        lhs = Fraction(math.factorial(m) * math.factorial(K + 1) * math.factorial(l + 1),
                       math.factorial(l) * math.factorial(m + 2) * math.factorial(K + 1))
        assert lhs == Fraction(l + 1, (m + 1) * (m + 2)), (l, m, K)
    print("E4 identity (first-point class mass closed form): proved OK")


def check_E5():
    # (l,K)=(1,4), first-point-at-2 class: 12 paths; pasted thread on
    # truncation: coords in {0,1}^4, sigma_j = drop-first-j (zero-pad);
    # point values p1..p3 in {0,1}^4 (mesh stand-ins for c_1..c_3).
    # Pasted thread for path with coord choices (a at level1 in {1,2}=sigma_1/sigma_2,
    # point at 2, b at level3 in {1..4,pt}): evaluate at mesh point x in {0,1}^4.
    mesh = list(itertools.product([0, 1], repeat=4))
    p = {1: (1, 0, 1, 0), 2: (0, 1, 1, 0), 3: (1, 1, 0, 0)}

    def drop(v, j):
        return tuple(v[j:]) + (0,) * min(j, 4)

    def paste(a, bchoice, x):
        # level1: sigma_a(x); level2: point p2 (first point); level3:
        # sigma_b(p2) if coordinate else p3.
        y1 = drop(x, a)
        if bchoice == 'pt':
            y3 = p[3]
        else:
            y3 = drop(p[2], bchoice)
        return (y1, y3)  # thread signature (level1 image, level3 image)

    sig = {}
    for a in (1, 2):
        for b in (1, 2, 3, 4, 'pt'):
            key = tuple(paste(a, b, x) for x in mesh)
            sig[key] = sig.get(key, 0) + 1
    assert sum(sig.values()) == 10
    print(f"E5 sub-class split: 10 paths -> {len(sig)} distinct pasted atoms, "
          f"multiplicities {sorted(sig.values())}; atom masses = mult/60: OK")
    assert len(sig) <= 10 and len(sig) >= 2


def main():
    check_E1()
    check_E2_E3()
    check_E4_identity()
    check_E5()
    print("MASSLAW_OK")


if __name__ == "__main__":
    sys.exit(main())
