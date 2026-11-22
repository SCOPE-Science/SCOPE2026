---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The full theorem is established by exact two-eigenmode integration, a quartic-deficit factorization, a trigonometric cubic cross-moment identity, and a four-cycle Hilbert-valued parity cancellation. The attached `check_cycle_square.py` uses symbolic algebra for the polynomial identity and rational four-cycle coefficients, numerical checks on 496 cycles, and 200 complex-Hilbert-signal examples. These computations were run against the included script and all its assertions passed. The argument for all cycle orders is analytic, not based on numerical extrapolation.

Boundary cases: \(n=3\) gives equality for every signal; \(n=4\) admits exactly the pointwise real-orthogonality equality condition; \(n=5\) already fails; \(n=6\) has a folded frequency-three mode but the explicit cubic bound remains valid.

The primary literature establishes universal semigroup bounds, not this exact finite-cycle threshold. Bibliographic completeness and independent theorem validation remain outstanding. No assertion of unrestricted optimal constants on the failing cycles is made.
