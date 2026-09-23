# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `655ea3e489804aa486bf420fad01f4bc29f0f67b`, matching the assignment guard. RESULT.md blob: `2b02677cdd1fdf691019011f071ab1939e1c0f10`.

## Claim reviewed
Covering-radius census fragment for binary linear codes. This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS FOR STORED WITNESSES; NOVELTY FRAMING INCORRECT. The prior independent audit rechecked all 35 parity-check matrices for rank and zero columns, replayed exact syndrome BFS/coset-weight distributions and sphere lower bounds, and found no computational mismatch. Thus the stored matrices certify the stated radii/upper bounds. However, a sphere-bound match does not make a value new.

## Originality
FAIL. Existing covering-radius literature already contains relevant exact determinations in this length/dimension regime, including dimension-6 classifications, and the classical punctured Golay [22,12] code has covering radius 3. That directly undercuts the record's framing of seven new exact determinations and shows that comparing only to a sparse live table is insufficient priority checking.

## Scientific value
FAIL. After removing already-known exact values and classical constructions, the remaining contribution is a small witness table of upper bounds with no new lower-bound method, construction family, asymptotic improvement, or classification. The parity-check matrices are reproducible data but do not by themselves constitute a strong scientific advance.

## Literature checked
- T. Baicheva and V. Vavrek, On the least covering radius of binary linear codes with small lengths: https://doi.org/10.1109/TIT.2002.808099
- T. Baicheva and I. Bouyukliev, On the least covering radius of binary linear codes of dimension 6: https://doi.org/10.3934/amc.2010.4.399

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
A bounded repair can remove the unsupported 'new exact determinations' wording and retain the matrices as reproducible witnesses/upper bounds. That repaired dataset still lacks a sufficiently new general method or consequence to pass the value axis.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `655ea3e489804aa486bf420fad01f4bc29f0f67b`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
