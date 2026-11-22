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

The standalone `verify.py` exhausts every subset of \(\{1,\ldots,r-1\}\) for \(1\le r\le12\), for three different admissible multiplicities, totalling 12,285 numerical semigroups. It checks the defining pseudo-Frobenius predicate, the exact pseudo-Frobenius decomposition, the residue-product counts and the rational mean. The required output is `VERIFY_OK 12285 semigroups; r=1..12, three m values`.

The infinite-dimensional expectation estimate follows from the disjoint-edge matching bound in the proof, and the Gaussian limit follows from the binomial central limit theorem, the bounded first moment of the correction and Slutsky's theorem. Finite testing does not verify the asymptotic argument, and independent mathematical audit is not performed.
