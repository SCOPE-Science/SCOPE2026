# Independent Audit — 2026/09/18/fgm-obstruction-copula-block-substitution--762cc039a08b

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c0e2b968534c70d2e7a05eedeb37cc759b55ff29`
- Disposition: **FAILED**

## Correctness

**PASS** — The mathematics is substantially correct. The exact density 1+theta(1-2z)(1-2^m prod x_i) yields the same sharp |theta|<=1/(2^m-1) threshold. The Stirling-number chain-rule formula is equivalent to (1+u d/du)^{m-1}c. The convex-order argument correctly makes entropy strictly smaller than the outer FGM entropy throughout the nonzero strict admissible region. The additional criticism of the source L log L example is also valid: normalizing A(xy)^{-a} forces A=(1-a)^2, whose one-dimensional marginal is (1-a)x^{-a}, not 1 unless a=0.

## Originality

**FAIL** — This record was publicly committed at 2026-09-18 18:07:44 UTC, but the assigned record fgm-block-substitution-threshold-entropy-defect--8e6f21783699 had already been publicly committed at 04:03:46 UTC the same day. That earlier record already contains the identical sharp FGM threshold, an equivalent Euler-operator criterion, and a stronger quantitative entropy-defect theorem. The later record therefore duplicates its principal claimed contribution. The L log L source-error diagnosis is an additional observation, but it does not make the headline theorem independently original.

## Scientific value

**FAIL** — As a standalone correction note the extra L log L diagnosis is useful, but nearly all of the substantive theorem package is already covered by the earlier same-repository record, which even supplies a quantitative entropy gap. The later package therefore adds too little independent scientific content to justify a second validated research finding.

## Sources

- Earlier SCOPE record: Exact FGM thresholds and entropy defects for blockwise copula substitution (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/commit/586d65e6e543fae2567bfa5aeab0fd2a08536f9b — Earlier public commit at 2026-09-18 04:03:46 UTC containing the same threshold/operator theorem and quantitative entropy defect.
- Later SCOPE record: Exact FGM obstruction to copula block substitution (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/commit/a86ae68ae71e7da3175d99e558ba29808efbeec3 — Current audited record first committed at 2026-09-18 18:07:44 UTC.
- Copula Operad and Copula Entropy (X. Lu): https://arxiv.org/abs/2609.20512 — Source paper whose unrestricted substitution and entropy claims are being corrected.

## Limitations

- Failure is based on duplication/originality and scientific value, not on a mathematical error.
- The additional L log L criticism may be worth preserving as a correction note, but it is not enough to support the full later record as a distinct validated finding.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository write was performed. Open-access/preprint sources were checked first; Oxford Download was not needed for this record.
