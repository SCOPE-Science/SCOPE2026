---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Under the known-identity point null and independent splits, the conditional qth moment is exp(q(q−1)kλ²||X̄||²/2); the chi-square integral diverges even at equality. For the balanced product, the per-coordinate precision eigenvalues are (1−λ)² and (1+λ)². This gives the mixed moment, and F≥E₁/2 proves divergence of its second moment at the marginal boundary. At λ=c/√d the two logarithms have the same random term c∑UᵢVᵢ/√d and both norm penalties tend to c²/2. The second-moment and cross-moment exponents are c²+c⁴/d+O(d⁻²) and c²+c⁴/(2d)+O(d⁻²), respectively, so the swap difference has the stated sharp coefficient and the variance gain is one quarter of it. Independence under the alternative gives the stated concave expected-log quadratic; r/(1+r)<1/√2 is exactly r<1+√2, with an unattained supremum beyond the open boundary. The exact finiteness threshold at each fixed d is distinct from bounded, nonzero variance as d grows. RESULT.md, VERIFICATION.md and checker.py were inspected; the bundled checker was not executed.

## originality

PASS

Pass for the scoped deterministic-shrinkage comparison, in particular the sharp high-dimensional loss of benefit from averaging the swapped directions and its constant. The universal split likelihood ratio, validity and unshrunk cross-fitting are established background; the marginal moment and log-growth computations extend known special cases by routine Gaussian algebra and receive no separate priority credit for those cases.

## value

PASS

The canonical nondegenerate bounded-null-variance scaling tests a concrete reason to use cross-fitting: reduction of null fluctuations. The common lognormal limit and the sharp e^(c²)c⁴/(4d) variance gain show that reversing the halves buys only a vanishing correction in that regime. This quantitative conclusion is useful even though the Gaussian integrals are elementary. The exact finite-moment versus oracle-growth boundary clarifies a second tradeoff; no power gain or data-dependent validity is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
