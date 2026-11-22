---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Reconstructed the exact 3x3 Gram density (det G)^((d-4)/2) over positive-definite matrices with each diagonal <1, including the normalization I_d=(8*pi^(3/2)/d^3)*Gamma((d-1)/2)*Gamma((d-2)/2)/Gamma(d/2)^2 from the three radial-square integrals and two beta correlation integrals. The obtuse linear inequality is F(G)=G11-G12-G13+G23<0. The positive definite maximizer G* with diagonals 1, offdiagonals (1/3,1/3,-1/3) has determinant 16/27 and inverse as specified; logdet concavity and its supporting gradient give a strict global saddle under F<=0 and Gii<=1. Independently symbolically expanded the full determinant in the six scaled marks: linear h coefficient zero; second-order coefficient exactly -(3/2)(z+u+v)-Q(t,p,q)/2 for h=1/sqrt(d). The 3x3 Gaussian Hessian has determinant 2187/64 and parent T variance 8/9, while the one-sided constraints z,u,v have rate 3/4 in the (d-4)/2 exponent. Local boundary Laplace integration gives the single-vertex constant sqrt(6)/12, multiplied by three disjoint obtuse vertices to sqrt(6)/4. Strict global localization plus the local dominating Gaussian/exponential envelope make the transformed conditional densities L1-convergent and hence total-variation convergent by Scheffe. Numerical finite-d simulations and importance tests supplement but do not prove the asymptotic. The support uses volume-uniform balls, not sphere-surface uniform sampling.

## originality

PASS

PASS as to the specifically claimed conditional six-coordinate marked law within the checked source body, with material historical-priority risk. Hall (1982) already gives an all-dimension exact integral for the marginal acute probability (thus could imply the leading probability after asymptotics), and is explicitly credited. Its accessible abstract does not specify the conditional Gram-variable boundary layer; its complete four-page paper was unavailable even after lawful publisher/OA routes, and authorized institutional retrieval reported disconnected VPN; no whole-document absence claim is made. The related sphere-surface Resultary theorem has a d^(-1/2) prefactor and no radial marks; the Gaussian-triangle conditional law is a different vertex distribution. Generic Laplace/Gram methods are tools, not claimed original.

## value

PASS

PASS: a full conditional rare-event geometry law explains the physical configurations generating a rare obtuse angle, beyond a marginal integral or leading exponent. The half-normal d^-1/2 deficit at the obtuse vertex, d^-1 exponential deficits at other vertices and the correlated inner-product Gaussian block demonstrate a distinctive mixed-scale boundary mechanism. Total-variation convergence is stronger than a basic moment or weak-limit computation and is a motivated exact shape limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
