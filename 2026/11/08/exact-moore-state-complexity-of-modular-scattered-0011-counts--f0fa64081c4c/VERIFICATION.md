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

# Reproduction

Run `python3 checker.py` with Python 3.9 or later (standard library only). The script independently counts scattered \(0011\) index quadruples for every binary word of length at most \(16\), checks the four-coordinate recurrence at moduli \(2,3,4,5,7,11\), checks reachable state and suffix-signature counts for every modulus \(2\) through \(30\), tests the explicit universal reaching words through modulus \(11\), and independently minimizes reachable Moore machines through modulus \(11\).

The extracted package-path replay printed:

```
direct-subsequence-comparisons: 786426
all-modulus-reachability-and-distinguishability-tests: 29
explicit-witness-comparisons: 8710
independent-Moore-partition-minimizations: 10
PASS
```

The all-modulus claim relies on the symbolic proof, especially the phase count, explicit orbit generators and the injectivity of the four-output signature; finite verification is not an infinite certificate. Historical priority and independent mathematical validation are not certified by these checks.
