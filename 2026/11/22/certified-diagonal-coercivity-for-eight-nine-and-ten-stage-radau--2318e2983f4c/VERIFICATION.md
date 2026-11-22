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

# Reproducible scientific verification

Invoke `python3 check.py` in the directory containing this file. The included standalone code is its complete dependency; it needs Python 3 standard library only. Its real operations are exact-rational sign and inequality comparisons, except for optional floating-point display after each success.

For each of the stage counts \(8,9,10\), the checks performed are: all \(s-1\) shifted-Jacobi root intervals have exact opposite endpoint signs and are disjoint; all denominators in the barycentric derivative formula exclude zero; all displayed diagonal weights are strictly positive; the entrywise interval enclosure for \(C_s\) is valid; the largest exact rational row-sum error against its central rational matrix is less than \(1/20000\); all exact rational unpivoted \(LDL^{\mathsf T}\) pivots for the central matrix minus \(I/1000\) are positive. The spectral inequality \(C_s\succ(19/20000)I\) follows analytically from those verifications.

The verifier succeeded when run from the current complete package, for all three stage counts. Printed maximum row errors were approximately \(2.94\cdot10^{-5}\), \(2.50\cdot10^{-5}\), and \(2.71\cdot10^{-5}\), respectively, and were accepted only after exact rational comparison. These decimal values are explanatory diagnostics, not computational proofs. No result for stage counts outside the listed finite set is verified. A separate independent audit has not been performed.
