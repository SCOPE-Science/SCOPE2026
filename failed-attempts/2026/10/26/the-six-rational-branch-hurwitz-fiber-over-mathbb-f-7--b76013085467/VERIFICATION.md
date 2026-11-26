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

Riemann–Roch and very ampleness of the complete degree-three linear system give the projection model over F_7 without a choice of rational origin. In the depressed model the only fixed-base freedom is scaling the third section, since any addition of a linear form would restore a Z^2 term. With a fixed complement 0,∞ the tame discriminant condition is exactly 3Q^3+R^2=κ(X^6−Y^6), κ≠0. A new exact coefficient hash join computed all 2,401 cubic squares, compared with 343 quadratic cubes at each of six nonzero scalars, and recovered precisely the twelve claimed models. Fiber scaling has two orbits, one for each κ=3,4, and swapping X and Y interchanges them. The smoothness check via the three partial derivatives is valid over the algebraic closure; the branch sextic is squarefree and the projection has degree three. Independent count by normalizing projective coordinates gives 13 rational points, which attains the integer Hasse bound.

## originality

FAIL

The central arithmetic cover count is a routine specialization of the published exact prescribed-discriminant count of Weir–Scheidler, Theorem 3.10(1), not just an application of a generic enumeration algorithm. Set ℓ=3, q=7, M=0. The two possible quadratic resolvents are D_κ: y²=κ(x⁶−1), up to squareclass; inversion in x exchanges the squareclasses (−1 is nonsquare). For κ=3, the two degree-two elliptic quotients are y²=3(u³−1), u=x², and v²=3(1−w³), w=x⁻², v=y/x³. They are quadratic twists and have 12 and 4 rational points, respectively, by the nonzero cube values ±1. On rational 3-torsion the hyperelliptic involution acts by −1, so the two quotient elliptic Jacobians give the plus and minus eigenspaces for x↦−x: pullback after pushforward is 1+i for the relevant involution i and pushforward after pullback is 2. Thus Pic⁰(D_κ) has 3-rank one. The old theorem gives (3−1)/2=1 cubic field per resolvent, i.e. two fixed-target classes, exchanged by base inversion. All six simple branch inertia groups are transpositions and the genus-one condition follows from Riemann–Hurwitz; taking normalization translates the field count to covers. A displayed model is then verified by substituting Q=X², R=2Y³ in the discriminant and checking smoothness; its point count is an elementary seven-element fiber tally. No claim is made that the older paper explicitly prints these models or the number 13; the independent special-case certificate does not make the covered classification original.

## value

FAIL

The maximally rational branch configuration is natural, and the distinction between fixed and reparameterized targets is real. But its exact class count is mechanically determined by the existing prescribed-discriminant theorem with the small elliptic quotient counts above. The extra explicit model and seven-element point tally serve as an illustrative example, not a separately motivated unresolved invariant or structural contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
