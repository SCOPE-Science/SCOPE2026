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

The partial derivatives cannot vanish together in characteristic 5; in the all-nonzero case their product would force 28=0. Of the lines through [0:0:1], only X=0 is tangent there and its contact multiplicity is 3, so the chart Z=uX+vY contains every bitangent. For u=0 the nonzero X^3Y coefficient rules out a square. For u≠0, matching the leading three coefficients of a quadratic square gives precisely the two equations in RESULT.md. An independent check sets z=u²v: the equations reduce over F5 to z⁴−z³−3z²+1=0 and u⁷=2(z³−4z−1). The z-polynomial is (z+1)(z³−2z²−z+1), with irreducible cubic and no root at which the right side vanishes. For z=−1 there is one rational seventh root and one orbit of six, since 5 has order six modulo 7. For each of the three z-roots of degree three, the power map is bijective on F125*, giving one u in F125 and six others in F_(5^6) (which contains the seventh roots of unity). The latter have exact degree six: their z has degree three, and they are not in F125. Thus those three z-roots contribute one 3-cycle and three 6-cycles. v=z/u² recovers each line, and u=v=−1 gives the rational line. This proves the orbit lengths, counts over every extension, and minimal common field without relying on the classical 28-count to establish completeness. Independent exact replay: `python3 /workspace/branches/review_replay.py 5` also computed the monic eliminant by a degree-four norm and matched all six displayed factors. The frozen script was inspected, not run.

## originality

FAIL

The exact finding is covered in the inspected corpus by a distinct exact characteristic-five computation and by an all-prime cyclotomic classification. Both are indexed under a date later than the frozen record's label; this is demonstrated coverage, not an assertion that either was historically first or that the frozen proof was derived from them. The known-overlap decision does not depend on inability to retrieve Elkies's chapter.

## value

FAIL

The Frobenius action of a standard arithmetic model is a natural and useful invariant: e.g. it gives the point counts of the bitangent locus over every extension. The frozen contribution, however, is that same already covered invariant. A resultant recomputation for one prime, without a distinct reusable theorem, further invariant or new mathematical boundary, is not a separate contribution on value under the narrow-invariant criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
