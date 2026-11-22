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

The diagonal substitution q=RS*s produces the quadratic logistic map q→(1+R)q−q² with distinct positive primitive two-cycle q±=(R+2±sqrt(R²−4))/2 precisely for R>2. Its two Jacobians are affine in a single circulant C and commute. Independently expanded their product for general symbolic R,alpha,beta to I−(R+2)(R−1)C/S+(R+2)(C/S)^2 and checked exact rational multipliers at R=12/5 and c=1/100,1/10,1/2. C/S eigenvalues 1 and w±=[1−(alpha+beta)/2 ±i sqrt3(alpha−beta)/2]/S supply full spectrum; longitudinal multiplier is 5−R². On c∈(0,1), w=(1−c)/(1+2c) decreases from1 to0, and P_R(w)−1=(R+2)w(w−(R−1))<0. P_R quadratic minimum passes −1 exactly when (R+2)(R−1)^2=8, equivalently R^3−3R−6=0; the two roots v± and decreasing inverse w→c prove the ordered sink/saddle/sink intervals. R>=sqrt6 fails the longitudinal strict contraction; c>=1 has transverse P_R>=1; c=1 and root couplings are nonhyperbolic rather than assigned a flip bifurcation type. These are local full-3D Floquet statements; finite witnesses alone never establish global parameter inequalities.

## originality

PASS

PASS within full accessible target-source and published comparator readings. The complete Muni 2024 preprint defines the same exact cyclic Euler map but its reported numerically continued period-two branches at R near1 and negative interactions are not the positive synchronous primitive two-cycle that only emerges at R>2. Same-model published Resultary equilibrium Neimark–Sacker proof works in a nonnegative asymmetric competition region with R_*<2, not on the R>2 synchronous two-cycle; Ricker competition uses exponential update and cannot imply these polynomial multipliers. The 1987 Gardini et al article on a cyclic three-dimensional Lotka–Volterra map is highly plausible prior coverage but only abstract accessible; its missing full analysis is a named priority risk, not an invented failed comparison.

## value

PASS

PASS: varying positive interspecies competition at fixed R produces a mathematically surprising reentrant local stability of a genuine positive periodic orbit while its longitudinal Floquet multiplier stays frozen. A complete sharp two-threshold classification on a natural symmetric family, rather than isolated numerical stability checks or a fixed-point Jacobian, is an independently motivated bifurcation/periodic-orbit fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
