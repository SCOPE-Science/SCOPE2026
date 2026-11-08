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

# Verification notes

The exact-domain claim concerns \(d\ge2\), \(e\ge1\), algebraically closed fields of arbitrary characteristic for normalization/conductor/seminormality and characteristic \(p>0\) for Frobenius splitting. The written proof includes the interval-union argument, the conductor check over every weight residue, the seminormality witnesses, and Frobenius-root-closure/splitting arguments. These are infinite arguments.

Run `python3 check_weighted_curve.py` from the directory containing this document and the checker. It independently generates weighted monomials (not using the formula under test) and checks all degrees \(0\le a\le22\) for \(1\le d\le7\) and \(1\le e\le8\). It then tests conductor criteria and primes \(2,3,5,7,11\). Its observed output was:

```
WEIGHTED_CURVE_SEMIGROUP_MEMBERSHIP_OK 56
CONDUCTOR_AND_FROBENIUS_ROOT_TESTS_OK 280
INFINITE_THEOREM_REQUIRES_WRITTEN_SEMIGROUP_PROOF
```

These diagnostics do not inspect every integer parameter, and the field-characteristic statements require the proof rather than finite trials. The already-known nonnormality and Hilbert-series statements are appropriately attributed. No independent mathematical validation was performed.
