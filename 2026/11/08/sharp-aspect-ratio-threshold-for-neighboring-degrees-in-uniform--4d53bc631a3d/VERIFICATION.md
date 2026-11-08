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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or later (standard library only). The program evaluates two independently implemented rational expressions for the covariance for every parameter pair with \(2\le m,n\le12\); checks the exact sign boundary; exhaustively enumerates all spanning trees of \(K_2\square K_2\), \(K_2\square K_3\), \(K_3\square K_2\), \(K_2\square K_4\), and \(K_3\square K_3\); and tests the two symbolic threshold substitutions at additional finite integer arguments. Recorded output ends `VERIFY_OK 313 exact assertions`.

The exhaustive enumeration gives covariances \(0\), \(-19/225\), \(8/225\), \(-29/288\), and \(-7/162\) in that order. The infinite-parameter formula and sign classification are proved by spectral decomposition, the finite-graph transfer-current identity and polynomial sign analysis in RESULT.md, not by finite numerical experiments. Independent external validation was not performed.
