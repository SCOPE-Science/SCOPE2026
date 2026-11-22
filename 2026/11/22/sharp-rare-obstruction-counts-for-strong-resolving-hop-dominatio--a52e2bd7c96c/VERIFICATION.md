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

## Checks
Rebuilt antipodal transversals and Hamming distance-two neighborhoods from coordinate words. `verify_small.py` directly checked every strong-resolving condition through dimension four and enumerated the full dimension-five census and one-parity dimension-six census. `verify_structure.py` independently reproduced the Clebsch neighborhood face vector, strongly regular parameters, intersection formula through dimension ten, and exact dimension-six obstruction count. Both scripts passed. Their recorded output is in `verification_outputs.txt`.

## Proof versus computation
The asymptotic coefficient and explicit error bound are established by the symbolic inclusion-exclusion and antipodal-consistency proof in `RESULT.md`. Finite program runs do not prove the asymptotic. The dimension-five incidence count is acknowledged as implied by earlier Clebsch-complex work. No independent mathematical audit is represented here.
