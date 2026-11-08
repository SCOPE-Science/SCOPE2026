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

Run `python3 verify_covariance.py` with the standard Python library. It exhaustively enumerates all compositions of each size \(2\le n\le14\), checks the coefficient identity for every cutoff, verifies the covariance and strict negativity, and tests its asymptotic approximation numerically at five larger sizes. It checks 226 finite assertions; the script's output is reproducible. The all-size proof is analytic and requires the residue estimate, the two uniform tail inequalities and the Gamma periodization given in RESULT.md. No external independent audit or infinite computer certification has occurred.
