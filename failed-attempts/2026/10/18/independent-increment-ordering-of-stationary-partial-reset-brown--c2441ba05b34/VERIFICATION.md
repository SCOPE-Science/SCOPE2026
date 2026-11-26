---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At a fixed time in a two-sided stationary rate-one Poisson process the backward age and successive interval lengths are independent unit exponentials. Brownian increments conditional on these lengths are independent Gaussians, so unconditionally the weighted contributions are independent centered Laplace variables c^jY_j of variance c^{2j}. The sum is square-summable in variance; translating the two-sided construction gives stationarity, while synchronous coupling contracts any initial difference by c^{N_t}→0 almost surely, including coalescence at the first reset for c=0. For χ_s(u)=1/(1+s²u²), χ_{b^j/√2}/χ_{a^j/√2}=q_j+(1−q_j)χ_{b^j/√2}, q_j=(a/b)^{2j}; the j=0 factor cancels. Centering and summability of b^{2j}−a^{2j} give the claimed almost-sure and L² convergence. The log-Laplace integral follows by differentiating in u, giving derivative −2s²u/(1+s²u²) and zero value at u=0. Integrating x² against each symmetric density difference yields b^{2j}−a^{2j}, proving Lévy integrability by a positive summable majorant; the sign is strictly positive, with the a=0 convention. The increment distributions compose by the transform ratios; consistent finite-dimensional distributions with an independent π₀ start yield the claimed process and centered increments give the natural-filtration martingale. Symmetric unimodality follows by convolution and limit of the Laplace laws. A shifted symmetric interval has probability no greater than at zero and has arbitrarily small probability sufficiently far away. Since the first nontrivial mixture term is unbounded with positive probability and independent of the rest, the average is strictly smaller for every r>0. Equivalently, conditional on common unit exponentials E_j, the stationary Gaussian variance V_c=Σ c^{2j}E_j increases strictly for a<b, so every such Gaussian central probability decreases strictly. Jensen gives both convex-order claims, with strictness for nondegenerate centered noise and strictly convex tests with finite expectations. Inspected checker.py lines 10–77 but did not execute it; its finite rational identities, quadrature and truncation checks neither prove the process statements nor bear on priority.

## originality

FAIL

Verified prior coverage by direct implication, not a claim that a prior resetting paper explicitly states the entire package. The published stationary Laplace series and classical self-decomposition of each scale factor give the convolution order and infinitely divisible remainder term by term. The explicit mixture, Lévy kernel, consistent martingale and strict distributional comparisons require only direct scale changes, standard convolution consistency and elementary inequalities. No independently distinct substantive remainder of the frozen claim is established. This verdict does not depend on any inaccessible source or on a later index hit.

## value

FAIL

The raw-law comparison is physically natural and stronger than variance monotonicity, but the frozen result is a routine application of the already published explicit stationary Laplace series to standard scale remainders. The auxiliary martingale, strict Jensen comparison and every-threshold Gaussian variance coupling are immediate consequences of those available premises, and the written kernel is direct Lévy scaling. The package is useful exposition, without a supported new structural or exact-invariant contribution under this standard. No genuine surviving repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
