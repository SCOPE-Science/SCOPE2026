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
# Reproducibility notes

The included `verify_lie.py` needs only the Python 3 standard library and can be run with `python3 verify_lie.py`. It enumerates every factor of a finite prefix that captures the whole factor language through the specified length bound, forms genuine rotation orbits, and checks the predicted orbit representatives. Its deterministic seed is included in the source.

The verified output is:

```
PASS exhaustive_cases= 5120 random_and_family_cases= 3668 total= 8788
```

The exhaustive regime covers all \(4^4\) zero-gap multiplicity profiles in \(\{0,1,2,3\}^4\), lengths \(1\) through \(20\); the other tests include noncontiguous gap supports, randomly chosen longer plateaus, strictly increasing gaps, and \(m_a=a\), through factor length \(36\).

**Completeness of each finite comparison:** any missing future gap is longer than the tested factor length. A factor with two or more markers has a complete zero gap shorter than that length, so it appears before the large-gap tail. Single-marker factors and all-zero factors appear around a tail marker with both adjacent zero gaps longer than the tested length. Hence no additional distinct length-bounded factor appears later.

**Proof boundary:** finite enumeration does not certify the theorem for all nondecreasing unbounded gap sequences. That claim is established by the written circular-gap monotonicity argument in RESULT.md. No independent scientific audit or external certification is asserted.
