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

# Verification of the new result

Run `python3 verify_natural4_monotone.py` with Python 3's standard library. The included execution result reports `PASS: 5050 exact-rational derivative checks; all middle coefficient identities; sharp boundary witnesses`. This checks polynomial derivative identities from independently constructed rational natural curvatures and strictly negative witness derivatives beyond the proposed contrast cutoff; the file contains executable checker source and a same-directory output record. The proof for every \(r>0\), every continuous evaluation point and every positive-slope triple is provided in `RESULT.md` and is independent of the finitely many tests. No independent audit or formal-machine proof is claimed.
