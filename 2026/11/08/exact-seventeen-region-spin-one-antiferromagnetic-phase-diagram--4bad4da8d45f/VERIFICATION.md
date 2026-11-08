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

# Reproduction and finite certificate checks

Run `python verify.py` with Python 3.9+ and `certificates/phase_polytope.json` present at the relative path supplied in this package. The program uses only Python's standard library. It performs two complete independent enumerations of the 531441 spin configurations (incremental vertex recursion and four-triangle block factorization), checks equality of their full microcanonical histograms, and verifies the ninety-one sector minima. It then verifies seventy-four exact rational convex domination certificates and seventeen exact strict phase-exposure witnesses. The calculations use integer counts and `fractions.Fraction`; no approximate convex-hull algorithm is part of the verifier.

The expected output includes:

```
PASS | vertices=12 edges=18 microstates=531441 sectors=91
PASS | independent complete microcanonical histograms equal
PASS | exactly 17 generically exposed ground-state sectors
PASS | 74 exact rational domination and 17 strict exposure certificates
PASS | (h/J,D/J)=(1,1): energy/J=0, degeneracy=1577
DOS SHA256: 35dea54d5dddbc058df29197a4e4b33c552866fb96af0c481299873533db577d
```

`certificates/sector_minima.csv` is the separately readable complete sector table. The rational convex certificates establish the full affine energy envelope, not merely its behavior at a finite set of real-field sample points. This is an exact finite-state theorem; source originality is reviewed on examined evidence, without independent scientific validation or guaranteed historical priority.
