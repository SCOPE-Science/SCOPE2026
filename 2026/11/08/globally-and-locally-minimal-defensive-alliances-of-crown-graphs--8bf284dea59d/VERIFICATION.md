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

# Computational verification

Run `python3 verify_crown_alliances.py` using Python 3.10 or later. It independently enumerates defensive alliances by the original vertex-neighborhood inequality on all labelled crown graphs of orders \(3\) through \(8\), and tests local minimality by individual deletions and global minimality by strict alliance containment. It separately checks the proposed family classification and symbolic binomial counting formulas. The verifier uses only the standard library.

The finite calculations are strictly supplementary to the proof in `RESULT.md`: a finite run cannot establish a theorem for all \(n\ge3\). The assumptions include simple graphs, the fixed deleted perfect matching, and the ordinary closed-neighborhood defensive-alliance inequality.
