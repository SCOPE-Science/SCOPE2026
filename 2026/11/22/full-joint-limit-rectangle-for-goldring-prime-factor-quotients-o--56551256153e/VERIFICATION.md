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

The dependency-free file `verify_goldring_joint.py` was run directly and passed, returning

```
GOLDRING_JOINT_PARAM_OK rational_centres=4 local_checks=350 complexity_rows=150 real_targets=50 sample_prime_patterns>=4
```

The script checks the actual formulas \(p=mx+my-z\), \(q=mx-my+z\), \(r=-mx+my+z\), the two quotient identities for prime instances, exact rational center computations including \((3/4,5/32)\), local nonzero residue solutions at 14 primes for 25 multipliers, the full three-class six-form complexity certificate in 150 distinguished-row checks, and 50 two-regime real target inversions. Each case checks positivity. Its finite output does not establish an infinite density theorem.

The infinitude and order of the count are established instead by the unconditional complexity-two Green–Tao theorem, used with the Yang–Zhao six-form lemma. A fixed positive-volume box and hyperplane exclusion are essential: a prime equality at the exact real center is not an obstruction. The proof separately checks the transition at \(\alpha=1/2\), the endpoint \(\alpha=1\), and axes by neighborhood closure.

No formal proof assistant or independent external audit is claimed. Full 2012 Chen–Shi–Wu article access was unavailable; the scientific-priority conclusion is qualified accordingly.
