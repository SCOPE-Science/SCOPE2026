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

For |z|=1 write u=sin²(arg z/2). Then |φ|²=1−u and |h|²=64u³. Squaring the perturbed symbol gives |ψ_ε|²≤1−cu with c=1−16/100−64/10000>0, except for equality at the contact point. The maximum principle and nonconstancy give disk self-maps. The power difference quotients on the monomial basis are bounded by n|h| times the (n−1)st power of the larger symbol modulus. Their squared sum is dominated by 64u³(2−cu)/(cu)³, a bounded majorant off a single null point, so joint dominated convergence proves the complex Hilbert–Schmidt derivative. Summing n²|φ|^{2n−2} gives exactly 64∫(2−u)dm=96 for the squared norm, with normalized arc measure. Under w=(1+z)/(1−z), the Hardy unitary gives 16F(2w+1)/(w+1)²+32F′(2w+1)/(w+1). Laplace inversion gives the triangular kernel 16e^(−t)(t−4u)e^u for 0<u<t/2. Output dilation is unitary and transforms this to 32√2(−T+R) with T kernel e^(−2x)ue^u and R kernel e^(−2x)(x−u)e^u, both for u<x. The triangular composition factors of R have squared Hilbert–Schmidt norms 1/4 and 1/3, hence R is trace class. For T the inverse energy in y=e^(2x)Tg is ∫e^(−2x)|y′|²/x² with mass ∫e^(−4x)|y|². Smooth compactly supported y are a core by approximating g and canceling its weighted moment with arbitrarily small L² corrections far out. The Liouville change dξ/dx=xe^(−x) has length one; multiplying y by e^(−3x/2)/√x gives the positive potential printed in the record. Closure from the core embeds the form into H₀¹, and min–max with the whole Dirichlet interval for the lower bound and interior intervals for trial functions gives s_n(T)∼1/(πn) without assuming bounded endpoint potential. Ky Fan inequalities with an index shift proportional to n in both directions show that trace-class R does not affect the coefficient. This proves n s_n(A)→32√2/π, and the Schatten threshold and logarithmic partial-sum limit follow directly from that positive coefficient.

## originality

PASS

Credit the concrete Hardy composition-path derivative, its exact squared energy and its sharp singular-value residue after the explicit spectral reduction. Do not credit a new Weyl law for weighted Volterra operators: a verified older theorem already covers the reduced principal operator T and gives exactly 1/π. It does not identify the Hardy tangent, establish Hilbert–Schmidt differentiability and energy of the path, or put the conjugated kernel, which is not of its separable form, into that class modulo a trace-class remainder. The closest related Hardy and Dirichlet statements inspected do not supply that identification or the combined result.

## value

PASS

An affine symbol with quadratic boundary contact and a cubic perturbation gives a concrete path of composition differences whose Hilbert–Schmidt tangent is at the weak-trace endpoint but not trace class. The exact ordered coefficient and logarithmic residue quantify the failure of trace-class regularity; the Hilbert–Schmidt energy alone cannot read it off. The nontrivial reduction from the composition path to a spectral model gives an exact example for Hardy boundary-jet analysis rather than merely substituting weights into the known Volterra asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
