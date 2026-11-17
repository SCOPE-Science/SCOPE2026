---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The displayed rational predator–prey reaction with diffusion diag(1,100) and Neumann length π√10 has homogeneous positive equilibrium u=v=h, with κ=(2−h)/(h(2+h)). Direct differentiation gives J(h)=[[1/2−h,−3/2+h²/4],[1/2,−1/2]], tr J=−h<0 and det J=(4+4h−h²)/8>0. At h_c=42−sqrt(43410)/5, D1(h_c)=0 (5h²−420h+138=0); n=0 and every n≥2 remain strictly stable. The critical right vector is (1,1/21), and reflection flips the first Neumann cosine. Hessian, third derivative tensor, and constant/second-harmonic inverses yield exact normal form dot t=S(κ−κ_c)t+Ct³+remainder with independently recomputed S≈0.113222629765>0, C≈−0.603782237456<0. Algebraic rational root isolation certifies signs, not mere floating-point signs. Standard analytic parabolic center manifold/implicit function theorem with spectral gap gives exactly two nearby positive, reflection-related, locally exponentially stable nonconstant equilibria for small κ>κ_c; no global result or all-parameter theorem is claimed.

## originality

PASS

The original Wang–Zou fear-cost-only reaction–diffusion model and linear Turing conditions are already published and receive no novelty credit. Its inspected model equation (81), linear spectral pattern criteria and simulation discussion do not determine the cubic sign or stability of two nonlinear near-threshold patterns. The Song–Zou Turing–Hopf normal form is for a different cost-free reaction tensor. The precise positive-rational specialization, analytic cubic coefficient and stable pitchfork constitute a best-of-knowledge separate result.

## value

PASS

Linear Turing instability alone does not establish existence or stability of a spatial pattern. An exact supercritical sign and pair of locally attracting positive equilibrium branches in a canonical fear-cost predator–prey diffusion model fill that physically motivated qualitative gap. The parameter specialization is a constructive rigorous nonlinear stability witness; it is local, not an unsupported general ecological claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
