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

# Reproducibility

Run `python3 verify.py` in the directory containing this document. The script uses Python's standard library only and recomputes all scattered subsequence counts by a direct, independent dynamic recurrence. It checks every integer triple \((a,b,m)\) in \([1,12]\times[1,12]\times[1,5]\) (720 parameter triples), every phase within each triple, every cross-family pair for first-coordinate collision and the stated second-coordinate gap, and a four-run counterexample through six positive powers.

The observed execution returned:

```
PASS: 9360 direct pattern-count checks; 30420 cross-phase comparisons; 6 four-run power cases
PASS: all (a,b,m) in [1,12]^2 x [1,5] have 720 tested parameter tuples
```

These are finite checks, not an exhaustive verification of all positive integer parameters. Universal correctness is supplied by the closed-form phase enumeration and algebra in `RESULT.md`. Independent external scientific validation has not occurred.
