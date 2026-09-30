# Independent Audit — 2026/09/11/041

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `335e68bc28f7c32df1a5d9d70fb9d18c85654382`  
**Audited current source tree:** `335e68bc28f7c32df1a5d9d70fb9d18c85654382`  
**Audited main commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

## Correctness

PASS AS A COMPUTATION. I independently recomputed all 70 maximal minors of the displayed 4x8 matrix: exactly 1234 and 5678 vanish. I checked all 420 three-term tropical Plücker relations for h, with the minimum attained at least twice in every case, and recomputed the determinants of A+t(E41+E15): the two exceptional minors are -22t and -18t and every other basis minor has t-adic valuation 0. The exact certificate is internally correct.

## Originality

FAIL AS A NEW STRUCTURAL RESULT. For this rank-4 sparse-paving matroid the height vector h is exactly the corank vector: the 68 bases have corank 0 and the two circuit-hyperplanes have corank 1. Joswig--Schröter (2017) proves that paving matroids are split and, for a connected split matroid, Proposition 30 places its corank vector in the relative interior of a simplicial Dressian cone. The same prior theory relates realizability of corank tropical linear spaces to realizability of the underlying matroid. Thus, once the record supplies a rational realization of M2, the headline Dressian-cone/lift phenomenon is an instance of established general theory. The particular small integer matrix and two-entry first-order perturbation are explicit witnesses, but they do not rescue the claimed research-level structural novelty.

## Scientific value

FAIL AS A VALIDATED NEW RESEARCH FINDING. The matrix, minor table, and sparse perturbation are useful worked certificates, but the central mathematical conclusion is a routine specialization of existing split-matroid/corank-vector theory rather than an unresolved realizability case. The context describing this minimal two-hyperplane case as part of an open lift catalogue therefore overstates its scientific novelty/value.

## Independent checks

- all 70 minors recomputed exactly
- all 420 tropical Pluecker three-term relations checked
- all 70 lifted determinant valuations recomputed; exceptional determinants -22t and -18t
- current main record tree SHA equals the assigned source-tree SHA

## Sources consulted

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/041
- https://doi.org/10.1016/j.jcta.2017.05.001
- https://arxiv.org/abs/1112.1278

## Limitations

- The failure is not a correctness failure: the displayed realization and valuation computation are valid.
- This audit does not claim that every explicit matrix or sparse perturbation has appeared verbatim in prior literature; the rejection is that the advertised structural finding is already covered by general theory.
