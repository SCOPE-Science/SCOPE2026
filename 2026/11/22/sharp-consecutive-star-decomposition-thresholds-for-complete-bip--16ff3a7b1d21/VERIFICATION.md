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

# Verification

The source package contains `verify.py` and `certificates.json`; execute `python3 verify.py` from their shared directory. No third-party libraries are necessary. The checked certificate covers every exceptional pair \\(a\le b\\) from the explicit semigroup gaps for \\(k\in\{4,5\}\\) with \\(a+b\ge k^2-1\\). Each row mask specifies every edge direction, and all vertex outdegrees are tested for actual nonnegative decomposability into \\(k\\) and \\(k+1\\).

Successful execution:

```
SEMIGROUP_AND_EXCEPTION_COVERAGE_PASS
TWELVE_EXPLICIT_ORIENTATIONS_PASS
SHARP_OBSTRUCTIONS_PASS
VERIFY_OK
```

The unrestricted proof additionally uses elementary semigroup and orientation lemmas established in `RESULT.md`. The finite computations alone do not establish an infinite theorem; the proof reduces all infinite cases to the bounded certificate. No independent external audit is claimed.
