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

After transforming original masses q_j into tails S_i=sum_{j>=i}q_j, the exact ODE is S_i'=a S_{i-1}+(1-a)S_{i+1}-S_i with a=(sum S)/m, S_0=1, S_(m+1)=0 and m=2k>=4. Its off-diagonal partial derivatives are nonnegative throughout the ordered tail simplex and strictly positive along neighboring coordinates on the segment from the uniform U to a comparable state; strong comparison propagates an initially strict difference to all tails. With w_i=i(m+1-i), barriers U±epsilon w are admissible for 0<epsilon<1/((m+1)(m+2)), and direct substitution gives F_i(U±epsilon w)=±epsilon(m-1)/3+epsilon^2(m+1)(m+2)(2i-m-1)/3, strictly signed. Monotone barrier orbits converge to the only equilibrium strictly on their respective sides of U, the endpoint consensuses; comparison sandwiches all initial stochastic-order-comparable orbits. The equilibrium equation in z=a/(1-a) has a strictly increasing polynomial with unique root z=1 in the positive domain. The symmetric tail Jacobian J=H+2*11^T/(m(m+1)), H negative Dirichlet tridiagonal; 1^T(-H)^(-1)1=m(m+1)(m+2)/6 gives rank-one inertia ratio (m+2)/3>1, so exactly one positive and m-1 negative eigenvalues. Independently exact-rational checked strict barriers k=2..10. This proves a global sufficient cone, not complete basin boundaries.

## originality

PASS

The one-dimensional unstable-index claim is explicitly ALREADY ESTABLISHED in the October 12 entropy-dissipation theorem and is not credited as original. That prior paper also proves full convergence and an entropy-sublevel basin certificate. The distinct surviving new claim is global selection from the entire first-order stochastic-order cone about U; it is not implied by the earlier energy sublevel condition. For m=4, the comparable perturbation q=U+epsilon(e_2-e_1) has S_2-U_2=epsilon>0 and all other tail differences zero, but the energy Hessian along this direction at U is positive, so at sufficiently small epsilon the energy is above F(U), outside the prior certificate. Cao–Gong established only far-mean sufficient conditions and equilibrium census. Best-of-knowledge original component is therefore the order-cone barrier theorem, not the already-published index or convergence trichotomy.

## value

PASS

The FOSD cone is a substantial explicit high-dimensional global attraction certificate for many nonsymmetric initial laws with central means, extending the source and earlier entropy sublevel basins. The decisive value is classification of a genuine previously undecided region, not the already-known saddle index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
