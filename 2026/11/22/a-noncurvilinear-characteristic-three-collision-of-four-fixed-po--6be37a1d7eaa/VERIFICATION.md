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

Renormalizing the cyclic shift of (1,x,y) by division by x gives (y/x,1/x). In x=1+u, y=1+uv this gives u'=u(v−1)/(1+u) and v'=1/(1−v). The fixed equations, multiplied by the units, are v²−v+1 and u(u+2−v). In the quotient v(1−v)=(1+u)(1+vu)=1, so no supports or nilpotents are introduced at their vanishing sets. Geometrically, stable trees have at most three components, and a three-vertex path admits no nontrivial order-three permutation of its edges. Each edge's partition is therefore individually fixed at any fixed boundary point. There is only one invariant partition, with side {4,5}; this excludes every deeper boundary stratum. On its exceptional P¹ the Möbius map takes infinity to zero, with every fixed point in the stated chart. In the interior x³=1, x≠1 and y=x², so v=x+1, u=x−1; these points are in the same chart. Support inclusion puts the entire equalizer in the open chart, including nonreduced structure. The two successive monic quotients make rank four over Z. Away from 3 the v-roots are simple and u=0 and u=v−2 differ, including in characteristic 2. In characteristic 3 put w=v+1; the relations are w²=0, u²=uw, with uw≠0 and maximal ideal cube zero. In the ambient characteristic-three local coordinates the differences are exactly u(w−u)/(1+u) and −w²/(1+w); they vanish to second order but are not the zero power series, proving tangent identity and obstruction to formal linearization. The supporting script was inspected, not executed; its expansions and finite-field samples are not needed for global support exhaustion or the wild formal conclusion.

## originality

PASS

The existence and geometric realization of a three-cycle are prior, and the tame point count alone is not the contribution. The actual finding is the integral equalizer for the specified split marking action and its noncurvilinear tangent-to-identity wild specialization. The accessible same-action literature was materially compared; the nearby same-surface equalizer calculation is for a five-cycle, not this action. Priority remains qualified by access and indexing limits.

## value

PASS

The full equalizer on a natural compactified moduli space unifies two interior and two boundary tame points and gives their precise bad-prime collision. The isolated wild point has the full ambient tangent space as its fixed tangent space but nontrivial quadratic action. This distinction is not visible stably in a fixed-point count or tangent representation alone and supplies local data for future wild-quotient or equivariant compactification calculations, without asserting their classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
