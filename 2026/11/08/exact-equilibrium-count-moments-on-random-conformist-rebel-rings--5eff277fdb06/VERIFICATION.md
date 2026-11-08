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

# Reproducibility and verification

Execute `python verify_cycle_equilibria.py` with standard Python. This command enumerates every random type word and every binary action profile for ring sizes \(3\) through \(10\). It verifies best-response payoff inequalities directly, then compares their exact integer moment sums against the transfer-matrix moments using `fractions.Fraction`. It separately verifies a radical-free recurrence that follows from the displayed characteristic polynomials.

The exact run returns:

```
n=3 mean=13/4 second=25/2 empty_types=0/8
n=4 mean=25/4 second=81/2 empty_types=0/16
n=5 mean=121/16 second=501/8 empty_types=0/32
n=6 mean=169/16 second=1021/8 empty_types=2/64
n=7 mean=1093/64 second=10305/32 empty_types=0/128
n=8 mean=1681/64 second=24353/32 empty_types=0/256
n=9 mean=9841/256 second=213901/128 empty_types=0/512
n=10 mean=14641/256 second=482701/128 empty_types=2/1024
VERIFIED: 2040 type configurations, full action-profile checks, first and second moments.
```

The finite enumeration corroborates the analytic argument but does not prove it for arbitrarily large rings. That proof rests on the two parity-projector identities and characteristic polynomials explicitly supplied in `RESULT.md`. Source-priority comparisons are not independently audited; some relevant full text was not accessible.
