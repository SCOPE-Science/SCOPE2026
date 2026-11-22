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

Cyclic shift matrices T_k are orthogonal with Frobenius squared norm n. For every doubly stochastic X their circulant orthogonal projection has nonnegative coefficients summing to one; thus it is already the nearest point of the cyclic-shift simplex. For vertex permutation π distance²=n−Σ m_k²/n. The integer histogram has sum n and displacement congruence Σ k m_k≡0 mod n; balancing yields all-ones odd case and a doubled-missing difference n/2 in even case. Explicit 2i constructions attain both and the difference-of-squared-residuals variance identity rules out any nonvertex maximum. Integer-square increments come in even steps, with swapping images giving next vertex level. Checked exceptional n=3 separately and n=2 equality of convex sets.

## originality

PASS

Compared this final mathematical assertion with semantically relevant published findings and primary material by implication, not title; known tools and special-case results were excluded from the new part. Remaining source-access limitations are explicit.

## value

PASS

Sharp directed Hausdorff approximation between a classical stochastic polytope and its canonical circulant simplex, together with parity-rigid farthest points and next vertex-level gap, is a natural matrix-geometry question. Exact second discrete shell adds quantitative robustness beyond elementary averaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
