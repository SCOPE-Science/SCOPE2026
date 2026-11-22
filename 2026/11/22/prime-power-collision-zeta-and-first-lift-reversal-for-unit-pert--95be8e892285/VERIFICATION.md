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

# Reproduction and limits
The standalone Python 3 program `artifacts/verify.py` needs only the standard library and directly evaluates the original polynomial on each residue class, building target fiber counts without assuming the theorem. Execute `python3 artifacts/verify.py` from the enclosing directory.

Observed output:

```
PASS histogram_cases=105 input_residues=57885 direct_pair_checks=114015 finite_field_geometry_cases=35 phase_comparisons=24
```

The 105 cases cover primes \(3,5,7,11,13,17\), admissible coefficients among \(1,2,3,4,1+p,2+2p\), and exponents \(1,2,3\). For small moduli the script independently enumerates ordered equal-value pairs; it counts the crossing geometry directly modulo every tested prime and tests the exact difference formula for both coefficient classes through exponent four. The infinite result is established in the accompanying written proof by exact curve decomposition and Hensel lifting, not by the finite program. No external or independent mathematical audit has been performed.
