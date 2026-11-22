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

# Verification record

The exact standalone script `VERIFY_PONCELET.py` uses the Python 3 standard library only. It runs over prime fields \(\mathbb F_p\) for \(p=3,5,7,11,13,17,19,23\). For every admissible \(c\), it constructs the split and nonsplit projective conics and enumerates all \(p+1\) rational points and all chord pairs, tests dual-conic tangency exactly, and checks either the complete predicted \(n\)-cycle decomposition or the absence of rational tangent edges. It derives \(n\) by an exact integer-modulo-prime recurrence for \(r+r^{-1}\), then enumerates all Frobenius-invariant cosets and their fixed-vertex counts, separately verifying rotation, odd reflection, and even reflection distributions.

Run: `python3 VERIFY_PONCELET.py`. The expected final line is `PONCELET_DESCENT_EXACT_CHECKS_OK`.

This verifier establishes the reported finite computational instances. The result for arbitrary odd prime powers is established in RESULT.md by projective normal forms, an exact chord equation, descent through the torus-isogeny quotient, and exact cyclic group calculations. No infinite theorem is inferred from a bounded enumeration. Literature priority is provisional and independent scientific validation has not been performed.
