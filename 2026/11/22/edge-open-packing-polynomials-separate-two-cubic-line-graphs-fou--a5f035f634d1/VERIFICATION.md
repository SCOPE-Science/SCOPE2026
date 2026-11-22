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

# Reproducible finite verification

The exact independent-set recurrence follows from partitioning sets into those containing or excluding a selected vertex of the explicitly constructed conflict graph; see `RESULT.md`. Run the two embedded standard-library scripts:

```
python3 verify_recurrence.py
python3 verify_direct.py
```

The first computes complete integer independence-polynomial coefficients by an exhaustive recurrence and enumerates the four coordinate-permutation orbits. The second constructs the Petersen graph in an independent representation and explicitly tests all candidate subsets through size five. Their exact captured outputs are `recurrence_output.txt` and `direct_output.txt`.

The first finishes with `RECURRENCE_AND_ORBITS_OK`; the second finishes with `DIRECT_ENUMERATION_OK`. Every maximum count and every coefficient is checked exactly. In particular the second program tests all 142,506 five-subsets for each graph; absence of such subsets and hereditary closure rule out larger packings. There is no asserted extrapolation from a finite sample to an infinite family.

The analysis does not certify the novelty of the counts against every possible unpublished table. Independent audit status remains not performed.
