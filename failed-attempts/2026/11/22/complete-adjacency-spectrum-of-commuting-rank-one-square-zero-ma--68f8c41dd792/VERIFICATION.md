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

Two rank-one square-zero matrices can commute only by mutual annihilation: if the products agree and are nonzero, their image and kernel force proportionality, making the products zero. Their flags have q−1 copies, giving simple adjacency B⊗J_(q−1)−I with B the mutual cross-incidence matrix including loops. Its row count is t+(t−1)s. For the point-plus-hyperplane sector U, incidence Gram counts give (t−s)I+sJ and the two stated nonconstant levels. In B² the middle point lies in H∩K and the middle hyperplane contains the span of that point and the two endpoint points. For distinct endpoints, each middle point contributes [n−3]_q except for points on the line joining the endpoints, which contribute an extra Q. The cross-incidence cases give q+1, one, or zero such points. The coincident-endpoint count instead uses [n−2]_q with an extra q^(n−2) for the common point. Subtracting (q−1)QB+qQ²I leaves exactly the point-only or hyperplane-only terms in (1). Hence on U perpendicular the factors are B−q^(n−2)I and B+QI. Dimension and trace yield the two multiplicities and scalar-copy lifting gives the listed eigenvalues. The two negative sectors cannot give a zero adjacency eigenvalue; the positive sector is bounded below by q^(n−2). For n=4 the two negative levels of B coincide for every q, so the corresponding table multiplicities must be added as directed in the assumptions; the n=3 ancillary list still follows with a=0. Independent products of actual matrices reproduced exact annihilators and multiplicities by trace moments in the binary n=4 and ternary n=3 cases.

## originality

FAIL

The prior partial-flag opposition algorithms of De Beule–Mattheus–Metsch mechanically yield the main n≥4 spectrum, even though they do not print this matrix-graph table. Opposition differs from B only by an explicit operator with image in the elementary point-plus-hyperplane sector. The general algorithms give precisely the two remaining magnitudes by standard symmetric-group branching; trace and trace of the square supply the signs and multiplicities. The scalar inflation is an elementary affine eigenvalue transformation. This is a verified implication, not a failure based on the unavailable 2014 paper.

## value

FAIL

The spectrum is a natural invariant and the direct case count is a useful elementary exposition. The frozen contribution, however, is the same exact data obtained by elementary reductions from an existing general algorithm for the corresponding opposition spectrum. The scalar-copy terms and nonsingularity are immediate after those data. An alternative proof is not itself established here as a distinct scientific result with a further substantive consequence or generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
