---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Signed inclusion-exclusion over vertices and factorization over E(K_n[T]) give W_n(H)=(-1)^n sum_{S independent in H}(-1)^|S|2^(choose(|S|,2)). Reduction modulo two gives W=(-1)^n(1-n), hence even-n invertibility and odd-n evenness; removing a matching of a edges from K_n gives independent-set polynomial 1+nt+at^2 and witness W=(-1)^n(1-n+2a), yielding gap 1 or 2 and odd-n zero at the stated a. Modulo four, only independent sets of size <=2 matter, and toggling a fixed H-edge pairs exactly half the odd-n frequencies with valuation one. Independently computed the full 2^21 coefficient transform via an integer subset-zeta algorithm: n=7 has 73115 zeros, positive rank 2024037, minimum magnitude 2, and exactly 1048576 coefficients with two-adic valuation one. The supplied 39 seven-vertex graph6 orbit rows and weight column sum to the zero total, and the proof of exact all-order gaps is separate from the finite census.

## originality

PASS

Best-of-knowledge: actual proof and cited primary/read indexed comparisons distinguish the specific result from older general tools and different objects; this is not a guarantee of priority.

## value

PASS

The complete-graph edge-cover indicator is a natural large symmetric Boolean family. The all-order exact invertibility/gap dichotomy controls counting-convolution stability, while the 2^21-point K7 zero-orbit census is a complete, reproducible natural finite classification rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
