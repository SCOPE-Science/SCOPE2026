---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For each positive continuous even weight the Neumann form splits by parity. On the half interval, w(x)∫_x^1w(y)⁻¹dy≤1−x, so ‖v−v(1)‖²≤E(v)/2. For even mean-zero tests, projection onto constants gives ‖v‖²≤‖v−v(1)‖², so the even gap is in fact at least 2; the weaker 1/2 in the source is valid. For odd form-domain tests the trace bound |v(1)|≤√(HE(v)) and the endpoint estimate give the lower bracket. The resistance function r=H⁻¹∫_0^xw⁻¹ has energy 1/H and norm at least √M−1/√(2H), giving the upper bracket. Thus odd dominance holds uniformly for large MH. In the flux equation for the positive mixed-boundary ground state the rate is λ_odd, which agrees with λ₁ in the relevant regime. Positivity and zero right flux give 0≤u≤1 and 1≤HE(u)≤λ_odd MH→1. The cross term of u and r in the energy is exactly 1/H, so H E(u−r)→0 and Cauchy–Schwarz gives uniform closeness. The normalized derivative vectors have inner product (HE(u))⁻¹/², giving L¹ convergence of their squared densities by Cauchy–Schwarz, preserved under the pushforward. At α=1+t/L with L=log(1/ε) and Q=log((1+ε)/ε), H/L=e^t(1−exp(−tQ/L))/t continuously at t=0, M→1/2 and the normalized resistance density in s is proportional to exp(−tQs/L). This supplies the stated eigenvalue and both profiles for t positive, negative and zero. Fixed α>1 gives M→1/(α+1) and ε^(α−1)H→1/(α−1).

## originality

PASS

Best-of-knowledge pass for the combined uniform mass–resistance asymptotic and explicit critical-window eigenvalue, normalized mode and dissipation profiles. Endpoint Hardy estimates and capacity-based spectral mechanisms are classical; the exact constants or profiles are not advertised as new independently of their specified regime. Existing general capacity theory is a serious possible source of implicit coverage, and its unavailable decisive passages limit the comparison.

## value

PASS

The exact rate of loss of coercivity, the normalized low-mode shape and the dissipation location are three useful observables of the same interface degeneracy. The uniform monotone-weight argument and the explicit continuously parameterized critical crossover give more than a rough bound or a selected exponent. The role of symmetry, monotonicity and one dimension is material, not a claim of broader diffusion universality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
