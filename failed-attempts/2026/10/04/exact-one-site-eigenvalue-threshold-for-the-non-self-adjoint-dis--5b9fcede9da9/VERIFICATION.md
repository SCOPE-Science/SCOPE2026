---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For any one-site block v, the source's Birman--Schwinger/resolvent equation reduces exactly to \((I+vT_0)x=0\) for some nonzero x. Taking norms gives \(1\le\|v\|\|T_0\|\). Conversely, if x is a top right singular vector of \(T_0\) and \(T_0x=\sigma e\), the rank-one map sending e to \(-x/\sigma\) has norm \(1/\sigma\) and makes the matrix singular; an orthogonal second singular direction raises the block norm to any prescribed larger Q without disturbing the kernel. The boundary equivalence is then immediate from \(Q\max(\|T_0\|,\|T_1\|)=1\). Fresh independent complex 2 by 2 random-matrix tests reproduced the threshold construction to about \(10^{-15}\).

## originality

FAIL

The exact threshold is an implication-level corollary of the primary source's one-site Birman--Schwinger equation plus the standard operator-norm singular-vector fact. Cassano et al. explicitly reduce their one-site witness to \((I+v_0T_0)\phi_0=0\) and define the improved boundary by the maximum of \(\|T_0\|\) and \(\|T_1\|\). For an arbitrary one-site block, the same support reduction is immediate from their general Eq. (5.1); the lower bound \(\|v_0\|\ge1/\|T_0\|\) and rank-one equality case are textbook norm geometry. Therefore the claimed converse outside the diagonal-dominance region is mechanically implied even though the paper does not spell it out.

## value

PASS

Despite being implication-level covered, the conclusion is mathematically well motivated: it exactly classifies the full one-site witness class used in the source's partial-sharpness argument and proves that any boundary saturation outside diagonal dominance must use more support or another mechanism. This is a natural complete obstruction tied directly to an unresolved global-sharpness question, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
