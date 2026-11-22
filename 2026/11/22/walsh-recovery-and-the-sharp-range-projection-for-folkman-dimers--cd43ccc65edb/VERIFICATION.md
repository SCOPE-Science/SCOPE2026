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

# Verification of exact Folkman matching-spectrum calculation

The binary edge-coordinate model is the subdivided double of \(K_5\), with a BFS spanning tree of 19 edges and 21 chords. The C++17 verifier generates its 40 edges from the explicit construction, checks every vertex has degree four, enumerates all perfect matchings by two distinct procedures (direct right-vertex backtracking and regular-tournament clone assignments), and compares the full reduced \(2^{21}\) incidence arrays. Each procedure returns 768 distinct matching patterns. Integer Walsh--Hadamard transformation returns 1,262,164 zero and 834,988 nonzero reduced Fourier multipliers, with 18 signed levels and least positive modulus 32. A second integer transform recovers the original data exactly. Transforming the nonzero-character indicator gives endpoint norm \(56,520,123/262,144\). Result token: `FOLKMAN_WALSH_PASS`.

The independent Python verifier constructs the same graph through a distinct source representation, independently enumerates regular orientations and assignments, performs its own integer Walsh transform, checks every signed-level count, verifies Parseval's identity and 14 direct signed-frequency sums, and reproduces the endpoint norm. Result token: `INDEPENDENT_FOLKMAN_WALSH_PASS`. It requires Python 3 with NumPy; C++17 alone reproduces the full spectrum without third-party dependencies.

These computations are **exhaustive for a proved complete finite search space**; the gauge-reduction and matching bijection, not mere tested examples, justify extension from the 21-dimensional calculation to all 40-edge characters. The general translation-average proof supplies optimality of the orthogonal Fourier range projection. No independent mathematical audit or external certification has been performed.
