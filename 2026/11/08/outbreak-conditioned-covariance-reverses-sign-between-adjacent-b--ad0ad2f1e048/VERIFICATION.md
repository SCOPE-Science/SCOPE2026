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

# Verification record

The enclosed `verify.py` can be executed independently under ordinary Python 3 with no nonstandard dependencies. It enumerates all thirty-two joint seed-and-edge outcomes at each of 144 rational parameter pairs; the resulting probabilities are compared with independently derived algebraic formulas. Additional exact rational parameter grids check the sign-polynomial derivative decomposition and monotonicity. The script prints 21,825 passed checks.

Analytical claims, including uniqueness over continuously varying real inputs, are proved in `RESULT.md` using exact factorizations and a strictly positive polynomial derivative. Finite sampling alone is not an infinite proof. No external mathematical validation or independent audit is claimed.
