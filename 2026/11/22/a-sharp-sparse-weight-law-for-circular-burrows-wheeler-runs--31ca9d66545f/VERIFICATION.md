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

# Reproducible checks

With Python 3 standard library, run:

```
python3 check_exhaustive.py
python3 check_gaps.py
```

The first program independently builds every cyclic rotation and its last column for 53,979 indexed words at designated small length/weight ranges, directly checking the universal bound, gap sufficient condition, and exactly counted certified family. The second builds full cyclic rotations from shuffled gap tuples, checks 926 separated-gap instances in independent index form, and checks 54 restricted-partition calculations. Exact terminal outputs are recorded in `checks.txt` and reproducible from this package.

The all-length separation argument is proved in `RESULT.md`. The finite checks neither certify all words nor imply the asymptotic result by extrapolation; the latter follows solely from the proved uniform weak-composition bound. No external independent audit or formal proof was performed.
