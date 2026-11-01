---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For any finite set of distinct minuscule weights, select a cocharacter outside finitely many rational hyperplanes. The ambient projective η-fixed set is then precisely the one-dimensional weight lines. Minuscule multiplicity one and the single Weyl orbit imply each such line equals a Weyl translate of the highest-weight line and belongs to X. Because σ_r(X) is G-invariant, closed/projective, and contains X, its η-fixed locus is exactly the ambient fixed set of dim(V) points. The general Euler fixed-point identity for singular projective complex C*-varieties gives χtop(σ_r)=dim(V), including the cases σ_1=X and σ_r=P(V). Compactly supported additivity for B_r=σ_r\σ_{r-1}, r≥2, yields zero, including empty layers after stabilization. The proof does not rely on smoothness or expected secant dimension. Independent finite combinatorial checks confirmed injective weight pairings in 66 type-A wedge cases, seven D half-spin cases and 18 D-vector cases; finite checks are corroborative only.

## originality

FAIL

The entire purported minuscule secant theorem is an immediate formal corollary of older, explicitly established results: Manivel–Michałek 2014 §2.1 states that all minuscule weights form one Weyl orbit with multiplicity one, so every ambient isolated torus-fixed line is already in the closed highest-weight orbit. Hu 2019/2021 §3 equation (3.18) and its Euler consequence give chi(Y)=chi(Y^{C*}) for any singular complex projective C*-variety. A generic cocharacter separates the weights. Therefore EVERY invariant intermediate projective variety X subset Y subset P(V), not just a secant, has the same fixed points and chi=dim(V). Higher exact rank strata have empty fixed locus, so compact-support Euler zero follows by localization/additivity. Neither earlier paper needs to print the exact secant sentence for its corollary to be covered. The geometric class is natural, but the derivation introduces no new mathematical condition, computation, or specialized secant lemma.

## value

FAIL

Border-rank secant towers of Grassmannian/spinor/exceptional minuscule varieties are natural geometric objects, and Euler invariants can be useful. Nevertheless the entire claimed "freezing" is a one-line application of the classical C*-fixed-point formula to a minuscule orbit containing all ambient fixed points, a property that automatically propagates to any invariant intermediate variety. The special role of secant geometry is only inclusion and equivariance; no nonstandard structural secant lemma, new exact parameter, classification, boundary, or independent computation is needed. The layer vanishing is formal additivity or absence of fixed points. As a standalone research discovery it is a routine already implied localization exercise, though potentially useful as an explanatory observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
