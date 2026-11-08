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

The complete proof establishes all positive integral run profiles and all alphabet sizes at least two. `verify.py` is a standalone Python 3 standard-library finite oracle test and can be run using `python3 verify.py`.

Actual output: `PASS 2684 independent finite pairs (all maximal factors and whole common language up to L+1)`.

The 2684 comparisons comprise 600 exhaustive ordered pairs of distinct two-run profiles with entries from 1 through 5; 1934 ordered pairs for q=3 with entries from 1 through 3 and q=4,5 with entries from 1 through 2; and 150 additional deterministic seeded comparisons with up to nine runs and run lengths up to eight. The program builds each infinite periodic word through enough repeated periods to enumerate every starting phase and every factor length up to the claimed maximal length plus one. It directly computes intersection, coverage by the proposed words, and the inclusion-maximal factors.

Finite enumeration is not a proof for arbitrary parameters. The result depends on the mathematical alignment and mismatch-endpoint arguments in `RESULT.md`; the checker is an independent finite consistency test. No separate independent scientific audit has been performed.
