# Fixed-class floor-diagram comparison against the complex Abramovich–Bertram coefficient: equality at r=0, defect −2 for r≥1

## Context

The Hirzebruch surfaces F0=P1×P1 and F2 are deformation equivalent, and the complex Abramovich–Bertram relation links their genus-zero curve counts. At the class used here the complex identity is 12=10+2·1.

Real analogues and surgery formulas for Welschinger invariants are already present in the literature, including Brugallé–Puignau's real Abramovich–Bertram/surgery formula and Brugallé's later invariance framework. Bousseau also proves a q-refined F0/F2 Abramovich–Bertram relation and notes the prior real Welschinger relation. Accordingly, this record does not claim a new failure of real Abramovich–Bertram theory.

The narrower calculation is this: take the three archived Brugallé–Mikhalkin r-real floor-diagram count rows below and combine them with the unchanged `+2` coefficient from the complex identity. The resulting direct numerical comparison agrees at r=0 and not at r≥1. This must not be conflated with a contradiction of the established real surgery formulas.

## Definitions

F0 bidegree (2,2) is class 2E+2F on Σ0. The F2 main class is 2E+4F=2C with C=E+2F, and the correction class is E+4F=2C-E. The archived genus-zero floor-diagram enumeration uses seven point conditions and Brugallé–Mikhalkin r-real marking multiplicities for r=0,1,2,3.

## Result

The archived rows are

W_F0(r)=(8,6,4,2),
W_F2(r)=(6,6,4,2),
W_corr(r)=(1,1,1,1).

Define only for this numerical comparison
RHS_naive(r)=W_F2(r)+2W_corr(r).
Then

RHS_naive(r)=(8,8,6,4),
D_naive(r)=W_F0(r)-RHS_naive(r)=(0,-2,-2,-2).

Thus the naive fixed-coefficient transplant of the complex identity agrees at r=0 and has defect -2 for r=1,2,3. This is an explicit ledger statement, not a counterexample to known real Abramovich–Bertram or Welschinger surgery theorems.

Per-diagram rows (automorphism order, marking representatives, complex multiplicity, complex total, W(r=0..3)) are:

- F0-A, w=1: 2, 4, 1, 4, (4,4,4,2);
- F0-B, w=1: 2, 4, 1, 4, (4,2,0,0);
- F0-C, w=2: 4, 1, 4, 4, (0,0,0,0);
- F2-D, w=1: 6, 6, 1, 6, (6,6,4,2);
- F2-E, w=2: 24, 1, 4, 4, (0,0,0,0);
- F2 correction: 48, 1, 1, 1, (1,1,1,1).

## Proof / evidence

The archived `artifacts/ledger.json` gives exactly the six rows above. Their complex totals are 12, 10 and 1. Summing the real rows gives the three W vectors above.

The recorded divergence equations also make the small shape census complete. For F0, bounded-edge weights w=1 yield two shapes and w=2 yields one; w≥3 is impossible. For the F2 main class, w=1 and w=2 yield one shape each; larger w is impossible. The correction class has one floor.

The weight-2 diagrams contribute to the complex totals but are killed by the real even-edge rule in this marking convention.

## Originality and interpretation

The general real Abramovich–Bertram/surgery mechanism is prior work. No priority is claimed for that mechanism. The retained scientific content is the explicit fixed-class r-indexed ledger and the warning that the unchanged complex coefficient `+2` applied termwise to these three archived rows is not, by itself, the full real surgery formula for r>0.

## Limitations

This is one fixed genus-zero class comparison and one floor-diagram convention. It does not determine or refute the general real surgery formula. The defect vector refers only to the explicitly defined `RHS_naive`.

## Reproducibility

`artifacts/ledger.json` contains the six rows. `artifacts/enumerate.py` and `artifacts/verify.py` encode the corresponding census and checks.

## References

- E. Brugallé, G. Mikhalkin, Floor decompositions of tropical curves: the planar case, arXiv:0812.3354.
- E. Brugallé, N. Puignau, Behavior of Welschinger invariants under Morse simplifications, arXiv:1203.2773.
- E. Brugallé, On the invariance of Welschinger invariants, arXiv:1811.06891.
- P. Bousseau, Refined floor diagrams from higher genera and lambda classes, arXiv:1904.10311.
