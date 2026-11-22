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

The nonzero graded source/target block is given explicitly in `RESULT.md`, with all boundary cases. The finite-field nondegenerate alternating-form count is derived as an orbit/stabilizer ratio; its all-dimensional application is proved algebraically, not inferred from computations.

Reproduce with Python 3 standard library:

```
python near_socle_checker.py
python exterior_cubic_checker.py
```

Expected terminal lines: `NEAR_SOCLE_CHECKS_OK` and `CHECKS_OK`, respectively. Recorded outputs are embedded alongside each checker. Exhaustive checks: every one of the 65,536 near-socle elements for \(n=5,q=2\), and 59,049 homogeneous cubics for \(n=5,q=3\). Other checks sample independently constructed multiplication matrices in dimensions five through seven, with seeded prime-field coefficients. No exhaustive experiment is claimed for unbounded dimensions or arbitrary field extensions.

Independent mathematical review and independent historical-priority verification have not been performed.
