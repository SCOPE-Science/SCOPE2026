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

The accompanying `rotation_enumerator.py` enumerates every length-six tuple over each of the normalized alphabets of sizes one through six, selects primitive lexicographically minimal cyclic representatives, constructs the BWT by sorting all cyclic rotations, and counts the input cyclic transitions.

The separate `cycle_enumerator.py` enumerates last-column candidates directly, tests the six-cycle condition on their stable last-to-first permutations, and computes the same input-run invariant by Hamming distance against the sorted first column. `verify.py` compares both complete sets, the eight histogram cells, the ten multiplicity-partition cells, the exact `census.tsv` table of 384 records, and the alphabet-lifting counts for alphabet sizes one through four.

Run:

```
python3 verify.py
```

The expected final line is `BWT_LENGTH_SIX_CENSUS_OK 384 8_HISTOGRAM_CELLS 10_PARTITION_CELLS`.

All computations use exact integer arithmetic and the Python standard library. The infinite-alphabet-size conclusion follows from order-preserving relabeling and the binomial-lifting argument, not an extrapolation of the finite checks. No independent mathematical audit has been performed.
