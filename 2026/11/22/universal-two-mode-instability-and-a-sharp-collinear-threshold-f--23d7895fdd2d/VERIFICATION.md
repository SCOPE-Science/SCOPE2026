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

# Verification and reproducibility

The self-contained proof in RESULT.md establishes the theorem for all integers \(M\ge3\), every \(k,c>0\), every collection of \(\beta_j>Mc\), and each closed polygon; it also covers all values of the sharp collinear susceptibility. The proof does not rely on numerical samples. Exact derivative, kernel-rank and Sylvester-inertia arguments are the essential certificates.

The standalone `verify_inertia.py` needs Python 3 and SymPy. Run `python verify_inertia.py`. It constructs the polynomial dynamical vector field independently from the potential, symbolically differentiates it, substitutes exact polygon equilibria, asserts vanishing vector field and symmetry of the Jacobian, and counts algebraic eigenvalue signs. It passed five cases: an equilateral three-oscillator triangle, a square four-oscillator polygon, and collinear four-oscillator balanced configurations for \(R=1/2\), \(R=1\), and \(R=2\). The checked inertias were respectively \((2,3,1)\), \((2,4,2)\), \((1,4,3)\), \((1,3,4)\), and \((2,3,3)\). Computation of these particular cases is not exhaustive proof for general populations.

Scope limits: the theorem assumes positive real coupling, no reactive coupling, zero nonlinear frequency shift, identical natural frequencies and strictly active amplitudes. Collinear zero eigenvalues do not determine higher-order nonlinear center dynamics. No independent audit is represented by the included exact symbolic tests.
