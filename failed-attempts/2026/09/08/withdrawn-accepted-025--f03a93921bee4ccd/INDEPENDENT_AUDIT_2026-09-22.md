# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `8598138b0cb0b7f5e51f28875fb38a2473ff9ee4`, matching the assignment guard. RESULT.md blob: `6ef5d2ce10c7cfe845a0516f667ce299db5ebddc`.

## Claim reviewed
v-number versus induced matching on seven-vertex graphs/trees. This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS FOR THE FINITE WITNESSES AND TREE CENSUS. The recovered audit independently verified the v-number/induced-matching witnesses and reproduced the complete 7^5=16807 labeled-tree census. The current source tree is unchanged.

## Originality
FAIL/NARROW. Saha–Sengupta prove v(I(G)) ≤ im(G) for every bipartite graph; every tree is bipartite, so the tree inequality itself is already covered by a stronger general theorem. The remaining strictness distribution is a finite n=7 census, and the non-bipartite H* is one small example rather than a new general regime.

## Scientific value
FAIL. The 7-vertex tree counts and one outside-hypotheses witness are descriptive finite data. They do not extend the known bipartite theorem, characterize equality/strictness, produce an infinite family, or supply a general algebraic/combinatorial consequence. Reproducibility of the census is not enough to overcome that limited scope.

## Literature checked
- K. Saha and I. Sengupta, The v-number of Monomial Ideals: https://arxiv.org/abs/2111.12881
- G. Grisalde, E. Reyes and R. H. Villarreal, Induced matchings and the v-number of graded ideals: https://arxiv.org/abs/2109.14121

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
A bounded repair can remove any suggestion that the tree inequality is new and present the n=7 distribution purely as data. A substantive repair would require an equality/strictness characterization, an infinite family, or a theorem beyond the already-known bipartite inequality.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `8598138b0cb0b7f5e51f28875fb38a2473ff9ee4`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
