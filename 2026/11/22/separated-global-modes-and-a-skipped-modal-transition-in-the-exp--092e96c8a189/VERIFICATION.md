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

Verification is based on an independent-of-floating-point exact-rational comparison certificate and an analytic infinite-tail argument.

Execute `python3 check_certificate.py` in the directory containing the package. The script uses only Python 3's standard library and rechecks the positive-series rational enclosure for \(\log(25/21)\), then verifies 28 rational-power enclosure inequalities by integer cross-multiplication. It certifies the sign change of \(p_2-p_0\) between shape exponents \(779/1000\) and \(39/50\), and the four strict comparisons of competing masses \(p_1,p_3,p_4,p_5\) against \(p_0\) at the upper endpoint.

The floating-point calculations in the script propose sufficiently wide rational power enclosures only; no scientific inequality depends on their accuracy. Failed approximate guesses cause an integer assertion failure, never a false pass. The proof of all remaining infinitely many comparisons uses strict concavity of the real CDF-power interpolant on \([4,\infty)\), not computational enumeration. The uniqueness and local mode-switch statements follow from monotonicity of exact probability-mass ratios. Independent human assessment of historical priority and proof is not included.
