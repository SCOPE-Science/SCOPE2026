# Independent Audit — 2026/09/12/022

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `072a94f4a033ffc9613a42377883afa739334906`  
**Disposition:** **FAILED**

## Correctness

The exact incidence count is consistent and reproducible. The cyclotomic verifier enumerates all C(21,3)=1330 triples and finds only the ten antipodal triples through the origin. An independent determinant scan agrees. Consequently ten 3-point diameters consume 30 of the 210 point-pairs and the remaining 180 pairs form ordinary lines, with the claimed 40 inner-inner, 100 inner-outer, and 40 outer-outer split.

## Originality

Targeted searches of ordinary-line and orchard-planting literature found general lower bounds, large-n structure theorems, and standard extremal constructions but no prior tabulation of this pinned two-concentric-decagon-plus-centre D21 configuration or its exact 180-line type census. The pass is narrow: it credits the exact instance ledger, not a new ordinary-line theorem.

## Scientific value

The configuration has 180 ordinary lines at n=21, extremely far from the few-ordinary-line regime driving Dirac-Motzkin and related structure theory. The source proves no family theorem, extremal statement, stability result, or new method; it performs a complete exact enumeration for one elementary symmetric finite set. That is a useful benchmark but not a standalone research contribution at the claimed level.

## Limitations

- Absence of an exact prior table in targeted search is not a proof that no one has ever computed this configuration.
- The scientific-value failure concerns publication significance, not the arithmetic correctness of the 180-line ledger.
- The audit did not generalize the count to varying radius ratio or angular offset.

## Evidence

- [Green–Tao, On sets defining few ordinary lines](https://arxiv.org/abs/1208.4714): Establishes the n/2 ordinary-line theorem for sufficiently large n and structural results for sets with few ordinary lines; it does not tabulate this fixed D21 configuration.
- [MathWorld, Ordinary Line](https://mathworld.wolfram.com/OrdinaryLine.html): Summarizes the ordinary-line problem and standard bounds; no exact D21 two-circle ledger is recorded.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `072a94f4a033ffc9613a42377883afa739334906`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
