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

The independent calculation path `checker.py` verifies the gap-word encoding, brute-force acceptance against dynamic programming for finite lengths, and finite-prefix exact calibration identities. Run `python checker.py`; expected terminal line `ALL_CHECKS_OK`. The proof of existence of limits uses the published layered-permutation convergence theorem, and rationality uses finite-state rational transition systems. The exact attainment of every rational is proved by stopping-time independence of nonoverlapping marker samples. Finite tests do not establish infinite limits or historical priority.
