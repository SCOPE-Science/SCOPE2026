# Mathematical review

## Correctness (C) — PASS

For positive \(u,v,\gamma,\omega\), the reflected Hessian is \(K=((u\cos2\theta,-v\sin2\theta),(u\sin2\theta,v\cos2\theta))\), with trace \((u+v)\cos2\theta\) and determinant \(uv\). The four-dimensional characteristic polynomial is explicit. Its Routh--Hurwitz inequalities reduce to one strictly increasing quadratic in the positive trace, giving exactly one boundary \(\theta_*\). Direct factorization at equality establishes a simple imaginary pair, a second pair with real part \(-\gamma\), and a nonzero crossing derivative. Zero and negative trace cannot be stable. The proof is analytical and covers all positive coefficients and all stated angles. The packaged symbolic and numerical checker passed. Risk: numerical evidence by itself does not prove uniform infinite-parameter statements; those follow from the symbolic and Routh--Hurwitz arguments.

## Originality (O) — PASS within the inspected literature

The direct motivating source, Shi et al. (2026), §5.2 Theorem 10, supplies a perturbation-size *sufficiency* theorem; it does not identify the exact two-dimensional threshold or prove the early oscillatory instability. Luo et al. (2023), §3, analyze *exact* Hessian eigenvectors in the accelerated flow. Chu and Lin (2025), §§2–4, concern reflector geometry and first-order gentlest ascent rather than heavy-ball acceleration. An earlier first-order fixed-projector \(45^\circ\) sharp stability bound cannot imply the accelerated threshold because the latter is sensitive to complex reflected-Hessian eigenvalues. Direct literature and mathematical-record searches for rotated/inexact heavy-ball projectors and equivalent quartic criteria did not locate the exact theorem. Residual risk: a classical linear second-order nonconservative system might already contain an equivalent parameterized condition not indexed under the saddle-search terminology. No independent exhaustive historical priority audit is claimed.

## Value (V) — PASS

A sharply specified input-accuracy requirement determines whether inertial acceleration is safe for a natural minimal saddle-search model. The result exposes a non-obvious region where the unaccelerated algorithm converges globally while the accelerated algorithm diverges, including an explicit \(25.91^\circ\) versus \(45^\circ\) mismatch at unit parameters; it also separates reflected-Hessian spectral coalescence from actual stability loss. This is more informative for algorithmic design than another sufficient small-error bound. Its limited two-dimensional fixed-projector scope is explicit, rather than claimed as a general convergence theorem.

## Evidence and independent status

The critical identities, source comparisons and reproducibility checks appear in `RESULT.md`, `AUDIT.json` and `VERIFICATION.md`. Scientific correctness and priority have not been independently validated.

Self-review: passed. Independent audit: not yet performed.
