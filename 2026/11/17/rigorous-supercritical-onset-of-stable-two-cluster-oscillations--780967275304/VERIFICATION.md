---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Walsh diagonalization of the Hamming-distance coupling gives effective damping a=(.19,.31,.59,1.11), with simple alternating parity eigenmode and an exactly invariant scalar parity line because tanh is odd. The retarded characteristic factor is Δ_j=z+a_j−(1/25)(1−e^(−20z))+(α/5)H(z), H(z)=∫_0^60 e^(−zv)dv, H(0)=60. The imaginary-axis equations yield explicit α=A(θ) and Q_j(θ)=0; a nonnegative-real characteristic root bound at α≤.0953 gives θ<4.34. Trigonometric signs confine roots to (π/3,2π/3) and (π,4π/3), with tangent+positive increasing B/A equation exactly one root in each interval; growing a shifts roots right, and A(θ) increases there, making the smallest-a first root the uniquely first crossing. At α=0 damping has ReΔ>0 in Re z≥0 and no roots enter from infinity. The odd nonlinearity has no quadratic term; scalar cubic fundamental Fourier coefficient is [α/125 H|H|²+(−.31)^3]/D, D=∂_zΔ. Independently at high precision found θ1=1.847814682771..., θ2=3.499629925869..., α1=.09529711602518, α2=.111991274821, Re λ'=.04596363144>0, Re c=−.01223643281<0 and cosine coefficient 3.87623186586; consistent with pinned interval VERIFY.py and exact Walsh. Standard RFDE Hopf center-manifold theorem then yields radial attraction with stable transverse modes and only neutral phase multiplier, proving local orbital attraction in the full history phase space. Finite numerical evaluations certify signs given the analytic root-exhaustiveness argument, not a global dynamical theorem.

## originality

PASS

Crane 2026 uses the same explicit 8-market model and already approximates the first center and numerically samples stable two-cluster branches. It does not in the full inspected Section 6 provide rigorous supercriticality, first nonlinear Lyapunov coefficient, exact exhaustive frequency/mode crossing proof, or local full-history-space orbital stability. New contribution is precisely that rigorously signed local stability theorem and leading amplitude, not the known near-center parameter or generic Hopf method.

## value

PASS

Turning an empirically observed two-cluster cycle into a rigorous full-history-space stable Hopf branch and sharp amplitude coefficient resolves a clearly identified dynamical stability gap for the very same model. It gives exact first-mode identification across an infinite retarded spectrum, a useful nontrivial boundary theorem rather than a generic Hopf-method restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
