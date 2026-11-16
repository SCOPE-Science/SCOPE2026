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

The proof uses the signed weighted matrix-tree formula, the multivariate Prüfer identity, a mod-two rank reduction, and the adjugate identity for a weighted tree; every step is stated in `RESULT.md`.

To replay finite checks, run `python3 VERIFY.py` alongside this document. Complete integer Walsh transforms are computed from independent Prüfer enumeration for \(n=3,4,5,6\): the respective frequency counts are 8, 64, 1024, and 32768; minimum nonzero absolute values are 1, 4, 1, and 16; zero counts are 0, 30, 0, and 15000. Exact integer weighted-Laplacian determinants are also checked against the divisibility and extremizing signings for all dimensions \(3\) to \(13\), with 50 pseudorandom signings per dimension (fixed seed).

Expected final marker: `COMPLETE_GRAPH_TREE_WALSH_SHARP_CHECKS_PASS`.

The code does not exhaust signings beyond six vertices, and finite tests are not a proof for all orders. The text provides the general proof. Independent mathematical validation has not been performed.
