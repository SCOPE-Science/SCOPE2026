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

The analytic argument reduces every modulus to its squarefree radical and exhausts the possible local root fibers of the first six squares. It proves the complete formula at all prime sizes and exponents; finite enumeration is not used in place of this proof.

Run `python3 verify_quadratic_jacobsthal.py` from the directory containing that script. Standard-library-only execution completed with the following results:

```
PASS: all integers 2..1600 with at most two distinct prime factors: 1059
PASS: distinct prime pairs p<q<79 (direct gcd vs independent CRT): 210
Checks include k=1,2,3,4,5,6; k>6 vanishes by monotonicity.
This is finite evidence only; uniform bounds require the written proof.
```

The script is included in full and separately compares direct gcd enumeration with CRT-local cover enumeration for the indicated prime pairs. No external audit has been conducted. The theorem does not cover radicals with three or more prime divisors.
