# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 28–55. A size-n^2 nonattacking set hits each vertical fibre once. On the underlying subgroup the horizontal projection is thus an additive isomorphism, so an affine placement is a graph of the homomorphism with unique ordered slopes and offset. For a nonvertical queen direction the displacement scalar must annihilate ad_1+bd_2-d_3; a nonzero annihilator always produces a nonzero horizontal displacement since a pivot is ±1. This proves the unit criterion over arbitrary composite moduli. Independently counted the prime-field slopes without relying on the frozen rational incidence enumeration: for T={0,±1} and a outside T, forbidden b are in T, T+a, T-a. For p>=7 they form nine elements except at the four distinct a=±2,±1/2. At a=±2 the unshifted set meets each shifted set in one element and the shifted sets are disjoint; at a=±1/2 only the two shifted sets meet, in two elements. Thus each exceptional row has seven forbidden b and the count is (p-7)(p-9)+4(p-7)=(p-5)(p-7), including zero for p=7. For p=2,3 every a is forbidden; for p=5 the only candidates a,b=±2 force a±b=0. Lifting each surviving slope independently modulo p^e gives p^(2(e-1)) lifts; CRT and n offsets give the stated product, including 264, 624 and 351384. This agrees with the frozen 12-line incidence calculation. Inspected verify_affine_queens.py and the recorded replay without running the uploaded script; those tests do not supply the all-modulus proof or enumerate nonaffine placements.

## originality

FAIL

The proposed local enumeration is exactly the m=1 extended Catalan arrangement of type B2, with the already known affine characteristic polynomial (t-5)(t-7). The generic local count follows from the finite-field method. The same attack-model literature already provides the hyperplane/unit argument and excludes all moduli with a prime divisor below 11. The graph normalization, good reduction at p>=11 and CRT with an independent offset are routine consequences, not a distinct new exact counting input. No separate printed statement of the final composite-modulus formula was verified; the FAIL is for demonstrable implication, not a claim that the same displayed product previously appeared in queens terminology.

## value

FAIL

The affine family is natural, but the only exact count here is the known B2 Catalan complement multiplied and lifted by elementary residue arithmetic. Good reduction and the affine normalization do not leave an independently unknown useful statistic once that equivalence is made. The unrestricted maximum-count problem remains untouched.

The dated certificate retains the supplied scientific assessment, sources and limitations.
