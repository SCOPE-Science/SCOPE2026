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

# Verification of the high-energy three-population theorem

The proof uses the conserved Casimir \(BD/C\) and an exactly canonical two-dimensional Hamiltonian. Its Hessian determinant is \(e^{p+q}+K^{-1}e^{p+q}(e^p+e^q)>0\). Properness and strict convexity give one periodic orbit at every energy above the minimum. The coarea identity exactly matches the period and canonical enclosed-area derivative; convexity and Brunn–Minkowski justify derivative asymptotics from the triangular scaling limit. The controlled interior negative-logarithm branch consumes asymptotically full orbital time and yields the uniform segment measure. All constants are for fixed positive \(a,d,K\).

The included `check.py` requires Python 3, NumPy, SciPy and SymPy. It checks symbolic conservation/field identities and finite-energy quadrature at two independent parameter sets, obtaining period/energy ratios approaching the proven limit. The computations are not an infinite-energy proof. No result is claimed for vanishing or varying parameters, total-variation convergence, or an error-rate estimate. Sources inaccessible in full text are indicated in REVIEW.md and AUDIT.json.

No external independent mathematical validation has been performed.
