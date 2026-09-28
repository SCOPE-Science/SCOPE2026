# Independent audit — SCOPE-20260910-004

## Scope
Independent review of `2026/09/10/004` at tree `6610bc59b47beac8f17755e8590a57b6dd671451`.

## Correctness
**FAIL.** The numerical replay is internally repeatable for the stored arrays, but the scientific headline is stronger than the certificate. The seed matrices are rounded decimals and the genus-2 surface relation is satisfied only up to a floating residual of order `1e-12`; no exact algebraic construction, interval enclosure, or validated correction to a nearby exact representation is supplied. Therefore the package does not certify an exact genus-2 Hitchin representation `rho_(1/4)` to which the stated Labourie cross-ratio theorem applies.

There is also a reproducibility inconsistency. `artifacts/build_matrices.py` advertises the cross-ratio table but uses an attracting-line/attracting-covector flag helper and labels `Q0=(A1+,B2+,B1+,A2+)`. `artifacts/replay_fallback.py` and `RESULT.md` instead use `Q0=(A1+,A1-,A2+,A2-)` with crossed attracting/repelling covectors. These are different observables; the rebuild path therefore does not independently reproduce the reported `674.3355...` datum.

## Originality
**PASS only in the narrow sense that the chosen numerical tuple was not located in the checked literature.** That is not enough to validate the record.

## Scientific value
**FAIL.** Without an exact representation certificate, the number is a floating-point datum on a near-representation. The record also notes that the bare `1.02` threshold is already exceeded at the Fuchsian base, and the computation proves no entropy gap.

## Literature checked
- Potrie–Sambarino, *Eigenvalues and Entropy of a Hitchin representation*, arXiv:1411.5405.
- Bridgeman–Canary–Labourie–Sambarino, *The pressure metric for Anosov representations*, arXiv:1301.7459.
- Beyrer–Guichard–Labourie–Pozzetti–Wienhard, *Positivity, cross-ratios and the Collar Lemma*, arXiv:2409.06294.

## Disposition
**FAILED.** Relocate the package atomically to the dispatcher-assigned failed path. A salvage attempt would need a rigorously certified exact representation (or validated nearby solution), one unambiguous flag convention, and one rebuild/replay path for the same observable.
