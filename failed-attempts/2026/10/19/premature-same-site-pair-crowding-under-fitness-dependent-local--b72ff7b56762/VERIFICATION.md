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

For the stated subcritical mean-field chain the stationary polynomial moments are finite, e.g. by comparison to the same linear birth/immigration and death process without resets. Applying the generator to N(N-1) gives the birth contribution 2N(ℓN+u), the death contribution -2(1+ζ)N(N-1), and one whole-site reset contribution -rN(N-1). This gives 2(ℓ+u)u/[(a+r)(2a+r)] with a=1+ζ-ℓ. Multiplication by the level multiplicity leaves the displayed ℓ-times-input term as v grows. At fixed ζ the linear mean equation on the grid has positive denominator for large L by Riemann convergence and βB_0<1, and the bulk normalized sum tends to the displayed integral. The original grid prescription has q(1)=r(1)=0 and v_L=1, giving an extra 2/(Lζ²), negligible only at fixed ζ. The first moment converges to A_0/(1-βB_0)>0 by domination. Uniform near-endpoint numerator convergence to 2 and r(1-ε)~Cε^ν give an integrable ε^{-2ν} bound for ν<1/2. For ν>1/2, rescale by ε=(ζ/C)^{1/ν}x; on the endpoint region a constant times (1+x^ν)^{-2} dominates the scaled integrand, and the rest is bounded before rescaling. With p=1/ν, the integral after t=x^ν involves t^{p-1}/[(1+t)(2+t)]; writing the denominator factor as ∫_1^2(t+s)^{-2} ds and integrating in t gives Γ(p)Γ(2-p)∫_1^2 s^{p-2}ds/ν, exactly π(1-2^{p-1})/[ν sin(πp)]. At ν=1/2, integrate between M(ζ/C)^2 and fixed small h: the integrand is uniformly within arbitrarily small relative error of 2/(C²ε) when M is large and h small, while both omitted regions contribute O(1) for fixed M,h. This yields 4C^{-2} log(1/ζ). Grange's ν=1 result is the onset, already logarithmically divergent there; the frozen comparison does not assert that the mean stays finite at ν=1. RESULT.md, VERIFICATION.md and checks/checker.py were inspected; the reported 32 finite numerical consistency checks were not rerun and do not establish the limits. No claim is made about a finite interacting network outside the one-site closure or about different-site covariances.

## originality

FAIL

Distinct catalogue record b88c55090541 covers the substantive frozen result at statement level: same local stationary marginal model, same input and mean closure, identical ordered pair integral, same parameter domain for the frozen physical profiles, and the same finite/log/power regimes and constants. It additionally gives a diagonal variance identity, not a result retained from the frozen claim. This is demonstrated equivalent coverage in the available catalogue, not an attribution or assertion that the later-dated comparison preceded the frozen record. The finite-grid endpoint omission in the comparison is only a fixed-cutoff Riemann-limit detail of the equivalent continuum theorem, not a separate substantive pair-threshold contribution.

## value

PASS

The mathematically meaningful content is an integrated fluctuation threshold with sharp coefficients in a regime where the mean stays finite, not the elementary stationary moment identities by themselves. It distinguishes physically different local observables and identifies a genuine earlier singularity under the specified order of limits. That intrinsic utility does not overcome exact equivalent coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
