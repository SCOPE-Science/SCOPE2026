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

The proof in `RESULT.md` establishes every integer dimension \(M\ge2\). Run the embedded `check.py` with Python 3 standard library only:

```sh
python check.py
```

Executed successfully with the following exact markers:

```
AFFINE_TRANSFER_DETERMINANTS_AND_RESOLVENT_OK dimensions=2..10
FIRST_NEGATIVE_CORRELATION_AT_DIMENSION_OK dimensions=2..10
MARTINGALE_PREIMAGES_AND_CONDITIONAL_VARIANCE_OK dimensions=2..10
```

For every tested \(M\), `check.py` computes a rational transfer matrix, compares the determinant to the proposed closed form at \(M+1\) distinct rational values (enough to prove equality of degree-at-most-\(M\) polynomials for each tested dimension), checks lag \(0\) through \(M\), checks the all-ones row of the \(z=1\) resolvent, and verifies exact branch inversion and conditional variance at rational interior points. A separate direct Monte Carlo iteration of the original map for dimensions 2, 3, and 5 with 400,000 uniform points per dimension agreed with the analytic covariance values at lags through the dimension to sampling error (not a proof). The central limit theorem rests on the analytical martingale-coboundary argument, ergodicity of the known map, and standard martingale limit theory. It is not independently externally audited, and the finite tests do not establish unbounded-dimension identities.
