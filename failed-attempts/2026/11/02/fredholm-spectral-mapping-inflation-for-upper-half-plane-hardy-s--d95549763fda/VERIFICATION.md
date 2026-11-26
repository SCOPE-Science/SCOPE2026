---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The inhomogeneous derivative norm gives 2π W_n(t)dt under positive-frequency Paley–Wiener, W_n(t)=Σ_{k=0}^n t^{2k}, and dilation sends g(t) to e^{−s}g(e^{−s}t). Thus conjugation by x=log t and the square root of the density gives V_sh=φ_0(x)h(x−s)/φ_0(x−s), with φ_0(x)=e^{−x/2}√W_n(e^x) up to a constant. Its logarithmic derivative b_n(x) is bounded and tends to α and β, yielding L=−∂_x+b_n with domain H¹ by bounded perturbation of translations. The equivalent distributional generator condition in holomorphic variables is zF′ in the stated space. The solutions of (L−λ)φ=0 have rates α−Re λ and β−Re λ at the two ends. In the open strip they grow at both ends, while the conjugate reciprocal is in L² and spans the adjoint kernel. The two half-line integrating-factor inverses have exponentially integrable bounds on their Volterra kernels and their traces match exactly on the codimension-one annihilator, proving closed range and index −1. On the boundary wide far-out modulated bumps have vanishing residual and are weakly null; their H¹ norms are bounded, so they contradict the graph-domain Fredholm estimate. Outside, the group Laplace estimate and reciprocal spectral-distance lower bound agree, giving the sharp resolvent norm. The norm of V_s is sharp by the polynomial weight ratio and limits at ±∞. The same norm for powers and inverse powers traps σ(V_s) in the annulus. In its interior choose e^{sλ}=ζ, so the adjoint eigenvalue needed for the cokernel is e^{s conjugate(λ)}=conjugate(ζ); all lifts differing by 2πi/s give independent Fourier characters times the same nonzero factor. The frozen text writes the adjoint eigenvalue as ζ, but conjugation preserves the annulus and relabeling gives the stated result for each ζ. The equation V_sh=ζh iterated along each fiber t+sℤ has h(t+ks)=ζ^{−k}φ_0(t+ks)h(t)/φ_0(t), incompatible with ℓ² on at least one tail for every ζ in the annulus, proving injectivity. Boundary circles follow by closedness or singular sequences. Thus the stated mathematical mapping failure is valid.

## originality

FAIL

The exact fixed-time Fredholm annulus, infinite adjoint multiplicity and both signs of the sharp group norm are already covered by Resultary f5fe871223a8 (take a=e^s), not merely by analogy to a different weight. The claimed generator Fredholm lines and interior defect numbers are a direct specialization of the established scalar case of the exponential-dichotomy theorem on the exact weighted model; the sharp resolvent norm is then the immediate matching of the standard group Laplace estimate with reciprocal spectral distance. The juxtaposition gives an illustrative mismatch but does not supply a distinct new spectral theorem on this evidence. No original remainder suitable for repair was established.

## value

FAIL

This is a clear illustrative example of Fredholm versus ordinary spectral mapping for a natural group, but the claimed new invariant is not independently valuable under the novelty-of-exact-fact standard: the bounded annulus and its infinite multiplicity are already known here and the generator side is the endpoint-sign case of a general theorem. Exact norm and resolvent facts add no independent novelty. No nonroutine new boundary, invariant or mechanism remains to justify a narrowed repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
