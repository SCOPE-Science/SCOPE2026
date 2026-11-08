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

The standalone `verify.py` requires Python 3.10 or later and uses only the standard library. Run `python3 verify.py`. It computes exact rational weighted transmissions for every labelled seed subset of \(D_{a,b}\) with \(2\le a,b\le5\), testing 36 rational parameter pairs per graph. It compares the full cardinality distributions with the sixteen-configuration quotient, for 576 graph/parameter instances, and verifies the tree upward-closure counterexample at \(a=b=2\), \(\alpha=4/5\), \(\beta=1\). The finite checks independently corroborate a universal structural proof and do not constitute an independent scientific audit.
