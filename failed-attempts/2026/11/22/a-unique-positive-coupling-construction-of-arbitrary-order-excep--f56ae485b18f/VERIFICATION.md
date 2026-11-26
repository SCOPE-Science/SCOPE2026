---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The determinant recurrence adds g_j² times the preceding minor, since (ig_j)²=−g_j². Parity divides (z+β)^m into Q_m and γQ_{m−1}, and the trace forces γ=mβ. The leading term of each backward remainder then recovers g_j² uniquely, with no sign ambiguity under g_j>0. With λ=1/2−m the monic Gegenbauer recurrence has no vanishing leading coefficient or denominator in the required range and gives the stated positive g_j² for all j<m. For degrees m and m−1 the eigenvalue in the differential equation is the same. The parity pieces of (z±β)^m solve that equation and match the monic solutions: both possible leading degrees are roots of the leading-term equation, but only one of those degrees lies in each parity, so no lower same-parity monic difference is possible. This gives exactly (z+β)^m. Nonzero nearest-neighbor entries force a nonzero eigenvector to have nonzero first coordinate and determine all other coordinates from it, so the sole eigenvalue has exactly one Jordan block. This checks the amplitude-loss convention and all m≥2 and β>0, not detuned sites, extra loss sites or robustness. Frozen verify_ep.py and VERIFICATION.md were inspected, not executed; their exact rational examples are consistency checks, not the universal proof.

## originality

FAIL

Arlinskiĭ–Tsekanovskiĭ Theorem 5.1 and especially Example 5.3 cover the same unique full-coalescence design for every dimension after a sign, scale and endpoint change. Although Example 5.3 does not print the compact all-size coefficients, its exact Weyl fraction yields them by a single standard terminating Gauss continued-fraction specialization. This is established prior implication, not just a related title, unavailable-source suspicion, or matching low-order examples.

## value

FAIL

The explicit numbers are useful design data, and the Gegenbauer derivation can serve as an exposition. As a standalone finding, however, this is the identical known collapsed-spectrum construction with its Weyl fraction evaluated by a standard identity. The exact novelty proposed as a valuable narrow invariant is mechanically implied, and no additional physical or mathematical result survives that comparison. No substantive repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
