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

# Reproducibility

Run `python3 check_sparse_cycles.py` with Python 3.9 or later; no third-party packages are required. The script independently constructs the full Hamming-limited de Bruijn digraph and enumerates every permissible local edge order for \(q=3,n=2,3,4\), \(q=4,n=2\), and \(q=2,n=2,\ldots,11\), retaining exactly the tours that traverse every edge once and verifying their distinct circular windows. It separately constructs the contracted weight-one Laplacian and computes its exact integer determinant by the Bareiss algorithm for \(2\le q\le5\), \(2\le n\le9\). Expect the final token `VERIFY_OK`.

The standalone exact computations confirm finite cases and boundary normalization only. The theorem for all \(q\ge3\), \(n\ge3\) follows from the displayed BEST/Matrix–Tree proof and the explicit upper-triangular determinant transformation. No external independent validation was carried out.
