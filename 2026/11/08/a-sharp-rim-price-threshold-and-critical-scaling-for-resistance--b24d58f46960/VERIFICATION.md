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

The theorem uses an analytic Laplacian spectral reduction and a cost-constrained strict-convexity argument for all wheel sizes and positive prices. The Python standard-library file `VERIFY.py` independently constructs weighted Laplacians with rational entries, forms and inverts \(L+J/N\) using exact fractions, and checks the Kirchhoff-index identity against a separate exact cycle-resolvent inversion. It also checks cycle Laplacian moments, the roots-of-unity resolvent identity at selected real values, and the marginal-cost formula in exact rational arithmetic. Executing `python3 VERIFY.py` produced `VERIFY_OK 260`.

The exact cutoff proof follows from the sign of \(\Phi'_{m,c}(0)\) and strict convexity in the linear budget coordinate. The large-wheel proof uses the closed roots-of-unity resolvent identity. For \(c=2+\kappa/m\) and \(t=u/m\), the normalized cost is \(1+[2u^2+(\kappa-2)u]/m^2+O(m^{-3})\), which is minimized by \(u=(2-\kappa)_+/4\). These steps supply the unbounded-size mathematical argument; finite checks cannot establish an infinite statement or literature priority.

Limitations: two uniform price classes; connected allocations only; no independent mathematical audit or proof-assistant certification. The inspected prior literature already covers the uniform-price wheel optimization and weighted-wheel resistance formula, which are not new claims here.
