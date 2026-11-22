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

# Verification of the cyclic distance-algebra theorem

The accompanying standalone `verify_distance_hh1.py` executes in standard Python 3.9+ with no external dependencies:

```
python verify_distance_hh1.py
```

The actual execution completed successfully and printed:

```
CYCLE_DISTANCE_HH1_DIHEDRAL_CHECKS_OK
finite cyclic orders: 3..16; fields: F2,F3,F5,F7
random geodesic cocycles and multiplication triples checked: 224
rank checks, rotational/reflection equivariance and mod-2 nonsplitting passed
```

The code implements modular Gaussian elimination for the antipodal geodesic relations and the inner-gradient space. It checks every multiplication triple for random derivations over the listed finite fields, and separately confirms dihedral symmetry, antipodal edge-pair values, the characteristic-two obstruction and odd-characteristic explicit sections. The random seed is fixed for reproducibility. These checks are finite, and they do not certify the all-length and arbitrary-field theorem; the exact symbolic proof is in `RESULT.md`.

No independent audit or external proof verification has been performed.
