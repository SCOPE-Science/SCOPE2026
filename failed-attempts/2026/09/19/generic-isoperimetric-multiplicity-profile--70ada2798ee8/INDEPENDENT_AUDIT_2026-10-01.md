# Independent audit — SCOPE-20260919-70ada2798ee8

Audited: 2026-10-01 UTC.

Disposition: **failed**.

## Final claim

For a generic smooth metric, unique isoperimetric regions occur on a dense \(G_\delta\) set of volume fractions; a natural minimizer-fiber diameter is upper semicontinuous, with uniqueness exactly at its continuity points, and minimizers vary continuously in strict BV at unique fibers, with the half-volume complement symmetry quotiented out.

## Correctness (C) — PASS

Niu’s compactness Proposition A.1 applies when both metric and prescribed volume vary and gives subsequential \(L^1\) convergence to a limiting minimizer together with strict \(BV\) convergence. Applying it to diameter-realizing pairs proves upper semicontinuity of the minimizer-fiber diameter. Niu’s Corollary 1 gives one generic metric set with uniqueness at every rational non-half fraction and exactly a complementary pair at half volume. Nonnegative upper semicontinuity then makes the zero set \(G_\delta\); dense rational zeroes force continuity exactly at zeros and discontinuity at positive values. The same compactness argument yields uniform collapse at unique fibers and modulo complement at half volume.

**Sources checked.** assigned RESULT.md at the audited tree; complete Niu arXiv:2609.20790 full text, including Theorems 1–2, Corollary 1, and Proposition A.1

**Risks / limits.** No size estimate beyond meagreness is proved for the exceptional set, exactly as limited in the claim.

## Originality (O) — FAIL

The full Niu paper already contains every non-elementary ingredient: simultaneous rational-fraction uniqueness for one generic metric, pair-space generic uniqueness, and compactness with strict-BV convergence under varying metrics and volumes. The audited dense-\(G_\delta\) statement is the immediate Baire/topology consequence of those rational zeroes and upper semicontinuity; the continuity-set identity and strict-BV selection are likewise direct compactness consequences. Under the required implication test, these are covered corollaries of the primary source even though Niu does not package them under the same multiplicity-profile terminology.

**Sources checked.** complete full text arXiv:2609.20790; Resultary semantic search for residual-volume uniqueness and multiplicity continuity

**Risks / limits.** None material beyond the stated scope.

## Value (V) — FAIL

The multiplicity profile is a useful organizational device, but after Niu’s corollary and compactness proposition are available, the residual-volume theorem, continuity-set identity, and strict-BV selection follow by standard upper-semicontinuity and subsequence arguments. Under the bar rejecting routine deductions from a newly proved theorem, this does not constitute a separate worthwhile mathematical gap.

**Sources checked.** Niu Corollary 1 and Proposition A.1 plus elementary Baire/upper-semicontinuity facts

**Risks / limits.** None material beyond the stated scope.

## Originality comparison

**Equivalent formulations.** Uniqueness is zero diameter of the compact minimizer fiber; the continuity-set formulation is obtained by combining nonnegative upper semicontinuity with a dense set of zero values.

**Broader coverage.** Niu’s generic rational uniqueness and strict-BV compactness jointly imply the residual-volume and minimizer-selection conclusions. His pair-space generic theorem similarly implies the pair-space zero-set statement once the same upper-semicontinuity argument is applied.

**Exact database or table checks.**

- Resultary: generic isoperimetric regions unique residual volume fractions multiplicity diameter upper semicontinuous strict BV — The audited record was the direct hit; the relevant primary source is Niu’s 2026 generic uniqueness paper.

- primary full text: Niu Corollary 1 and Proposition A.1 — Corollary 1 gives simultaneous rational non-half uniqueness for one generic metric; Proposition A.1 gives strict-BV compactness under varying metric and volume.

**Claim versus prior implication.** Dense rational uniqueness plus upper semicontinuity gives a dense \(G_\delta\) zero set and makes every positive value a discontinuity. Strict-BV compactness plus uniqueness forces every sequence of minimizers to the unique limit. These are direct implications of the source results.

## Source inspections

- Niu full text pages containing Theorems 1–2 and Corollary 1 inspected.

- Niu Appendix A, Proposition A.1 and strict-BV conclusion inspected in full.

- Assigned package files inspected from the frozen Git tree.

## Residual risks

- No additional material risk identified.

## Scope boundary

Scientific rejection is on originality and value, not correctness. The package correctly states a structural corollary of Niu’s very recent theorem, but implication-based originality does not survive.
