---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A change and rescaling in the plane variables lifts to the split cubic; smoothness follows from u=v=0 at a putative singular point. The polar criterion can also be checked directly: in coordinates with P=(1:0:⋯:0), write F=t²L+tQ+C, with L nonzero. The tangent section L=0 is a cone at P precisely when Q restricted to L=0 vanishes; the polar 2tL+Q has rank 2+rank(Q restricted to L=0). For the Hesse cubic the Hessian is block diagonal with the ternary block and entries 6u,6v. The ternary determinant on E is 8(λ³+27)xyz, giving nine reduced flex lifts; the binary line gives three points of rank two. Two nonzero tail coordinates leave no rank for nonzero plane coordinates. With exactly one nonzero tail coordinate, ternary rank must be one: for λ=0 only the three plane axes work; for λ≠0 all three plane coordinates must be nonzero (the two principal minors using a zero coordinate force the others to vanish). Three mixed minors then force λ³=216. For λ=6c with c³=1, normalizing x=1 yields q=(1,ρ,c²ρ²), ρ³=1; direct substitution gives rank one and A(q)=9, versus A(q)=1 on the axes at λ=0. Each q gives two choices of tail and three distinct nonzero roots, hence exactly 18 additional geometric points. Bonifant–Milnor's equation (14) gives the same exceptional parameter locus; the singular λ³=−27 is excluded. Independent exact determinant, mixed minor and rank-one substitutions verified with python3 /workspace/reproductions/hesse_review.py. The universal exhaustiveness is the rank argument, not the computation.

## originality

FAIL

Roulleau gives the identical split family in the alternate Hesse parameter, the same 9+3 cone vertices, the bijection with elliptic curves on its Fano surface, and a full classification in which the only counts at least 12 are 12 and 30, with 30 unique to Fermat. His three binary-line cones have elliptic base isomorphic to E, while every Fermat cone has equianharmonic base. Thus a 30-point member must have j(E)=0, not just the converse. Bonifant–Milnor identifies the equianharmonic Hesse parameters and shows their projective equivalence to the Fermat plane curve; that equivalence lifts to this split threefold. The exact uniform dichotomy is covered, even though it is not collected in the cited literature in the frozen notation.

## value

FAIL

The family-wide point count is a natural problem, but it is already determined by the published Fano configuration theorem and the classical Hesse parameter equivalence. The elementary polar-rank proof is useful as exposition, but the only possible remaining claim, explicit exceptional coordinates, is routine transport of the known Fermat list by a Fourier linear change. No distinct geometric invariant or substantive narrower finding survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
