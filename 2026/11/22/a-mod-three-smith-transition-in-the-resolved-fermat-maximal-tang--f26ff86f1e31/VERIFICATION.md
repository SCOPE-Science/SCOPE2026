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

# Reproducibility and scope

The proof is the integer row/column presentation in `RESULT.md`. It proves all degrees \(d\ge3\), with no computational extrapolation. The standalone Python script `verify.py`, with the dependency in `requirements.txt`, independently constructs a new reduced graph Laplacian from the stated edges and checks its exact Smith factors against the formula and the five-generator matrix for all integer degrees 3 through 12.

Run `python verify.py`; successful execution prints `FERMAT_MAXIMAL_TANGENT_BOUNDARY_UNIFORM_INTEGRAL_GROUP_OK`. The computation uses exact integer arithmetic, not random or floating-point tests. The five-generator determinant and prime-local decompositions are also explained in `RESULT.md` and are the infinite proof.

The geometric Néron component-group interpretation is conditional on a regular split semistable smoothing whose special fiber is the specified resolved boundary with unit node thicknesses. No independent validation has been performed, and unindexed historical priority remains unresolved.
