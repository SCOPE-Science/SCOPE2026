# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-015  
**Original source path:** `2026/09/07/015`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `38890eae9a415b6d9e178f0924f1bda13645a740`  
**census_table.csv blob:** `83ca1119a06337563e28ceca8d194bd7e05b67b5`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

The record supplies class numbers, class-group structures, continued-fraction periods, maximal-order fundamental units and regulators for all 91 squarefree `d` in `[201,350]`, together with nonprincipality witnesses and a correction concerning `d=277`.

## Correctness — PASS

No correctness defect is used as the rejection basis. I independently checked representative rows using the real-quadratic analytic class-number formula together with the published regulators and discriminants: `d=201` gives `h=1`, `d=202` (`D=808`) gives `h=2`, `d=226` (`D=904`) gives `h=8`, and `d=277` gives `h=1`. The published `d=277` unit `(2613+157 sqrt(277))/2` has norm `-1`, consistent with the stated maximal-order regulator correction. These spot checks exercise both `D=d` and `D=4d` cases and the largest class number in the table. The record's exact-integer verification artifacts and witness data are internally consistent with these independent checks.

## Originality — FAIL

The underlying data are not a new mathematical result. Exact class numbers, fundamental units/regulators and class groups of real quadratic fields in this tiny discriminant range are standard computational number-theory data. Henri Cohen's *A Course in Computational Algebraic Number Theory* includes Appendix B.2, explicitly titled “Table of Class Numbers and Units of Real Quadratic Fields,” and modern databases such as the LMFDB provide exact invariants for these individual quadratic fields. The record itself uses LMFDB spot checks, confirming that central values are pre-existing data rather than newly discovered invariants.

Searches used `real quadratic class number regulator tables`, `class numbers units real quadratic fields table`, `quadratic field discriminant 904 class number 8 regulator`, and exact field labels from the record. The interval packaging `[201,350]` and attached reduction chains do not create a new theorem or new parameter regime after the standard tables/databases and classical algorithms are accounted for.

## Scientific value — FAIL

The bundle is reproducible, but the surviving contribution is an arbitrarily bounded re-tabulation of classical invariants with certificates. It introduces no new class-number theorem, improved algorithm, new family, bound, distributional law, or database-scale coverage. For a validated-finding collection, the finite interval and witness packaging are not scientifically substantial enough once prior coverage is subtracted.

## Repair assessment

A bounded wording repair cannot turn this interval census into a new theorem without changing the record's scientific identity. A genuinely new family-level result, algorithmic improvement, or previously unavailable invariant would require a new investigation.

## Final disposition

**FAILED.** Arithmetic checks are consistent, but originality and scientific value fail because the claimed content is already standard tabulated/database material.