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

The exact theorem follows from face incidence, spherical-lune probabilities, and a constrained global optimization. The standalone `verify.py` checks four unrelated positive axis triples, 1,600 directly computed planar projection convex hulls, 1,604 central slice edge-crossing counts (contextual only), and 800,000 uniform view directions against the closed-form law. Its independent solid-angle expression agrees with the dihedral-angle expression to floating-point tolerance in four cases. The unique minimizer is proved analytically; the additional 5,000 random shape tests are supplementary.

Reproduction: run `python verify.py` with Python 3, NumPy and SciPy. The script uses a fixed random seed; no external datasets or private files are required. An actual run returned:

```
VERIFY_OK shapes=4 directions=800000 projection_hulls=1600 central_sections=1604 independent_cone_formula=4 sharpness_trials=5000
```

No formal proof assistant, exhaustive infinite-angle enumeration, independent human audit, or experimental validation has been performed. Numerical accuracy does not establish mathematical priority.
