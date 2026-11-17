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

The supplied standalone `verify.py` requires only Python 3 standard-library modules. Run `python3 verify.py` in the directory containing this file. The test independently computes Euclidean exterior-product lengths from distinct nonzero generator tuples and from compressed multinomial row-pattern counts. It compares all \(2\le d\le6\) with \(k\le\min(d,3)\), plus \((d,k)=(4,4)\). It directly verifies the key binomial moment identities for ten fixed orders and numerically checks the approach to the second-order coefficient for two-column Gram determinants.

The expected terminal marker is `BOOLEAN_INTRINSIC_PASS brute_vs_compressed=15 moments=10`. These bounded computations support finite identities and normalization, but do not independently certify the asymptotic proof, uniqueness in the literature, or the stated variance for every order. Analytical proof and scope appear in `RESULT.md`.
