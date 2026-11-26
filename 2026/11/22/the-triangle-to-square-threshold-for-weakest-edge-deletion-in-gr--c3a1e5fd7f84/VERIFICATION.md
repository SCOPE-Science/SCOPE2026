---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The constant mode cancels for both connected graphs. On the common mean-zero space the spectra are positive, and differentiation gives MZ+ZN=I for the convergent cross integral; traces are basis invariant. Independently derived the triangle cross trace using centered 2×2 operators X=M−αI and Y=N−βI, with α=tr(M)/2, β=tr(N)/2, X²=x²I, Y²=y²I and d=tr(XY)/2. For H=α+β and R=H²−x²−y², integration of the hyperbolic-function expansions gives tr(Z)=2H(R+2d)/(R²−4x²y²), with the repeated-eigenvalue cases by continuity. Substitution and exact cross multiplication matched the actual expanded P/D, both with 30 positive monomials, so the difference has sign b−a for every positive weight triple, including equality at a=b. Vertex relabeling covers all pairs. Independent rational solves for (100,10,11,11) matched the four printed fractions and E₂<E₁<E₃<E₀; exact E₁−E₂ is 18976950041406901787484663/11750543650483124820155055200. The deleted edge is (2,3) of weight 11. Triangles are the only smaller simple cycles, so four is sharp.

## originality

PASS

The full-time trajectory metric and generic evaluation or optimization are not original here. Fitz-Gibbon et al. use the exact same objective, not merely an analogous spectral distance. What remains distinct from the strongest inspected statements is the pairwise order law for every positively weighted triangle under one unrenormalized deletion, together with the exact four-cycle reversal and hence the sharp cutoff. The paper dated 2026-11-17 was compared on the merits, not excluded by the undefined window invoked in the frozen discussion.

## value

PASS

The theorem tests a natural pruning rule for a standard dynamic fidelity objective while holding conductance units fixed. A global triangle guarantee and an exact minimal-cycle counterexample clarify precisely where edge weight ceases to predict the best one-edge deletion; this is more informative than an arbitrary numerical counterexample or rederiving the standard integral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
