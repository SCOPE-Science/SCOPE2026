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

With λ=α+2>1 and a≥0, projection onto the one-dimensional kernel span gives P=(1−|w|²)^λ|1+aw−w²|²; its boundary value is zero and its value at the origin is one. The monomial norms give the stated total squared norm, so subtracting the captured norm gives the exact squared error. At each positive r the modulus squared is a concave quadratic in x=cos θ with vertex a(1−r²)/(4r); the constrained optimizer is the vertex clipped at 1. The unconstrained envelope is (1+a²/4)(1−r²)^λ(1+r²)². Its only interior radial maximum for 1<λ<2 is at r₀²=(2−λ)/(2+λ); it is strictly decreasing for positive r when λ≥2. For λ<2 the vertex is feasible at r₀ exactly when a≤a_c. This gives the two phases, merger, and captured norm, including a=0. For a>0 the clipping boundary r_b solves a=4r_b/(1−r_b²); in the real-site cases the outer branch decreases from r_b. At r_b the branches share their derivative, since their difference before radial weighting is [4r−a(1−r²)]²/4. The inner objective increases from zero radius and its positive stationary point solves a=h_λ(r) on (0,1/√(λ+1)); h increases from 0 to infinity since its derivative numerator after factoring λ+2 equals (1−r²)²+λr²(1+r²)>0. Beyond that interval the inner derivative is negative. Thus the root is below r_b in the real-site regime, and equals r₀ at merger; the origin uniquely wins at a=0 for λ≥2. The exact arccos phase gives the square-root asymptotic. Evaluating h′ at r₀ gives 8(λ+2)/λ³, hence the claimed positive one-sided radius derivative. The finite numerical checker was inspected, not run; no finite grid establishes the optimizer counts.

## originality

PASS

Credit the standard one-kernel objective, prior existence and prior examples of nonuniqueness. The distinct result is the complete sharp weighted-disk phase diagram for the specific quadratic, with its exact critical curve, radius behavior and captured norms. The inspected related claims do not contain this phase diagram.

## value

PASS

The quadratic family is the simplest type here with interference of both first and second angular harmonics; real coefficients do not force an optimal sampling site to be real. The theorem answers which weights and coefficients give nonunique sites, explains when the symmetry-related pair merges, and quantifies the angular scale and radial kink. The result is a complete global optimizer classification for a natural kernel objective, not merely another existence example or a single optimizer computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
