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

The proof uses an exact derivative identity, standard convex-comparison criterion and Kaplan's angular-turn necessity. The signed limiting turn is strictly less than \(-\pi\) for each integer \(p\ge3,N\ge2\), so continuity establishes a finite-radius counter-witness without relying on numerical threshold guesses.

Run `python CHECK.py` (Python 3, standard library only) for finite coefficient and angular-turn checks. The script does not prove the all-parameter theorem. An earlier related full text was inaccessible, and independent validation was not performed.
