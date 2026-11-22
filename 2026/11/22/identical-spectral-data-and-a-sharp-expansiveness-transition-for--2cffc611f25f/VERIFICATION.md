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

# Verification

The exact semigroup blocks are triangular matrices whose exponential is computed using the nilpotence of the off-diagonal matrix. Their singular values and spectra are obtained algebraically, without infinite truncation. The sharp lower-modulus equivalent is proved by coercive localization of the saddle and density of the positive-integer sampling mesh. The critical threshold and supercritical eventual equality follow from differentiation and block accretivity, respectively. The reparametrized-orbit construction gives an explicit uniform error upper bound tending to zero.

`checker.py` is a standalone Python standard-library diagnostic. Executing `python checker.py` returned `CHECKS_OK 130 finite assertions`, including four subcritical parameter families, critical and supercritical test cases, and sampled explicit counterexample witnesses at increasing block indices. In the example \(a=c=1\), \(\beta=2\), \(\gamma=1\), the analytical coefficient is approximately \(2.331643981597124\), while the sampled discrepancies at indices \(25,80,200,500\) were approximately \(0.262812283\), \(0.0824059701\), \(0.0329724989\), and \(0.0131896469\), bounded above by the explicit analytical estimates. These numerical diagnostics neither certify the infinite-dimensional statements nor establish novelty.

The applied prior theorem is Huynh, arXiv:2611.01005v1, Theorem 5.1; its relevant hypotheses and proof were inspected against the present model. No independent audit has been performed.
