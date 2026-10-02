# Scientific audit — 2026-09-30

## Final claim

The package correctly tabulates Ehrhart polynomials, h-star vectors and linear-extension counts for every unlabeled poset with n<=6 and correctly reports the small-order extrema and reciprocity checks.

## Correctness — PASS

An independent generation of naturally labelled transitive relations followed by isomorphism canonicalization reproduced the unlabeled-poset counts 1,1,2,5,16,63,318. Independent order-preserving-map and linear-extension computations for all 318 six-element types reproduced 121 distinct Ehrhart-value vectors, 62 distinct linear-extension counts, unique maximum 720 at the antichain, runner-up 360, and unique minimum 1 at the chain. The remaining volume and reciprocity identities are standard consequences of the order-polytope theory used by the package.

## Originality — PASS

No exact per-type Ehrhart table matching this package was located. FindStat already supplies the complete small-poset universe and linear-extension statistic, and Stanley's theory identifies order-polytope Ehrhart counts with order-polynomial counts. Thus the explicit table appears not to be a copied database, but it is very close to a routine derived export of established objects and algorithms.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and implication from prior results. See `INDEPENDENT_AUDIT_2026-09-30.json` for the structured searches, source inspections, checked sources, and residual risks.

## Scientific value — FAIL

The claimed contribution is principally a bounded recomputation of standard order-polynomial data over a complete small-poset database already available through n=7. Its highlighted normalized-volume extremum is a textbook consequence of the linear-extension interpretation, and the finite cutoff n<=6 is not tied to a mathematical boundary, obstruction, conjecture, or motivated unknown invariant. Under the stated value bar, correctness and absence of an identical published table do not make this mechanically derived census scientifically worthwhile.

## Disposition

FAILED. This assessment records the mathematical status of the claim. It is not an external attestation or formal-proof certificate.
