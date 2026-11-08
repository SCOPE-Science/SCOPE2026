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

# Verification record

The proof of the infinite theorem is contained in `RESULT.md`. Its critical deductions are the persistent obstruction for three whites on a shore, two exhaustive constructive sequences for the two-by-two case, monotonicity, the exact profile count, and the real-root discriminant inequalities. The n=3 boundary is included and n=2 is excluded explicitly.

To independently reproduce finite checks, execute `python verify_crown.py` in the same folder. The code uses no external dependencies. It directly generates graph neighborhoods and repeatedly applies legal individual forces; its predicate does not use the claimed characterization. All subsets of \(2n\) vertices for \(3\le n\le9\) were tested, with inclusion-minimality verified by deleting each selected blue vertex. The observed output was:

```
VERIFY_OK orders=3..9 subsets=349504 minimal_sets=2772 direct_sequential_forces=PASS white_profile=PASS zero_forcing_polynomials=PASS inclusion_minimality=PASS symbolic_counts=3..100 PASS
```

The symbolic coefficient test covers integer orders \(3\le n\le100\) but is a finite arithmetic consistency check. Neither finite graph enumeration nor sampled polynomial checks establish the unrestricted theorem. Publication priority is provisional; no independent mathematical audit or external certification has been performed.
