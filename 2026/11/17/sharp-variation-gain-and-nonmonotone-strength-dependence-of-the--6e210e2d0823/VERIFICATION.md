---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For λ>0 resolvent partial fractions reduce (I+λL²)^−1 to conjugate nearest-neighbor Green kernels; the decaying q root gives a geometrically summable real kernel of mass 1. D commutes with convolution, so Young and a one-step input give exact BV gain ∑|K(j)|. Negative sine lobes force >1; Neumann ℓ1 expansion yields 1+4λ+O(λ²). As λ→∞, rescaling j/λ^(1/4) with an exponential envelope yields the closed damped-sine absolute integral 1+√2e^(−3π/4)/(1−e^(−π)); first sign-change scale is 3π/(2√2)λ^(1/4). Exact rational finite-section residual bounds rigorously certify nonmonotonicity.

## originality

PASS

McElroy has already derived the exact bilateral HP Green coefficients and their signed lobes, and the BV convolution norm equals their ℓ1 mass by a standard jump reduction. The meaningful added claims are rigorously certified decrease in gain as λ rises from 1/16 to 1/9, the explicit strong-smoothing limit 1+√2 e^(−3π/4)/(1−e^(−π)) and the first negative lobe scale; none is stated by the relevant full McElroy material or distinct finite-path order/positivity result.

## value

PASS

The Hodrick–Prescott low-pass estimator is a natural filter and bounded variation is a natural stability invariant at discontinuities. The theorem identifies exact jump-extremizers, unavoidable ringing, an unexpected rigorously certified reversal under stronger smoothing, and a closed saturation constant. It measures behavior distinct from conventional frequency-domain or squared-error estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
