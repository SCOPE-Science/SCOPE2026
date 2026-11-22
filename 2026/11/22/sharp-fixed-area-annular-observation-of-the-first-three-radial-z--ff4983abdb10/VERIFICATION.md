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

The analytical proof establishes the identities and variational comparison uniformly for every area fraction \(q\in(0,1)\) and every admissible annulus position. No finite numerical experiment is used as a substitute for that universal argument.

Reproduce using `python check_annulus.py` with SymPy and NumPy. The self-contained checker executes symbolic integration and confirms 7 exact identities, independently computes 9 original planar disk polar integrals, and tests the global strict displacement estimate in 288 parameter cases. It also confirms the exact area-one-half example \(\lambda_-=(113-9\sqrt{145})/256\).

The checker does not prove independent historical priority, certify machine-verified formal mathematics or establish new results about arbitrary Zernike bands. An independent mathematical audit has not been performed.
