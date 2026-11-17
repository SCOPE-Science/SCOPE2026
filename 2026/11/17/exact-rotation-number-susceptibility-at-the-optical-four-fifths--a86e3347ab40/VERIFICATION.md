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

# Verification details

The exact checker `verify.py`, using Python 3 and SymPy, reconstructs the five branch itineraries at their interior midpoints, symbolically composes them, checks unit spatial slopes and zero unperturbed fifth-return displacements, differentiates each in the parameter, and verifies all five equal crossing times and the final closed form. The checked output is reproduced below.

```text
VERIFY_OK exact_itineraries=5 exact_unit_slopes=5 algebraic_drifts=5 equal_crossing_times=5 derivative= -7*sqrt(5)/100 - 3/20 decimal= -0.3065247584249853
```

A numerical orbit count at small nonzero parameter perturbations independently supported convergence to the indicated slope but is not used as proof. The dynamical derivative uses a mathematical crossing-time limit; finite symbolic algebra alone does not certify its applicability. Source and publication comparisons are same-model reviews. Independent validation has not been performed.
