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

The proof is fully analytic: the contact-weight identity and union-of-balls geometry establish the upper envelope in every dimension, while a four-point planar configuration gives exact equality. The one-dimensional case uses inclusion–exclusion for overlapping bounding intervals.

Reproduce the supplementary finite tests with `python3 verify_circumradius_submodularity.py` from the directory containing this file. The standard-library verifier enumerates support subsets for minimum enclosing balls rather than using the upper-bound proof as its implementation. A verified execution reported:

```
PASS: numerical equality witness and published-example comparison;
PASS: 1752 random finite-set comparisons in dimensions 2, 3, 4.
Scope: numerical tests support but cannot certify the universal inequality.
```

Floating-point tolerances apply only to those tests. They are not an exhaustive finite certificate and do not support any independent audit status. The exact theorem, equality witness, and all boundary cases are proved in RESULT.md.
