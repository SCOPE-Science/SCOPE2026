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

# Verification scope and reproduction

Run `python3 verify.py` with Python 3, SymPy, NumPy, and SciPy. An actual execution of the included source printed:

```
PASS 123 algebraic / finite-dimensional consistency checks; unique-root example 1.132906609052
```

The code builds exact stationary moment expressions, a five-dimensional polynomial-generator resolvent, and a separate five-stage positive convolution semigroup. It verifies the rational identity and zero derivative with respect to thermal diffusivity symbolically and compares both semigroups over multiple rates, times, thermal strengths and repeated relaxation eigenvalues. The exact kernel ratio monotonicity and global uniqueness are analytical arguments documented in RESULT.md; sample checks of positivity and monotonicity do not certify those infinite assertions. No external independent scientific audit was performed. The literature-priority evaluation is provisional pending wider independent comparison.
