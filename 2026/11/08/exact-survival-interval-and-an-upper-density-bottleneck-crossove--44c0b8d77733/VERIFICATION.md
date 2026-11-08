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

The proof uses exact polynomial identities at the fold, monotone interval dynamics, reciprocal parabolic increments, and a direct arctangent summation for the below-fold bottleneck. The finite verifier is `verify.py` (Python 3 with SymPy).

Actual verifier output terminates with:

`VERIFY_OK exact_normal_form=1 exact_order_identity=1 exact_threshold_factor=1 crossover_profiles=9 full_passages=3 overpopulation=3`

The finite checks include fold densities \(\rho\in\{1/8,1/4,2/5\}\), layer coordinates \(\zeta\in\{-1,0,1\}\), and \(\varepsilon\in\{10^{-5},10^{-6},10^{-7}\}\). The upper-cutoff formula is checked directly. Differences between finite and asymptotic passage values remain and shrink on the displayed parameter refinements; they are not asserted to vanish in any finite calculation. The proof, not the experiments, establishes the asymptotic limits. Independent audit: not performed.
