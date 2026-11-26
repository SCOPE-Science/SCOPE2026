---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the mean-zero subspace the divided differences of the derivative of x^(-p) are strictly positive, making the trace strictly convex. Off-diagonal Laplacian entries distinguish conductance vectors; blowup near disconnection and compactness give a unique minimizer without assuming orbit-constant input. Symmetry then forces constant rail and rung rates, both positive. Fourier diagonalization gives the two stated spectral blocks and differentiation gives S_p=R_{m,p}(t), with coefficients 4-mu_k nonnegative and the zero mode's coefficient positive, so the scalar root is unique. For p below 1/2, integrability and fixed-point bracketing give convergence to the unique positive integral root. At and above 1/2, S_p/m diverges, forcing t to zero, and the k=0 term implies t >= (4/S_p)^(1/(p+1))/2, hence m sqrt(t) tends to infinity. This makes the monotone Riemann-sum error O(t^(-p-1)/m) relatively negligible versus D_p t^(-p-1/2). The two-end cycle sum gives (m/pi) log m at 1/2 and C_p m^(2p) above it, yielding the claimed coefficient 2 at criticality and (D_p/C_p)^(1/(p+1/2)) beyond. The beta-integral singularity and uniform local rescaling give t_p ~ 2(1-2p) from below; at p=0 the integral root is 2/3 by direct integration. Bounded independent replay at /workspace/branches/379e4427-3307-496b-a917-5b9b9a0b47ae/inverse-laplacian-check.md reproduces the exact m=3,p=1 polynomial 8t^4+24t^3-36t-27 and the m=4,t=1 all-order root, as well as coefficients 18^(1/3) and 540^(2/5)/2 at p=1,2. Finite-sum ratios are corroboration, not proof or a finite-size bound. The uploaded checker was inspected, not executed. Limits in m are for fixed p, not a joint critical crossover.

## originality

PASS

The contribution is the real-order trichotomy for the unrestricted cyclic-prism allocation, including the logarithmic critical coefficient and subcritical boundary behavior. Neither the optimization method nor the known p=1,2 examples are novel. The inspected comparisons do not cover the critical-order or full allocation law.

## value

PASS

The theorem identifies precisely when optimal rungs retain positive budget share, when the share decays logarithmically, and when it follows a variable power. This gives a complete asymptotic allocation classification for a natural family of losses and a concrete benchmark for design. The significance rests on the sharp change of allocation across a continuum of orders, not on recomputing the two coherence endpoints or claiming a physical interpretation for every fractional p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
