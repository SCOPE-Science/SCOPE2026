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

The complete proof is in `RESULT.md`. The script `checks/verify.py` uses only Python 3's standard library and independently enumerates every trichotomy (new point less than, incomparable to, greater than each parameter) for all nondecreasing chain partitions through total size eight. It tests the necessary and sufficient transitivity conditions directly against the underlying strict-order relation. Its count agrees with the closed form for every profile. It checks the first global unimodality and log-concavity failures and verifies the two-chain analytic characterization over 3240 profiles with sizes at most 80.

Run from the package root:

```
python3 checks/verify.py
```

Expected final marker is `VERIFY_OK`. The proof of the unrestricted two-chain theorem and the infinite witness families does not rely on finite testing. The finite minimum thresholds are exhaustive within their stated finite ranges because every integer partition is enumerated. The arity is one, types are nonalgebraic, named parameters are fixed pointwise and the class is precisely a disjoint union of chains in the countable homogeneous poset. Independent review remains unperformed.
