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

# Verification evidence

Run `python3 verify.py` using Python 3 standard library only. The actual execution printed:

```
PASS: exact integer GCD checks=870; modular window congruences=5412; matrix shifts=18; total=6300
```

The checker evaluates the integer recurrence for even exponents \(2,4,6,8,10,12\) and lengths \(1\) through \(145\), then computes the gcd of the first \(d+1\) windows. These initial windows determine the infinite gcd for fixed \(d\) because the sequence of \(d\)-th powers satisfies a monic integer recurrence of order \(d+1\). Additional modular checks cover exponents \(2,4,6,8,10,12,14,20,30,50,100\), complete lengths \(3\cdot5^r\) for \(0\le r\le5\), and arbitrary three-divisible lengths up to \(200\). Matrix congruences are checked through \(5^6\).

The source proof, not the finite checks, supplies the universal quantifiers. No complete global integer gcd or non-five prime behavior is claimed. Neither independent mathematical examination nor external certification has been performed.
