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

# Finite cycle-moment certificate

Run `python3 verify.py`. Two independent integer-arithmetic methods enumerate, respectively, the exact multivariate generating-product coefficients and the full descending-part integer partitions for each fixed cardinality \(1\le M\le14\). The resulting signature dictionaries match in every entry. The first repeat is unique at \(M=14\), with the two cycle partitions \((7,4,3)\) and \((6,6,1,1)\) and the pair of power sums \((74,434)\).

The checker also confirms the raw mean \(37/7\) and variance \(150/49\) with rational arithmetic and tests the explicit family through \(1000\) points. The infinite statement rests on the algebraic singleton-extension proof in `RESULT.md`; finite tests are not substituted for that proof. No independent audit is asserted.
