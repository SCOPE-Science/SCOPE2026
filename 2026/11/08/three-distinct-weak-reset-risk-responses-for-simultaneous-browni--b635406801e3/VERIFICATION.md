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

## Reproduction
Run `python check.py` with Python 3 standard library from the same directory as the file. The checker evaluates conservative bounds for the full integrals, including small-argument and infinite tails, writes `enclosures.json` and asserts all six sign triples. Analytic renewal and derivative steps are established in RESULT.md, not delegated to the code.

## Boundaries of verification
The computation is deterministic and finite but its interval enclosure is justified by the monotonic integrand and explicit remainder bounds; the program does not assert numerical sampling proves a continuum theorem. No claim is made for all populations, for global optimization, or for independent audit.
