# Exact one-sided Nash-support census of the non-degenerate 3x3 {0,1,2,3} bimatrix cube with a 7-equilibrium fully-mixed and maximal-welfare witness

## Context

Nash equilibrium structure (existence, support bounds, generic oddness,
Lemke-Howson computation, PPAD-motivated selection) is a recognized frontier.
Exact small-game ground truth is demanded to calibrate
equilibrium-selection/enumeration benchmarks and to test generic oddness before
large-game asymptotics. The 3x3 cube with payoffs in {0,1,2,3} is the minimal
natural scope admitting fully-mixed 3x3 supports with the smallest alphabet
giving nontrivial indifference while staying finite and auditable.

## Definitions

A bimatrix game is (A,B) with A,B in {0,1,2,3}^{3x3} (A row payoffs, B column
payoffs). A Nash equilibrium with supports I (rows, positive probability) and
J (columns) satisfies: some y fully supported on J makes all rows of I
indifferent under A and all rows outside I strictly worse; some x fully
supported on I makes all columns of J indifferent under B and all columns
outside J strictly worse. Non-degeneracy: every mixed strategy with support of
size k has at most k pure best responses (in particular each pure strategy has
a unique best response and no support-2 mix has a third tied best response).
One-sided admissibility at (I,J) means the A-side (respectively B-side) system
above is solvable, without yet requiring the other side.

## Result

One-sided factorization lemma (proved): for fixed (I,J) with |I|=|J|=k, the
row-side system depends only on A and the column-side only on B. Hence the
number of jointly one-sided-admissible pairs (A,B) at (I,J) is the product
N_A(I,J)*N_B(I,J), and by cube symmetry these depend only on k.

Exact one-sided census (exact exhaustive integer arithmetic over 4^9=262144
matrices per side): per fixed support, 1x1: N_A=57344 (joint pairs
57344^2=3288334336); 2x2: N_A=31104 (joint pairs 31104^2=967458816, strict core
486 patterns over the 6 relevant entries); 3x3: N_A=34032 (joint pairs
34032^2=1158177024; 17016 with D>0/all-positive Cramer numerators, 17016
mirrored D<0/all-negative).

Exhibited non-degenerate game A=[[0,1,3],[0,3,0],[2,2,1]],
B=[[0,1,3],[2,3,1],[2,1,0]] has exactly 7 Nash equilibria (odd): three pure
((0,2),(1,1),(2,0)), three 2x2 ((0,1)x(1,2) with x=(1/2,1/2),y=(3/5,2/5);
(0,2)x(0,2) with x=(2/5,3/5),y=(1/2,1/2); (1,2)x(0,1) with x=(1/2,1/2),
y=(1/3,2/3)), and one fully mixed with x=(3/8,1/8,1/2), y=(1/11,6/11,4/11)
(row payoffs 18/11 x3; column payoffs 5/4 x3; all deviation checks strict).
Maximum equilibrium welfare is 6 (two co-maximal pure equilibria), next
distinct value 4, welfare gap 2.

## Proof / evidence

Lemma by inspection of the indifference/strictness systems (only A entries on
the row side, only B on the column side). Counts by exact exhaustive
enumeration: 1x1 analytic (sum_a a^2=14 strict-maximum column triples at fixed
position, times 4^6 free entries); 2x2 exact scan over 4^6 tuples with interior
condition (p,q nonzero opposite signs, outside row strictly worse at induced
mix); 3x3 Cramer-sign scan over all 4^9 matrices. Game certificate by
exact-rational support enumeration over all 19 support pairs, re-deriving each
equilibrium's equalities and strict inequalities. Reproduction: `python3
artifacts/verify.py` (stdlib only, Fraction/integer arithmetic) ends with
`ALL CHECKS PASS`.

## Limitations

Complete joint per-pattern realized-equilibrium-count table with multiplicity
distribution over all 4^18 pairs is not claimed; Section 3 counts are exact
one-sided (marginal) admissibility counts and products. Mixing-probability
denominator observation ({2,3,4,5}) is reported computed evidence, not a proved
classification. Non-degeneracy certified for the exhibited game only via the
operational edge-tie check.

## Reproducibility

Payoff entries above; `output/artifacts/verify.py` replays non-degeneracy, all
7 equilibria, welfare table/gap, and all three one-sided recounts from entries
only, in seconds with stdlib-only Python.

## References

- Nash, Equilibrium points in n-person games (1950).
- Lemke-Howson / Mangasarian, Equilibrium points of bimatrix games (1964).
- von Stengel et al., Enumeration of Nash equilibria for two-player games.
- Quint-Shubik / Wilson, odd number of equilibria in non-degenerate games.
- Papadimitriou (PPAD) / Gambit equilibrium software (general tools, not this cube census).
