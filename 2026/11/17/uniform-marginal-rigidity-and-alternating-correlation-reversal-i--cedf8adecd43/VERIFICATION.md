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

# Reproduction and verification

Execute `python3 verify.py` using Python 3 from the extracted package directory. The program uses Python's standard-library exact `fractions.Fraction`, constructs all monotone affine branch intervals to the requested finite depth, and integrates the resulting linear-product polynomials exactly against normalized Lebesgue measure on \((-1,1)\).

The program checks both conditional phase covariance sequences for every lag from \(0\) through \(12\), plus the paired-block-sum variance formula for every block count from \(1\) through \(8\). Each assertion compares exact rational numbers; all tests passed when executed from the package.

The uniform-marginal classification and full infinite covariance sequences are established by the analytic push-forward and transfer-operator proof in `RESULT.md`. The limiting Gaussian statement follows from an explicitly bounded remainder relative to independent fair binary digits, not finite simulation. The code is a finite cross-check, not a stand-in for these proofs. An independent mathematical audit has not been performed.
