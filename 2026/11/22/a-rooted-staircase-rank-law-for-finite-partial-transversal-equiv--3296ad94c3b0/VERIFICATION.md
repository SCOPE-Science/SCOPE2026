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

# Reproduction and boundaries

Run `python3 checker.py` in a directory containing the supplied standalone Python 3 script. It requires only the Python standard library. The final successful line begins `ALL_CHECKS_OK` and reports 1,215 finite host structures and 2,325,866 marked-position/threshold comparisons. Two independent finite-game implementations, an exact sorted-capacity comparison, 179 randomized profile comparisons (from 300 generated candidates) and minimum-host witness checks through rank six are included. The output is an executable finite check, not an independent audit or an all-size proof.

The all-size result is supported by the relative one-point-extension induction, the empty-position peeling recurrence, the sorted-capacity exchange and the tight size count in `RESULT.md`. The proof applies to arbitrary finite partially-rooted equivalence structures, including the empty structure. Infinite hosts and historical priority are not certified by this script.
