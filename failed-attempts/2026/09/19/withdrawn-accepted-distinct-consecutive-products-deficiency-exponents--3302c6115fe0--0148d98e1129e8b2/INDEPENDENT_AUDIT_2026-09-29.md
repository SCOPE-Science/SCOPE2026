# Independent audit — Quantitative deficiency exponents for distinct consecutive products

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/distinct-consecutive-products-deficiency-exponents--3302c6115fe0`  
**Audited tree:** `4cbd02ddb5292d650a9fc098d1cadff8603f686f`

## Disposition

**FAILED.** Correctness passes, but originality and standalone scientific value fail. The package should be relocated to the designated failed-attempt path while preserving its evidence.

## Correctness

**PASS.** The displayed exponents are internally correct. In the reduced split-product parameters, p=2 forces q=1 and hence r=2s, so the X^{1/2} term occurs on only O(L) pairs; the remainder has p>=3. This gives the raw exponent 1/2+5 theta. Substitution into the stated forest exponents gives maximum 1/2+7 theta for theta<=1/20. Runbo Li’s Theorem 1.1 supplies almost-all primes in intervals of length n^{1/24+epsilon} with O(X(log X)^{-B}) exceptions, so theta down to 1/24 yields 17/24 and 19/24 and the long-gap logarithmic term. Exact recomputation gives rho=24/47, the quoted monotonicity coefficients 113/276 and 341/1081, and the long-root exponent 787/1128.

## Originality

**FAIL.** The central mechanism is already present in the earlier 2026-09-18 SCOPE record `sharper-sparsity-prime-gap-distinct-products--019c9cd2e5c7`, which explicitly isolates the same sparse degree-two locus r=2s and proves the general raw count X^{1/2+5 theta+o(1)}. That earlier record also proves the same super-logarithmic full-deficiency conclusion and a stronger short-gap deletion exponent 2927/3698≈0.7915089, whereas the assigned record states 19/24≈0.7916667. A separate same-day record already applies Li’s 1/24 theorem to the global defect. The new 17/24 raw numerical specialization is therefore an incremental substitution into an already published SCOPE formula, not a sufficiently distinct finding for this package.

## Scientific Value

**FAIL.** As a standalone validated record, the package adds little beyond prior SCOPE work and is partly dominated by it: its 19/24 short-length exponent is weaker than the already published 2927/3698 bound, and its full deficiency statement is already known. The raw 17/24 corollary is correct but does not compensate for the duplicated mechanism and weaker headline downstream bound.

## Independent checks

- Recomputed the exact limiting quantities rho=24/47, raw=17/24, short=19/24, long-root=787/1128, and both positive monotonicity coefficients.
- Verified algebraically that p=r/gcd(r,s)=2 iff r=2s for positive s<r.
- Inspected Runbo Li’s Theorem 1.1 in the public PDF; it states the 1/24+epsilon interval exponent with O(X(log X)^(-B)) exceptional integers.
- Compared against the earlier SCOPE record `sharper-sparsity-prime-gap-distinct-products--019c9cd2e5c7`: its 2927/3698 short-mass exponent is numerically smaller than 19/24 and it already contains the sparse-locus raw formula and super-logarithmic defect conclusion.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.17543 — Chojecki (2026), underlying distinct-consecutive-products prime-gap construction.
- https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf — Runbo Li, Theorem 1.1: 1/24+epsilon almost-all short intervals and logarithmic exceptional set.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/sharper-sparsity-prime-gap-distinct-products--019c9cd2e5c7 — Decisive earlier SCOPE record: same r=2s sparse degree-two mechanism, raw formula 1/2+5 theta, stronger short-mass exponent 2927/3698, and super-logarithmic full deficiency.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/19/quantitative-distinct-consecutive-products-defect--809d39ad5c1a — Same-day earlier-context SCOPE record already uses Li’s 1/24 input for quantitative global deficiency.

## Limitations

- Failure is on originality and standalone scientific value, not mathematical correctness.
- The raw 17/24 numerical corollary is a correct incremental strengthening under the newer 1/24 input, but the package’s principal mechanism was already recorded and its 19/24 short-mass bound is weaker than prior SCOPE work.
- No claim is made that the prior 2927/3698 exponent is optimal.

## Repository identity

The assigned source-tree SHA `4cbd02ddb5292d650a9fc098d1cadff8603f686f` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
