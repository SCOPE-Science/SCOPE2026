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

## Reproduction

Run `python3 verify.py` in the directory containing the embedded file. The checker uses only Python 3 standard-library `fractions`, `math`, and `random`. It outputs `PASS: 976 exact-rational and nonlinear numerical assertions` on success.

The rational checks confirm stochastic resolvent inverses, stationary return bounds, the linear-map formula and its threshold, and mean-energy inequalities on multiple directed and asymmetric finite generators. The nonlinear checks use \(\phi(s)=3\tanh(s)\) and compare weighted \(3\log\cosh(s)\) potentials. The all-dimensional statement, necessity at arbitrarily large finite steps, and universal nonlinear comparison follow analytically from the proof; finite tests do not certify their quantifiers.

The displayed scientific findings have undergone self-review only. No independent audit or independent validation has been performed.
