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

The non-contingency semantics were independently implemented from the displayed definitions in `check.py`. Execute `python check.py` in the directory containing the extracted files. It enumerates the exact single-arc-reversal family through order nine, and every Boolean valuation on each member through order eight. Expected output: `VERIFY_OK reversals= 119 singleton_assignments= 868 all_valuation_assignments= 11256`.

The finite checks do not prove the formula for arbitrary order. The proof in `RESULT.md` classifies all possible singleton failure roots from directed triangles and verifies full validity for both exceptional tournament families. The result does not assert the singleton-support property for arbitrary tournament frames.
