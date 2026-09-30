# Independent Audit — 2026/09/18/outer-parallel-deficit-planar-fractional-isoperimetry--54a568d5ea97

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c80b2ec0cf769873edb44ae991486d3e5ac5d693`
- Disposition: **FAILED**

## Correctness

**PASS** — The displayed deficit identity is mathematically correct under the stated smooth strictly convex hypotheses. With H(r)=C_q(K+rB)-C_q(B_{R+r}), the cited first-variation formula gives H'(r)=2q[W_{1-q}(K_r)-W_{1-q}(B_{R+r})], the cited fixed-perimeter inequality makes this nonnegative, and the cited large-radius asymptotic gives H(r)→0. Integrating from 0 to infinity yields the formula with the stated sign. The P_s reformulation has coefficient 2/s after using P_s=[s(1-s)]^{-1}C_{1-s}. Döhrer-Dohmen's disk uniqueness for convex planar fractional-Willmore energy supplies the strict equality step, and the support-function identity h_{K+rB}=h_K+r transfers disk rigidity back to K.

## Originality

**FAIL** — The claimed new identity is the fundamental-theorem-of-calculus restatement of the exact ingredients already used in Lin-Yang-Yang-Yuan-Zhang's proof: their outer-parallel variational formula, fixed-perimeter Willmore inequality, and decay at infinity. The equality consequence then follows immediately by inserting Döhrer-Dohmen's already-published unique disk minimization theorem. The record does not introduce a new estimate, compactness argument, rigidity mechanism, or extension of hypotheses; it packages two recent published results into an unstated corollary. That is useful exposition, but under an independent research audit it does not meet the originality threshold.

## Scientific value

**FAIL** — Writing the monotonicity proof as an exact accumulated deficit can be conceptually convenient and may suggest later stability estimates, but the record itself proves no quantitative remainder, new equality regime, nonsmooth extension, or new curvature inequality. Its substantive conclusions follow in a few lines from the cited first-variation/asymptotic argument plus an existing uniqueness theorem. The incremental scientific content is therefore insufficient for validation as an independent research finding.

## Sources

- A Sharp Planar Fractional Isoperimetric Inequality (Xiaosheng Lin; Dachun Yang; Sibei Yang; Wen Yuan; Yangyang Zhang): https://arxiv.org/abs/2609.19052 — Provides the sharp inequality and the outer-parallel variational, fractional-Willmore and asymptotic ingredients from which the displayed identity is obtained by integration.
- A Fenchel Theorem for the Gauss maps and uniqueness of minimizers of nonlocal curvature energies (Elias Döhrer; Alexander Dohmen): https://arxiv.org/abs/2604.02042 — Proves that disks uniquely minimize all fractional Willmore energies among convex planar sets, supplying the equality rigidity used by the record.

## Limitations

- The failure is for originality and independent scientific value, not mathematical correctness.
- The identity is restricted to the smooth strictly convex setting in which the cited first-variation argument applies directly.
- No statement is made here about whether the identity is useful as an expository lemma or as a starting point for future stability estimates.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this record.
