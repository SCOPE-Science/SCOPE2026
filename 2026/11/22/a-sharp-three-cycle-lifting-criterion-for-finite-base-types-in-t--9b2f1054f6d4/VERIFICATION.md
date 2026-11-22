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

# Reproducibility

Run `python verify.py` using Python 3 standard library. It constructs random finite non-antipodal circular bases, samples exact rational coordinates within each induced type arc, and tests every ordered one-type triple for directed-cycle realization. It compares the observed count with the symbolic formula for positive base sizes one through eight. It is not a universal exhaustive proof; see the cyclic-gap argument in `RESULT.md` for the full mathematical justification. The exact construction and tested random seed are in the embedded script. All original source citations are given in `RESULT.md`.
