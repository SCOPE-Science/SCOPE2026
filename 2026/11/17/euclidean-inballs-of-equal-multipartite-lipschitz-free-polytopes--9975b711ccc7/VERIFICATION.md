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

# Reproducible mathematical checks

Execute `python3 checker.py` with Python 3.10 or newer. The checker uses only the standard library, integer arithmetic and rational fractions; it makes no network requests and reads no external papers or tables.

The six-point part exhaustively constructs signed spanning-tree tight potentials for all labeled trees, checks every cross-part and within-part metric constraint, deduplicates feasible potentials, and compares their exact centered variances and contact-normal ranks to the theorem. Test values include both sides and the equality \(t=5/3\). On larger finite cases it independently enumerates endpoint statistics, exact maximizing scores, contact counts and spanning-witness ranks. A rational resonance \(t=12/7\) for three parts of six vertices is included. The expected concluding line is `TRIPARTITE_INBALL_TRANSITION_AND_RESONANCE_ALL_CHECKS_PASS`.

These are finite sanity and boundary checks; the theorem for arbitrary sizes is proved separately by the convexity and centering arguments in RESULT.md. Historical novelty and external independent validation are not mechanically certified.
