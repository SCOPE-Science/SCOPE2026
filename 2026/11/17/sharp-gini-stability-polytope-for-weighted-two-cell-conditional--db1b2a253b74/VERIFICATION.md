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

Run `python3 check.py` with Python 3 and no third-party dependencies. The code uses exact `fractions.Fraction` arithmetic, exhaustive enumeration of all nonempty proper binary cuts in the stated finite tests, and deterministic rational probes; the unrestricted proof is in `RESULT.md`.

Actual output of the embedded checker before packaging:

```text
EXACT_ALL_TWO_CLASS_CUTS_AND_RATIONAL_INPUTS_PASSED 75
EXACT_NONBISTOCHASTIC_CONTRACTION_AND_SHARP_FOUR_POINT_THRESHOLD_PASSED
UNIFORM_STABILITY_AND_PARTITION_ENVELOPE_BOUND_PASSED 1600
ALL_WEIGHTED_TWO_CELL_GINI_CHECKS_PASSED
EXACT_STABILITY_RADII_AND_NEARBY_SHARP_VIOLATIONS_PASSED 256
```

The script tests 75 strictly positive rational mass pairs up to five coordinates per class, every cut for each pair, and independent rational input inequalities; 1600 uniformly weighted size pairs; exact contrasting four-site witnesses; and 256 sharp-radius perturbation families. The finite program cannot establish the all-dimensional coarea reduction, the general weight-parametric stability polytope, or historical priority; those are addressed respectively by the proof and the stated literature limits. No independent scientific audit is reported.
