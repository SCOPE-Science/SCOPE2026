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

The proof is a residue-count argument that applies at every finite period and every positive integer \(K,Y,H\) with admissible training and test windows. The attached standalone `verification.py` recomputes phase multiplicities and checks the stride formula over 1,755 finite parameter combinations. It additionally builds actual periodic length-five history tuples at \(P=29\), confirms the full-test exact-neighbor fraction \(31/899\), and confirms the stride subsample fraction \(31/31\). Run `python verification.py`; expected stdout begins with `VERIFY_OK`. Checks are finite corroboration, not a certificate for all integer parameters. The proof does not assert that unsaturated histories must produce forecasting errors.
