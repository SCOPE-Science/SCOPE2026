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

# Reproducibility and proof limits

The mathematical assertion is proved in `RESULT.md` by the explicit arch factorization and last-occurrence recurrence; no external certificate or computational completeness claim is used. `check.py` can be run using Python 3 without third-party packages. `check_output.txt` contains the captured execution result. The checker generates finite iterates from the stated morphism and compares the whole shortest-absent language with an independent next-occurrence dynamic program; selected instances are also checked by direct enumeration of every word at the proposed absent length.

The recorded run reported 630 successful instances, of which 22 underwent direct exhaustive length-level comparison. They test selected alphabets, blocks and tails, not all infinite parameters. The proof itself is the only justification for the universal quantifiers. The full external independent audit has not been performed.
