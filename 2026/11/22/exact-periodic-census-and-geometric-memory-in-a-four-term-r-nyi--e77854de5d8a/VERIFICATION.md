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

# Verification and reproducibility

Run `python3 check.py` from this package. Python 3's standard `fractions.Fraction` is the only needed exact-arithmetic facility.

Observed output from the delivered checker:

```
PASS: 1000 rational integration cells; 6 exact covariance integrations; 7 all-lag arithmetic identities; 2095 rational periodic lifts
A=1111; mean=2; variance=2321/6000; lag-1 covariance=211/606000
```

The script independently computes the first two moments by exact integration on the 1000 genuine affine branches, checks the Fourier-gcd formula by exact partition integration for six pairs, verifies seven lag instances of the all-lag arithmetic identity, and tests 2095 rational lifted periodic points (including complete small-gain period censuses). The domain, branch endpoint conventions, measure correspondence, infinite periodic census, all-lag covariance, uniqueness of the absolutely continuous invariant measure, exactness, and measure entropy are established analytically in `RESULT.md`; finite tests are not used to certify unbounded quantifiers. Scientific publication priority has not been independently audited.
