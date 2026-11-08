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

# Reproducibility and limits

Run `python3 verify.py` with the standard Python library. Recorded output from the checked program:

```text
s= 2.1 r= 3.946618531261939 local maxima= 1 noncentral stationary pairs= 0
s= 2.13 r= 4.01066477608318 local maxima= 3 noncentral stationary pairs= 2
s= 2.3 r= 4.371231517720798 local maxima= 2 noncentral stationary pairs= 1
s= 4.0 r= 7.872983346207417 local maxima= 3 noncentral stationary pairs= 2
s1= 2.168248175552983 s2= 2.833689029759382
r0= 3.9893314312876678
r1= 4.092124510141264 r2= 5.485064807988238
All checks passed
```

The program tests the double-root onset and related algebraic identities using exact rationals; the finite comparisons test 42 direct/reduced values and an independent analytic derivative on dense positive-frequency grids. Crucially, the proof, not the sampled root counts, establishes the parameter ranges universally. It does not establish independently validated priority, experimentally resolvable peaks, or behavior outside the stated strength interval.
