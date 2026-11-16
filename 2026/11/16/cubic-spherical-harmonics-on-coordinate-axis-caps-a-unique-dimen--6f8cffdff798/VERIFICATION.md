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

# Verification of the cubic coordinate-cap spectrum

Run `python check_cubic_coordinate_caps.py` with Python 3, SymPy, and mpmath. Its successful observed output was:

```
CUBIC_COORDINATE_CAPS_EXACT_PASS symbolic=all_d independent_cases=25
```

The symbolic part checks the representation dimensions, sectorwise trace, independent representative-harmonic conditional integrands, exact Beta-derivative primitives, the dimension-three crossing root, and the thin-cap constant. The numerical part independently integrates representative squared cubic harmonics using conditional Dirichlet moments and high-precision Beta quadrature at five cutoffs in each of five dimensions. This is reproducibility evidence for a complete analytical proof, not a claim that 25 samples certify all dimensions.

The result is conditional on pure degree three, dimension at least three, and \(1/2\le t<1\). The mathematical priority comparison is limited to the identified accessible literature; no independent external audit has been performed.
