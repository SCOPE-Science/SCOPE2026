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

The primary argument is an exact symbolic proof: it uses the two-step product equation \(NN'=p^2q^2\), unique factorization, valuation differences, and an exhaustive enumeration of the nine exponent pairs \((u,v)\in\{0,1,2\}^2\). Its eight exclusions are algebraic and hold for every pair of distinct primes. The conclusion is that \(D_{\{p,q\}}^2(n)=n>0\) forces \(D_{\{p,q\}}(n)=n\).

`verify.py` separately evaluates the map for every positive integer through \(100000\) and all \(45\) unordered pairs among the first ten primes. It checks the finite nine-case condition for these pairs and independently confirms the absence of primitive two-cycles in that finite region. The output captured from the actual execution is in `verification_output.txt`. This finite check is not asserted to certify all primes or all integers.

Scientific scope: nothing is proved about potential cycles of lengths greater than two or about prime sets of cardinality at least three. The known fixed-point classification is not claimed as novel.
