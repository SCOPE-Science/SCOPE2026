# Independent scientific audit — SCOPE-20260920-96e1ba61d903

Audited at: 2026-10-01T19:12:08.377982Z

Disposition: **failed**

## Correctness — PASS

The translated-ball and polar expansions through fourth order are algebraically consistent, the critical quadratic terms cancel, and the radial integral identity gives \(D_n>0\), so the critical quartic coefficient is negative. The general quadratic coefficient has a simple zero at \(s_c=2/(n+1)\); rewriting the even analytic expansion in \(q=\varepsilon^2\) and applying the implicit-function theorem gives the displayed square-root branch and gain coefficient. These statements are confined to the translated-unit-ball family, as claimed.

### Correctness sources

- assigned RESULT.md
- published 2026/09/19 quartic-translation record
- published 2026/09/18 Gaussian Hessian record

### Correctness risks

- The protected full-text retrieval attempt for the motivating 2026 preprint was blocked; correctness does not depend on that unavailable comparison because the relevant expansion is reconstructed directly.

## Originality — FAIL

A published 2026-09-19 record already gives the same critical translated-ball quartic expansion with the same negative coefficient in equivalent normalization. A published 2026-09-18 record already gives the full quadratic Hessian and the exact degree-one coefficient crossing at \(2/(n+1)\). Once those two prior formulas are combined, the assigned nearby symmetry-breaking branch, its radius, and the order-\(\delta^2\) gain are the standard even-analytic implicit-function expansion. The assigned final claim is therefore covered by prior published ingredients.

### Equivalent formulations

Its \(C_n\) is algebraically the same quartic coefficient as the assigned \(\beta_n\); this already covers the endpoint theorem.

### Broader coverage

Together they give the complete local normal form needed for the assigned translated-ball pitchfork calculation.

### Exact database or table

This is direct theorem coverage, not a database-only coincidence.

### Claim versus prior implication

Solving \(\partial_q\Phi=0\) is a routine implicit-function step, so the branch and gain are mechanically implied.

### Sources inspected

- Quartic stabilization of the critical translation mode in the Gaussian Santaló product — published record 2026/09/19/gaussian-santalo-ball-full-hessian-spectrum--89fed354a859. COVERING: It contains the same endpoint quartic stabilization theorem.
- Exact spherical-harmonic Hessian and instability index for the Gaussian volume product — published record 2026/09/18/gaussian-volume-product-hessian-instability-index--adb76edfac12. COVERING_INGREDIENT: It supplies the complete quadratic translation coefficient used in the local branch calculation.
- Uncentered Blaschke-Santaló inequalities for the Gaussian measure — https://arxiv.org/abs/2609.18472. PARTIAL_ACCESS_NOT_DECISIVE: The originality failure is already decisive from the two earlier published same-object records.

### Checked sources

- published 2026/09/19 quartic translation record
- published 2026/09/18 Gaussian Hessian record
- https://arxiv.org/abs/2609.18472
- Resultary semantic search

### Residual risks

- The inaccessible full text of the motivating preprint is not needed for the rejection because stronger prior coverage is already explicit.

## Value — FAIL

The branch formula is correct and useful as a corollary, but after the earlier quadratic and quartic formulas it is a standard one-dimensional even-analytic bifurcation calculation rather than a distinct research gap.

### Value sources

- published 2026/09/18 Gaussian Hessian record
- published 2026/09/19 quartic translation record

### Value risks

- This rejection concerns distinct scientific contribution, not mathematical correctness.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The theorem concerns translations of the unit ball only.
- The source paper's protected full text was not retrieved in this audit; decisive prior coverage makes that access gap nonblocking.
