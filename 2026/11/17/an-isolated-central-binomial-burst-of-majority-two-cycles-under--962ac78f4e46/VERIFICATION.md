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

# Reproduction and verification

From a directory containing the included programs, use Python 3 (standard library only):

```
python3 exact_certificate.py
python3 two_restorations_certificate.py
python3 crown_check.py
python3 direct_verification.py
```

The first three programs perform integer-only Fourier–Motzkin elimination on explicitly enumerated threshold regimes and supports. A contradiction over the reals excludes all integer configurations in that regime. The fourth program independently builds each graph's vertex-majority update directly and enumerates every binary state for 22 small graphs (1,186,048 states). The four captured outputs accompany the programs and were reproduced from the actual included source files.

The counts classified by symbolic elimination are for all odd orders, not inferred from the finite graph checks. The result does not cover attraction basins or even shore orders. Independent validation has not been performed.
