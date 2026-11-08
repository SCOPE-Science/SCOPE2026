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

# Verification scope

Run `python3 CHECK.py` under Python 3 without third-party dependencies. This reconstructs the positive and negative pair-distance autocorrelation peaks directly as sums of triangular kernels and integrates their squared difference exactly over the sorted rational breakpoints. Its selected rational samples verify the exact identity \(E(\varepsilon,0)^2=8|\varepsilon|^3\) and nontrivial two-parameter cases. There is no floating-point premise in the cubic identity checks.

The complete proof for arbitrary real \(L>0\), \(d>3L\) and \(|u|,|v|<L/20\) is in `RESULT.md`; finite samples are not an exhaustive proof. The key analytic steps are convolution with reflection, Plancherel, disjoint-support decomposition, exact three-tent integral \(4|s|^3\), translation Lipschitz estimates, and the pure-split contradiction to any larger inverse exponent. This is an internal self-review only. No independent audit, external certification, numerical noise model, or all-pairs inverse theorem has been performed.
