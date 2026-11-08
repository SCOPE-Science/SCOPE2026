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

# Executable checks

Execute `python3 verify_forts.py` (Python standard library only). The script builds the triangular graph from pair intersections, tests every nonempty vertex subset for fort status, tests **all proper nonempty subsets** for minimality by a bottom-up subset dynamic program, compares every minimal fort against the two root-graph structural types, and compares all cardinality coefficients to a separate rooted-component recurrence plus an undirected-cycle count.

Recorded execution:

```
n=3 vertices=3 checked_nonempty=7 forts=4 minimal=3 coefficients={2: 3}
n=4 vertices=6 checked_nonempty=63 forts=45 minimal=11 coefficients={2: 3, 3: 8}
n=5 vertices=10 checked_nonempty=1023 forts=828 minimal=60 coefficients={3: 40, 4: 20}
n=6 vertices=15 checked_nonempty=32767 forts=29137 minimal=308 coefficients={3: 35, 4: 195, 5: 78}
n=7 vertices=21 checked_nonempty=2097151 forts=1977458 minimal=1659 coefficients={3: 35, 4: 420, 5: 777, 6: 427}
VERIFY_OK n=3..7 nonempty_subsets=2131011 forts=2007472 minimal_forts=2041 all_subsets_and_coefficients=PASS
```

# Mathematical limits

The finite test does not establish the formula for unbounded order; the complete proof in `RESULT.md` does. No external theorem prover or separate expert certification was used. Publication priority and correctness have not been independently audited.
