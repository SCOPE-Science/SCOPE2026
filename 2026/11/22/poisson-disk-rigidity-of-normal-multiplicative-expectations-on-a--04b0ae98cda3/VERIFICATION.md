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

For each n>0 and any m, both V and U^n V^(m-1) belong to A. Their two products differ by the nontrivial scalar lambda^(-n) but have equal values under a scalar multiplicative functional. The transverse Fourier coefficients vanish, including negative n by the adjoint relation; powers and adjoints of V give the remaining moments. The trace on W*(V) has Haar spectral law, so equality in the first-moment norm bound would require a normal state to charge a zero spectral projection at one point. For interior zeta the displayed density has the correct conjugate placement: the coefficient of V^(-m) is zeta^m for m>=1. Its integral is one and its positive lower bound proves faithfulness. Analytic polynomial multiplicativity extends by separate ultraweak continuity in each argument, and density of all Laurent monomials gives uniqueness among normal extensions. For entropy, log|1-conj(w)v| is a harmonic boundary datum, and its Poisson expectation at zeta is log|1-conj(w)zeta|; substitution yields the specified symmetric ratio with equality only at zeta=eta. The supplied quadrature script was inspected, not rerun; the proof does not need finite numerical evidence.

## originality

PASS

The supported distinct claim is exhaustiveness for all normal multiplicative scalar expectations and the consequence that all are faithful, not existence along complex radial rotations or the classical entropy identity. Ji constructs the same algebra and radial expectations but does not establish the classification in the relevant construction and theorem. The checked broader representing-measure framework extends characters already given on the analytic algebra; it does not identify them all there.

## value

PASS

For the explicit counterexample algebra, the natural next question is whether the exhibited expectations exhaust the possibilities and whether nonfaithful normal examples are hidden. The Fourier rigidity and Haar-null boundary argument answer both exactly and identify each density. That complete classification is useful independently of the known entropy identity; rotating the old construction or restating Cauchy divergence alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
