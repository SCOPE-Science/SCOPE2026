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

Execute `python3 scripts/verify_orbits.py` from the artifact root. The program exhausts the 336-element projective group acting on the 140 full-branch twist presentations, checks all 112896 group compositions on all states, verifies orbit stabilizers and an independent character-sum trace classification. See RESULT.md for the separate genus-three Frobenius argument. The calculation does not certify other characteristics, all genus-five curves, or full geometric automorphism groups.
