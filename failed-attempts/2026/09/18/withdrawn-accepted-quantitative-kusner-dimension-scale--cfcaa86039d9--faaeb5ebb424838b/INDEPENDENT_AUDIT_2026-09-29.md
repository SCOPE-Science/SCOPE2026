# Independent audit — Quantitative dimension scale for Kusner counterexamples near p=4

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/quantitative-kusner-dimension-scale--cfcaa86039d9`
**Audited tree:** `3f2a029d5a980ab05387880f163c562d7384283d`

## Disposition

**FAILED.** The mathematics is correct, but the record fails originality and standalone scientific value because equivalent SCOPE results were already published earlier.

## Correctness

**PASS.** The Hadamard-order construction and the asymptotic calculation are mathematically sound. An arbitrary normalized Hadamard matrix preserves the four agreement/disagreement counts used in Xiong's construction. Independent algebra reproduces Phi_4(a)=1-3(a^2-2)^2/(4(a^4+2)), its unique nondegenerate maximum at a=sqrt(2), c=sqrt(2)log(1+sqrt(2))-(7/4)log 2=0.0334429143005567..., and 8/c=239.2136022627.... The Lambert-W lower bound is a valid inversion of Swanepoel's stability inequality after log(1+x)>=x/(1+x).

### Independent checks

- Re-derived the p=4 identity for Phi_4 and verified the unique maximum at a=sqrt(2).
- Differentiated Phi_p at (p,a)=(4,sqrt(2)) and reproduced c=0.0334429143005567... and 8/c=239.2136022627....
- Checked the arbitrary-Hadamard distance counts: distinct rows disagree in exactly m/2 positions and H_4 tensor H gives the same distinguished-column cases as the Walsh construction.
- Re-derived the Lambert-W lower bound from Swanepoel's fixed-dimension stability inequality.
- Compared the current theorem with the earlier SCOPE records 43b27c183a43 and 61c76de11ba3 and verified substantive equivalence of the Hadamard refinement and leading asymptotic constant.
- Verified repository chronology: 43b27c183a43 at 2026-09-17T14:31:30Z, 61c76de11ba3 at 2026-09-17T17:00:42Z, current record at 2026-09-18T04:51:55Z.

## Originality

**FAIL.** The core theorem was already present in two earlier SCOPE records from 2026-09-17. Record 43b27c183a43, committed at 14:31:30Z, already proves the arbitrary-Hadamard extension, optimizes max_a Phi_p(a), derives the same constant c and 8/c, and proves the template-optimal 1/(p-4) scale. Record 61c76de11ba3, committed at 17:00:42Z, likewise states the arbitrary-Hadamard refinement and the same near-4 two-sided asymptotics. The assigned record was added later, at 2026-09-18T04:51:55Z. Its explicit Lambert-W presentation is a short rearrangement of the same Swanepoel inequality and is not a distinct research finding.

### Literature and chronology checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/74497afca5c44c2b08e68e3dc3debb522018666a — Earlier SCOPE commit adding Hadamard densification and the exact near-p=4 scaling constant at 2026-09-17T14:31:30Z.
- https://github.com/SCOPE-Science/SCOPE2026/commit/e2ee634da15ddde82e6ac513059818cc6459d7dc — Earlier SCOPE commit adding the arbitrary-Hadamard Kusner refinement at 2026-09-17T17:00:42Z.
- https://github.com/SCOPE-Science/SCOPE2026/commit/a250d6167648ca943fd5fbe873469007900f5a0e — Commit adding the assigned later duplicate at 2026-09-18T04:51:55Z.
- https://arxiv.org/abs/2609.14794 — Nathan Xiong, Kusner's conjecture is false for p>4; source of the all-p>4 equilateral construction.
- https://arxiv.org/abs/1304.7033 — Konrad Swanepoel, Equilateral Sets and a Schütte Theorem for the 4-norm; source of the quantitative stability interval used for the lower bound.

## Scientific value

**FAIL.** Although the exposition is useful and the formulas are correct, this record is a later duplicate of an already published repository result. The Lambert-W lower-bound form is a minor repackaging rather than a materially new theorem or method, so the record does not justify separate validated-finding status.

## Limitations

- The mathematical statements are correct; failure is specifically due to prior repository coverage and resulting lack of standalone scientific value.
- The true first-failure dimension remains between scales 1/(epsilon log(1/epsilon)) and 1/epsilon; no global sharp asymptotic is proved.

## Publication guard

The current source tree on `main` matched the assignment tree `3f2a029d5a980ab05387880f163c562d7384283d` exactly during this audit. The guarded change-set adds the independent-audit evidence, marks the independent-audit channel as failed, adds `FAILED_ATTEMPT.md`, and requests atomic relocation of the complete package to `failed-attempts/2026/09/18/withdrawn-accepted-quantitative-kusner-dimension-scale--cfcaa86039d9--faaeb5ebb424838b`. Lean and expert-attestation channels are preserved unchanged.
