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

The exact `verify.py` script embedded with this result ran successfully using Python 3 and standard-library integer arithmetic:

```
VERIFY_OK valuation_pairs= 78683 carry_checks= 2779 direct_gcd_cases= 80
```

The verifier enumerates parameter triples with \(p<40\), \(p^a\le1100\), \(1\le m<p\), and \(3\le mp^a\le1100\); it checks all \(2\le q\le mp^a\) by exact Legendre factorial valuations. It independently checks selected Kummer carry counts and, for \(mp^a\le135\), directly computes the gcd from exact binomial integers. All 78,683 multiplier cases satisfy the lower bound and every tested minimum equals the predicted exponent. This is a finite reproducibility check only. The unrestricted result follows from the proof in `RESULT.md`, including the cited published local criterion.
