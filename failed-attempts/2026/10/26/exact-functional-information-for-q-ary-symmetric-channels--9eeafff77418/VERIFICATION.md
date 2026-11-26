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

With s_y=P_Y(y)>0 the likelihood ratio is W(y|x)/s_y on the prior support, so only the interval between b_y/s_y and a_y/s_y can contribute to the integral: the width there is m_y and it is 0 or 1 elsewhere. Its contribution, multiplied by s_y, is (a_y-b_y)(-m_y log_2 m_y), including m_y=0,1 and coalescing levels. In the symmetric channel the high-set mass is p_y or 1-p_y respectively; a dropped zero-probability output would contribute zero to those expressions. Strict concavity gives uniform optimality when the levels differ. In the conventional regime P_Y=cP_X+(1-c)u with c=a-b. The gap equals H(row)-(1-c)log_2 q minus the entropy Jensen deficit H(P_Y)-cH(P_X)-(1-c)log_2 q, where H(row)=h_2(epsilon)+epsilon log_2(q-1). The deficit is nonnegative and vanishes only at P_X=u for 0<c<1. At c=0 or 1 the displayed gap is identically zero. No result on gap maximization for c<0 is implied, and no coding achievability is certified.

## originality

PASS

Limited to the explicit q-ary sharp gap optimization and its equality cases as a stated quantitative result: no exact matching theorem was identified. The finite two-level evaluation itself is an immediate evaluation of an existing definition; no novelty is credited for functional information, the integral, or its operational lower-bound role.

## value

FAIL

The channel family and simulation bound are natural, but the two-level assertion reads a single rectangle off the existing defining integral. For the remaining sharp gap, the symmetric output is the textbook mixture with the uniform law, so the claimed improvement is a constant minus the ordinary Shannon entropy Jensen deficit; its maximum and interior equality follow immediately from the deficit being zero exactly at the uniform input. The exact number is just the evaluation there. No distinct structural obstacle, operational improvement beyond the existing bound, or demonstrated need for this particular routine corollary is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
