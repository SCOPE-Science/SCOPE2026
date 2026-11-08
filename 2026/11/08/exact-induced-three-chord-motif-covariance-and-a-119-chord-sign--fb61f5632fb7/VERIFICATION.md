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

# Verification of the exact induced three-chord motif covariance

Run `python3 check.py` from this artifact set using Python 3.9 or later. No dependencies or additional files are required. The verifier constructs every word of length \(2k\) on \(k\) labels, with each label appearing twice, for \(k=5,4,3\). These are respectively \(113400\), \(2520\), and \(90\) words. It checks all entries of \(Q_1,Q_2,Q_3\) against integer rational tables, rather than sampling.

It then constructs every perfect matching of \(2n\) endpoints for each \(3\le n\le7\), checks all four mean formulas, and checks all sixteen covariance entries independently against the polynomial formula. The matching-space sizes are \(15\), \(105\), \(945\), \(10395\), and \(135135\). Seven additional rational substitutions verify the overlap expansion, and exact polynomial sign tests cover the displayed cutoffs. The actual program run returned `ALL CHECKS PASSED`.

The finite enumeration is complete for the *small restriction words needed in the proof*; it is not claimed to enumerate diagrams for every \(n\). The proof for arbitrary \(n\) is the exact overlap decomposition with those small rational joint tables, followed by closed-form polynomial arithmetic and monotonicity. Independent external review is not performed.
