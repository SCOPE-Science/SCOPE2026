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

# Verification

The standalone standard-library program `verify_orthogonal_kernel.py`, embedded unchanged with this result, was executed from the research package and returned `PASS: 605 finite regression checks`.

Its tests compare the direct Euclidean projection parameter with the exact ellipse threshold across even polygon sizes, verify three small even-n radical cases, evaluate the ellipse tangent residual against a deterministic high-resolution angular grid, and examine the asymptotic constant on increasing n. The uniform all-mesh rigidity, minimax optimality, sharp all-even-n threshold and large-n limit rely on the complete mathematical proof, not on finite computation. Historical priority and independent audit have not been certified.
