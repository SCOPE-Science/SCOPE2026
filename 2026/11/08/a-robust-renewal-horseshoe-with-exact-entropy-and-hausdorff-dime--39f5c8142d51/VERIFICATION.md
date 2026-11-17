---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For all real |a+2|, |b-3/2| <= 10^-3 the piecewise planar map is continuous at x=0. Direct substitution gives one-step section return ax-1 and three-step LRL return a(1+(a-1)b)x-[1+(a-1)b]-a-1. Rational interval bounds ensure inverse branches phi_0,phi_1 map I=[-9/10,-1/100] strictly into disjoint subintervals and LRL intermediate x signs +,- and negative y at the second phase. The unique address on the separated IFS produces a conjugate renewal three-state shift with transitions 0→0/1, 1→2,2→0; rho(A) solves lambda^3-lambda^2-1=0. Strong separation and bi-Lipschitz affine phases yield dimension root |a|^-d+|a[1+(a-1)b]|^-d=1. Only the explicitly constructed compact subsystem, not the full attractor, is proved to have these invariants.

## originality

PASS

Best-of-knowledge original quantified robust 1/3-return subsystem for this exact boundary-Hopf planar family. Its symbolic entropy and self-similar dimension are not obtained merely from a generic robust-chaos result or a numerically observed attractor. The closest Simpson study defines the map, while his separate first-return theorem assumes a repelling-focus regime delta_R>1, incompatible with b-1≈0.5. Inaccessible full primary texts, particularly 2024 zero-determinant survey, remain priority risks.

## value

PASS

A constructive, open-parameter rigorous entropy/dimension certificate for a physically motivated boundary-Hopf return map offers a mathematically motivated shift from numerical chaos to an exact invariant for a natural subsystem. The finding does not overstate full-attractor properties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
