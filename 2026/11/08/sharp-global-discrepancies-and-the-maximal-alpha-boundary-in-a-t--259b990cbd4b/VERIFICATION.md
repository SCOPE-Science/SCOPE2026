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

# Reproducibility and limits

Run `python3 discrepancy_verify.py` with Python 3 standard library. It uses integer enumeration and exact rational arithmetic, not symbolic numerical tolerances. Its checks cover 27 admissible small triples with dimensions two through four and a seven-term boundary sequence; they are not an infinite proof. The complete proof appears in RESULT.md and relies on Wu's primitive-ray description and standard toric discrepancy criteria. The verification did not attempt an independent audit of the mathematical statement.
