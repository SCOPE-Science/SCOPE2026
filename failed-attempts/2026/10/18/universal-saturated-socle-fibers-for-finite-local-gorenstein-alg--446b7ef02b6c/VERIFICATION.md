---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For t=rank(ω|M), lift a basis of ωM to vectors v_i. The map R^t→M given by the v_i is injective on Soc(R^t)=(kω)^t. Every nonzero submodule meets this socle: its last nonzero maximal-ideal power is annihilated by the maximal ideal. Thus the map is injective and dim_k M≥st, with equality exactly when it is an isomorphism; a free module has the required image rank. The case t=0 gives equality only for the zero module. At saturation there is therefore just the free-module orbit, with stabilizer GL_r(R); reduction onto GL_r(k) has kernel 1+M_r(𝔪) of order q^((s−1)r²). The target is attained since regular multiplication by ω has rank r, squares to zero, and hence has the unique target Jordan type. With block sizes (r,h,r), h=(s−2)r, the target centralizer has diagonal (A,H,A) and free upper blocks of combined size r²+2rh. Restricting transport from the regular action to the prescribed target gives exactly the centralizer/stabilizer quotient. The order is q^((s−2)r²)|GL_h(k)|, including s=2, and it counts labeled maps, not orbits of such maps.

## originality

PASS

The statement-level evidence supports a distinction for the exact fixed-output formulation over all split commutative local Artinian Gorenstein algebras. It does not support originality for essential-socle rigidity, the square-zero centralizer, or the orbit–stabilizer principle. The inspected catalog results match exact specializations but not the full arbitrary-algebra theorem and postdate the frozen result; the checked primary statements treat univariate zero-output counting, pair-variety geometry, or product feasibility. The absence of a found dominating exact statement does not make the derivation nonroutine or prove historical priority.

## value

FAIL

The saturated fiber is a natural object, and the cardinality is correct, but the proposed exact invariant is a routine consequence of the saturation choice. Basis lifting into the essential socle forces the entire module to be free, so there is no representation-type census left. The map from the single free-module orbit to the single Jordan orbit is the standard homogeneous projection G/H→G/K, and the fiber order is forced by the usual nilpotent centralizer and the reduction kernel for GL_r(R). Both orders depend only on dimensions, so multiplication-independence and the simplified power of q are bookkeeping consequences, not an additional rigidity phenomenon. The record gives no nontrivial range in which different module types must be reconciled, no additional invariant of the saturated fiber, and no application requiring more than that standard homogeneous-space computation. This is a value failure of the frozen claim, not a mathematical error or a priority verdict, and narrowing to one presentation would not fix it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
