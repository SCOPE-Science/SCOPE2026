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

# Finite verification and proof boundaries

Run `python3 verify.py` with standard Python 3; no dependencies beyond the standard library are used. The verifier enumerates all row orders on even \(n=2,4,6,8\), exactly inverts the matching binomial moments with rational arithmetic, and compares each numerical projection-product norm with the exact zero-factor criterion. It also enumerates all row orders on odd \(n=3,5,7\), confirming the minimum norm and exactly \(2n\) minimizers. Rational binomial moments are checked independently. Its observed output ends in `PASS 87320 finite checks`.

The proof for arbitrary \(n\) is in RESULT.md: rank-one projection product identity, orthogonal-pair graph, modular Hamilton paths, inclusion–exclusion, and a summable factorial-moment asymptotic expansion. Computations cover finitely many dimensions and do not certify the full theorem without that proof. No finite-precision or perturbed-row termination is asserted.
