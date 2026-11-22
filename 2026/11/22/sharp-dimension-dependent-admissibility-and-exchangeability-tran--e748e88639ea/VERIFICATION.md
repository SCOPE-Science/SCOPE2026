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

# Reproduction and limits

The result uses the following exact symbolic identity:
\[
\partial_1\cdots\partial_n C_{n,\alpha}
=(1+\alpha)^{n-1}\frac{1+\alpha\prod_{i=1}^{n}u_i(2+\alpha u_i)}{\prod_{i=1}^n(1+\alpha u_i)^2}.
\]
The boundary proof is independent of finite numerical testing: for \(-1<\alpha<0\), every \(u_i(2+\alpha u_i)\) is increasing, and the all-one corner determines the positivity threshold. The derivative of \(s(2-s)^n\) proves uniqueness of the admissible subunit root. The same proof separately establishes that the rational formula is not a continuous copula at \(\alpha\le-1\).

Run `python check_grpcopula.py` using Python 3 with SymPy and mpmath. The recorded run in `check_output.txt` passed 51 assertions, including symbolic comparisons for dimensions 2–4, marginal and two-product mixture identities, rational valid/invalid cases, high-precision root checks, and covariance signs. Numeric root approximations are not used to assert exact validity boundaries. The provided mathematical derivation covers all dimensions and all real parameters.

The binary mixing construction applies only to nonnegative parameters; it does not assert unique mixing measures. The negative-phase finite cutoff refers only to this GRP rational formula. Independent mathematical review and external certification have not been performed.
