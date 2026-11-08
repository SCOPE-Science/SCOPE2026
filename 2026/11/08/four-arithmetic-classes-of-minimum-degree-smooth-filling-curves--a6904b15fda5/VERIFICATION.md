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

# Reproducibility

Execute both programs in the same directory using Python 3 and SymPy:

```text
python verify_filling_43_orbits.py
python verify_filling_43_independent.py
```

Successful completion produces `BIDEGREE43_FILLING_PASS 2048 99 66 4` and `BIDEGREE43_INDEPENDENT_PASS 2048 66 4`, respectively. Both programs were executed on the submitted source files and completed with these markers. The first enumerates 99 geometric-orbit representatives, checking the four Jacobian ideals on each. The second checks the Jacobian ideals of all 2047 nonzero filling forms, using a different Gröbner ordering, and calculates the four extension-field point-count sequences with alternative binary irreducible polynomials. In both, all polynomial arithmetic is exact over finite fields.

The six-degree point-count input, full twelve-degree Weil polynomials, and coefficient-mask convention are recorded in `representatives.json`. The identity between the nine rational evaluation constraints and the complete filling linear system is checked directly. The reciprocal functional equation is applied only after the curve's smoothness and genus six are established.

These are computational and self-review, **not** independent mathematical certification. The scripts do not establish results for nonsplit quadrics, for other finite fields or bidegrees, or for abstract automorphism groups.
