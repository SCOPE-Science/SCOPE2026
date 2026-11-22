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

## Reproducible checks

Run `python3 checker.py` with a standard Python 3 interpreter. This script enumerates all 120 local five-point patterns, all 252 interleavings of two five-point coordinate sets, and independently implements the finite three-level extension-game criterion by direct insertion-cell occupancy. The observed counts are 16 and 180, whose fourth-power product is 68,797,071,360,000.

It checks 250 constructive minimum hosts, 5,250 single-point deletions and 2,100 randomized subthreshold permutations. The checker prints `CHECK_OK` twice on success. Finite tests are corroborating evidence only; the lower bound and total census follow from the proof in `RESULT.md`.

## Scope limits

The checker does not exhaustively enumerate all permutations of 21 points, nor certify historical novelty. Independent mathematical and historical reviews have not been performed.
