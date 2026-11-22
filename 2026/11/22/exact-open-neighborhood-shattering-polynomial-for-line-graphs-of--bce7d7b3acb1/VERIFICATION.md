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

# Reproducibility and verification

Run `python verify.py` from an extracted copy of the artifact. It uses only the Python standard library and independently generates labeled trees via Prüfer codes, constructs each line graph's open-neighborhood traces, exhaustively checks all supports of sizes one through four, compares coefficients with the structural formula, and tests the nine-vertex extremizer. Expected result: `VERIFY_OK 18948 trees; four-support checks and nine-vertex extremizer`. A separate test over all unlabeled trees of orders two through thirteen counted 2,287 isomorphism types and agreed. The infinite claim rests on the explicit proof, not on experiments or a certificate of independent validation.
