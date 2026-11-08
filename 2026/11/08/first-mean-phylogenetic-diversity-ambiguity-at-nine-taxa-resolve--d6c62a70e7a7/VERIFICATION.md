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

# Verification and reproducibility

Execute `python3 check_pd_fingerprints.py` in the directory containing the verification file. The checker uses only the standard library and reconstructs every rooted nonplane full-binary shape with two through nine leaves. Its recurrence is exhaustive by decomposition at the root, with a canonical tie break when two child sizes agree. The script asserts the shape counts \(1,1,2,3,6,11,23,46\), the corresponding mean-fingerprint counts \(1,1,2,3,6,11,23,45\), and the unique nine-leaf two-shape collision.

Each mean-fingerprint coefficient is computed from descendant clade sizes. Variance coefficients follow from nested-clade indicator covariance and are compared exactly. For the witness pair, a separate survivor-mask enumeration sums all \(512\) configurations per tree at \(p=1/2\), yielding identical means \(335/32\) and variances \(6483/1024\), \(6491/1024\). These finite tests independently check the algebraic witness; the all-parameter assertion follows from the symbolic covariance identity in `RESULT.md`.

The checker does not establish historical priority, empirical statistical power, or any extension beyond the explicitly defined model. No independent audit or field validation has been performed.
