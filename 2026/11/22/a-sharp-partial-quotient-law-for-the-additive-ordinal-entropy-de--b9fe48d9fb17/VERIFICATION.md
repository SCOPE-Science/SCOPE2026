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

At each cut a different sampled coordinate wraps to become least; the n ordinal permutations are distinct cyclic shifts, with probabilities equal to the circular gap lengths. Thus the defect is the relative entropy from the uniform law on n gaps. In q=q_k through Q−1, Q=q_{k+1}, the first q points lie within 1/Q of a permuted q-grid, so the largest gap is at most 1/q+2/Q, and inserting points only lowers it. This yields Δ≤log(3n/q)≤log(3(a_{k+1}+1)), including the claimed uniform bound by choosing the surrounding denominators. For a=a_{k+1}≥16, b=floor(a/log a) gives n=bq<Q. Writing an index as r+sq puts its b translates of each base point along one direction of the circle, spaced by δ=|qα−p_k|<1/Q. The arc length (b−1)δ is less than 1/(q log a), smaller than the separation of the q base points. There are exactly q large-group gaps and q(b−1) within-cluster gaps, the latter of total mass ε<1/log a. The chain rule gives H_{bq}≤log q+h(ε)+ε log(b−1), so M_k≥log a−log log a−1−o(1) uniformly in earlier quotients. Together these bounds give both the classification and the leading coefficient. For a_j=j, q_j≥j! and q_{j+1}/q_j≤j+2 imply irrationality exponent two by the convergent formula; in fact the uniform block upper bound directly gives Δ/log n→0 there. The optional finite checks are not used to establish the all-slope statement.

## originality

PASS

The gap identity, convergent-block upper estimate and exponent-two normalized law already occur in an indexed earlier result. The supported distinct claim is the all-slope additive classification and uniform large-partial-quotient block growth. Its lower estimate accounts for entropy within the small-gap group without a cost depending on the absolute denominator. The compared exact gap counts and normalized laws do not already give that maximized asymptotic or the classification as stated.

## value

PASS

The additive defect measures loss of near-uniformity of ordinal patterns on a scale where the standard normalized laws discard the difference. The theorem separates bounded-type rotations from exponent-two rotations with slowly growing unbounded partial quotients and quantifies by how much at their worst phases of observation length. The uniform dependence on the current partial quotient, rather than on the whole scale q, is the useful feature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
