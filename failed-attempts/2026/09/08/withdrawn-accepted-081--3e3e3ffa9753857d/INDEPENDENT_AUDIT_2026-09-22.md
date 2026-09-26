# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/081`  
**Audit performed:** 2026-09-26 UTC  
**Audited source tree:** `3e3e3ffa9753857d0322e68a8e8ba77d5237e974`

## Claim audited

The record reports exact star-discrepancy values for the Fibonacci lattices (F_5) through (F_{12}), extremal anchored boxes, and an exact dual-lattice witness table including counts of all nonzero dual vectors in (\|h\|_\infty\le 12) and the corresponding weighted sums (Q_H).

## Correctness — FAIL

The main star-discrepancy table independently reproduces exactly. A fresh all-grid-corners/all-four-boundary-types enumeration gives:

- (N=5): (9/25)
- (N=8): (15/64)
- (N=13): (28/169)
- (N=21): (16/147)
- (N=34): (41/578)
- (N=55): (136/3025)
- (N=89): (246/7921)
- (N=144): (13/648)

with the committed extremal boxes. The stated shortest dual vectors also reproduce.

However, the claimed **H=12 dual-hit table is false for N=5 and N=8**. By the record's own definition, the count must range over every nonzero (h=(h_1,h_2)) with (max(|h_1|,|h_2|)\le12) satisfying (h_1+g h_2\equiv0\pmod N). Direct exact enumeration gives:

- (N=5,g=3): **124** hits and (Q_{12}=3837623/415800\approx9.2294925445), not 24 and 5.126667.
- (N=8,g=5): **78** hits and (Q_{12}=4418807/831600\approx5.3136207311), not 36 and 4.139484.

The committed verifier explains the discrepancy. Its `spectral_witness(N,g,H)` loops over `range(-N,N+1)` and only afterwards tests whether (\|h\|_\infty\le H). Thus, when (N<H), it searches ([-N,N]^2) rather than the promised ([-H,H]^2). For (N\ge13), the H=12 table agrees with the independent enumeration.

Because the record presents the dual-witness table as an exact proved component of the result, the current package does not pass correctness even though the headline star-discrepancy fractions themselves are correct.

## Originality — PASS, for the star-discrepancy table

Prior Fibonacci-discrepancy literature establishes optimal-order (L_\infty) discrepancy and exact formulas for other discrepancy norms (notably symmetrized (L_2)); I did not identify a prior source giving this same eight-row finite exact (L_\infty) star-discrepancy table with extremal boxes.

Relevant source: Bilyk–Temlyakov–Yu, *Fibonacci sets and symmetrization in discrepancy theory*, https://doi.org/10.1016/j.jco.2011.07.001

The originality assessment does not rescue the correctness failure.

## Scientific value — PASS

The exact star-discrepancy fractions and extremal boxes are useful benchmark data for discrepancy/QMC implementations, and the dual-lattice diagnostics are natural companion invariants. The package would remain scientifically useful after correction of the two truncated H=12 rows.

## Repair assessment

A bounded repair appears possible: change the dual-vector search to enumerate ([-H,H]^2), correct the N=5 and N=8 hit/Q rows, regenerate the artifacts, and independently re-audit the corrected package. Under the campaign rules, however, the currently accepted record cannot be retained as passing while its asserted exact table contains known false entries.

## Final disposition

**FAILED.** Originality and scientific value pass, but correctness fails because two exact dual-hit/Q_H rows are wrong.
