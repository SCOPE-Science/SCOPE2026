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
# Verification

Run `python3 verify.py` using the Python standard library. It constructs the labelled ordinary powers of cycles, computes the zero forcing closure directly, and compares all minimum-cardinality subsets to the first-force representation for every valid parameter pair with \(3\le n\le13\) (\(36\) cases). It also checks the forcing property and representation multiplicities for represented candidates up to \(n=40\), and independently computes the full dihedral permutation orbits for 100 pairs through \(n=25\). The completed invocation returned:

```
ALL_MINIMUM_SETS_EXHAUSTIVE_OK 36
ALL_REPRESENTED_SETS_FORCE_OK through n=40
DIHEDRAL_ORBITS_EXACT_OK 100
VERIFY_OK
```

These are actual finite tests only. The unrestricted first-force equivalence, cyclic interval overlap lemma, separate small boundary cases, and dihedral orbit identification are proved in `RESULT.md`. The independent audit is not performed.
