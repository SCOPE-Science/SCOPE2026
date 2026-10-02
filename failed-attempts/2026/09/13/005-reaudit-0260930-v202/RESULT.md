# Genus-1 triple branching-gap decision at degree 6: exact connected Hurwitz number H = 2061

## Context

This record resolves the admitted target: decide, with proof, whether the Riemann-Hurwitz-satisfiable genus-1 degree-6 triple passport with ordered profiles alpha=(4,1,1), beta=(3,2,1), gamma=(2,2,2) plus three simple transpositions is realizable by a connected branched cover of P1 (positive connected Hurwitz number) or is a branching gap (connected Hurwitz number zero). The passport was selected to lie outside Chen's one-part reduction, outside the Bai-Chen (2,d-2) formulas, and outside the Pakovich / Baroni-Petronio length-2 existence classification, since none of the three profiles has length 1 or 2 and the two-part profile (2,4) does not occur.

## Definitions

Fix degree d=6, genus g=1, and an ordered branch locus B of 6 distinct fixed points in P1(C) carrying, in order, profiles (4,1,1), (3,2,1), (2,2,2), and three simple profiles (2,1,1,1,1). The ramification deficits (sum of part-minus-one) are 3+3+3+1+1+1=12=2d+2g-2, so Riemann-Hurwitz is satisfied. Connected covers with B fixed pointwise correspond bijectively to simultaneous-conjugation orbits of transitive tuples (a,b,c,t1,t2,t3) in S6 of cycle types (4,1,1), (3,2,1), (2,2,2), (2,1,1,1,1)^3 with ordered product t3*t2*t1*c*b*a=1 (a applied first). The connected Hurwitz number H is the sum of 1/|Aut(f)| over connected covers fixing B pointwise, equivalently the number of transitive tuples divided by 6!=720 when all transitive tuples have trivial simultaneous centralizer.

## Result (Theorem)

The connected Hurwitz number for this ordered passport is H=2061, a positive integer. Hence the passport is realizable by a connected genus-1 degree-6 branched cover of P1; there is no branching gap. The value is certified by two independent complete enumerations that agree exactly.

## Proof / Evidence

Conjugacy class sizes in S6: |(4,1,1)|=90, |(3,2,1)|=120, |(2,2,2)|=15, |transpositions|=15. Fix representative a0=(0 1 2 3) of type (4,1,1); its centralizer has order 8 (formula 4*2! confirmed by direct enumeration of all 720 permutations). By orbit-stabilizer, every S6-orbit of tuples with first entry of type (4,1,1) meets the slice {a=a0} in exactly 8 points, provided counted transitive tuples have trivial full stabilizer. Method A (solved-t3 over 225 (t1,t2) pairs with union-find transitivity) and Method B (literal 1800x3375=6,075,000 six-fold product tests with BFS transitivity and disconnected orbit tally) both fix a=a0, scan the 1800 pairs (b,c), and agree: 16956 relation-satisfying tuples, of which 16488 are transitive and 468 are disconnected, all of orbit type (2,4); 16488+468=16956. Since t3*P=1 with t3 a transposition forces P itself to be that transposition, Method A is bijective. Every one of the 16488 transitive tuples has trivial simultaneous centralizer in S6 (each full stabilizer lies in C(a0), so checking the 7 non-identity centralizer elements is exhaustive; 0 non-trivial stabilizers), so each contributes exactly 1/720 and H=16488/8=2061 exactly. An explicit witness tuple (a0, b=[0,2,1,4,5,3], c=[1,0,3,2,5,4], t1=[0,1,5,3,4,2], t2=[0,3,2,1,4,5], t3=[1,0,2,3,4,5]) has the correct cycle types, transitive action, and exact product identity. The audit independently re-executed the full 6,075,000-test census and all stabilizer checks, reproducing 16956/16488/468 and H=2061.

## Limitations

The certified value H=2061 is for the ordered, pointwise-fixed branch locus with the stated ordered profile assignment; it does not give the unordered-locus count and does not geometrically classify the 2061 covers. The proof is computational exhaustive enumeration in S6, not a closed-form formula, and depends on correct execution of the accompanying scripts.

## Reproducibility

Run python3 censusA.py (about 1 s), python3 censusB.py (about 2 s), and the stabilizer verification (about 60-120 s over all 16488 tuples) using only the Python standard library; outputs land in output/artifacts/ as censusA.json, censusB.json, verification.json, recording N_total=16956, N_transitive=16488, N_disconnected=468, |C(a0)|=8, and H=2061. Class sizes, centralizer order, sample-tuple types, product identity, transitivity, and the identity 16488+468=16956 can each be rechecked directly.

## References

Riemann-Hurwitz formula; S6 monodromy / simultaneous-conjugation orbit model of Hurwitz numbers; orbit-stabilizer normalization; Chen one-part reduction, Bai-Chen (2,d-2) formulas, Pakovich / Baroni-Petronio length-2 classification (excluded cases); Vakil genus-0-and-1 Hurwitz recursions and ELSV-type / quasimodularity background (no prior table value for this passport).
