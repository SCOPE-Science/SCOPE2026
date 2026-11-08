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

Run `python3 checker.py` in the extracted package directory; Python 3 standard library is the sole dependency. The checker reconstructs 216 ordered cubic triples and 37 distinct sum-frequencies; verifies the total square-multiplicity 2040 and hence the moment 85/9; builds both exact rational second-variation matrices; compares all entries to the displayed values; calculates exact rational eigenspace nullities for the four real and three imaginary bands; verifies the three phase-and-translation zero directions and the least-stable normal mode; and performs separate finite perturbation consistency checks.

Observed standalone execution:

```
HEXAGONAL_L6_LOCAL_PASS triples=216 sums=37 numerator=2040 real_bands=4 phase_bands=3 gap=15
```

The exact integer/rational reconstruction supports the Hessian calculation. The infinitely many nearby complex coefficients and the strict local assertion are covered by the explicit polynomial Taylor expansion and compact symmetry-orbit argument in RESULT.md, **not** by finite perturbation tests. Global sixth-moment maximality is unproved and not claimed. No external audit or certification has been performed.
