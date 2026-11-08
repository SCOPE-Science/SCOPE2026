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

# Verification and reproducibility

In a Python 3.10+ working directory containing `checker.py`, run:

```sh
python3 checker.py
```

The expected exact output is:

```text
PASS 156832 direct suffix-orbit comparisons; 324 full S3 subgroup spectra; 6 subgroups
```

The checker constructs every length-\(n\) factor from a complete periodic phase set. For the one-marker regime it compares actual subgroup orbit partitions against the theorem's piecewise expression, for all periods from 2 to 30, all lengths from 1 through four periods, all fixed-prefix sizes and both letter orientations. It independently constructs each subgroup of the coordinate group \(S_3\), tests closure, and computes all factor orbits for run lengths from 2 through 19 in the two-long-runs regime. Counts are exact within these finite ranges.

The proof of the infinite statement is in `RESULT.md`. In particular the arbitrary-length argument rests on phase indexing by the first marked-letter position and the fact that coordinate-permutation equivalence on a suffix is exactly equality of its Parikh vector. Negative-case impossibility follows from complementation symmetry at length 3. The finite checks are safeguards against calculation and boundary mistakes, not exhaustive evidence for arbitrarily large parameters.

No independent external review or independent certification was conducted.
