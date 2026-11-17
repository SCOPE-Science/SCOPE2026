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

# Verification of the uniform-vertex covariance spectrum

The self-contained checker `artifacts/verify.py` requires Python 3 and only its standard library. From the package root, run `python3 artifacts/verify.py`. Its expected successful completion line is:

`TWO_HUB_VERTEX_COVARIANCE_CHECKS_PASSED full_matrices=7 q_inequalities=98`

For each of \(q=3,4,5,6\) it enumerates all orders of the \(q+2\) labeled graph vertices, induces and deduplicates the corresponding acyclic edge orientations, and independently reconstructs the two-ternary-family model. For \(q=7,8,9\) it enumerates the ternary encoding directly. For all seven sizes, it derives the complete covariance matrix with exact rational arithmetic and verifies the claimed eigenoperator on a spanning basis, the zero-sum constraint, the vertex count, and the centering. It also checks the strict ordering and gap identity for each integer \(3\le q\le100\).

The mathematical argument proving the infinite-family statement is the symbolic counting and variance calculation in `RESULT.md`. A finite enumeration cannot establish an assertion for arbitrarily large \(q\); it checks for implementation and algebra mistakes in representative cases. No independent mathematical audit is claimed or performed.
