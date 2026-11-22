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

Run `python3 verify.py` from the extracted folder with Python 3.9+. It constructs the exact data anew, checking all frequencies in all nonempty orders two through thirteen by two independent algorithms, and checks the full projection-kernel histogram. Successful execution prints `PASS` and exits without an error. The finite certificate establishes only the stated orders; it is not a proof of novelty or of an unrestricted all-length statement. No independent mathematical audit is represented.
