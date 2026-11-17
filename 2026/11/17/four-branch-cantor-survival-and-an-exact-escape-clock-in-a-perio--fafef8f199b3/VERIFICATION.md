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

From the directory containing these embedded files, run `python checker.py` using Python 3.9 or later. The script relies only on the standard library and uses exact rational arithmetic for all branch endpoints, image inclusions, finite cylinder identities and recurrence cross-checks.

The analytical proof in `RESULT.md` supplies the required infinite-level arguments: a direct four-branch computation, strict branch separation, a nested-cylinder conjugacy, a separated-similarity dimension argument, and normalized Lebesgue measure of the finite survivor cylinders. No extrapolation from finite experiments is needed.

The threshold nonlinearity is defined on zero explicitly. The boundary of the survivor consists of genuine repelling periodic points in the stated parameter region. This verification does not establish claims in the complementary parameter bands and does not constitute independent scientific validation.
