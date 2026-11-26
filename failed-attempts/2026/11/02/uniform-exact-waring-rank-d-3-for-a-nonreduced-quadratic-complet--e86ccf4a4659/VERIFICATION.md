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

The quadratic intersection B consists of the double point at [1:0:0] tangent to Y=0 and the two simple [0:1:±1]; X^d−Z^d avoids all three support points. The resulting regular sequence is Artinian Gorenstein of socle degree d+1. Direct differentiation annihilates the stated nonzero F_d by all three generators, hence it is the top inverse system and has precisely the given annihilator. For the upper bound, independently of the presented Hilbert–Burch calculation, with N=d+1, the sum of ζ(ζx+z)^N/N over ζ^N=1 equals N x^(N−1)z by root-of-unity orthogonality. The two remaining powers give at most N+2 summands. For the frozen lower bound, if no line contains d points of a proposed set of at most d+2 points, sort the remaining vertices for each P by their lines through P. The largest group has size at most d−2. Pair entries separated in this ordering by M=max(largest group, ceiling(half the number of remaining vertices)), leaving singletons as necessary. Each pair uses a line avoiding P, as do chosen lines for the singletons. At most d−2 lines suffice and their padded products separate all P. Evaluation is then surjective in degree d−2 and the saturated point ideal is generated through d−1 (by a nonvanishing linear form and the bounded Hilbert function of the resulting Artinian reduction). Thus the reduced point set would have to contain the nonreduced finite scheme B, impossible. If a line contains at least d points, the pencil has no common line factor, ruling out just one off the line, and there is no linear annihilator. The only remaining arrangement is d points on L and two off it on M; its conic LM must be one of the two reducible pencil members since the determinant is λμ²/4. Cubics LH_2 show that the off-line pair must be the reduced zeros of the complementary quadric on M. This also forces the degree-d generator coefficient to vanish in a lift of the reduced divisor of d points on L, so the complementary quadric divides that divisor on L. For LM=XY one of the two restrictions has a double zero; for LM=Y²−Z² the restriction on M forces the off-line pair to include L∩M. Both are contradictions. The finite frozen script was inspected but not run; no assertion of machine certification is made.

## originality

FAIL

The whole rank formula, not just the sextic value, follows from Ballico–Bernardi's low-rank structure theorem in arXiv:1003.5157, Theorem 1, by verifying its hypotheses and the two off-line points. Their fourth-secant paper also explicitly identifies the relevant case in its main proof, albeit with a conflicting Proposition 7 heading. The conclusion does not depend on silently amending that heading or on obtaining the publisher copy. The special nonreduced-base family is not covered by the particular sufficient conditions cited from Bhat et al., but is covered by this stronger, earlier Veronese result.

## value

FAIL

The explicit apolar argument is a self-contained reproof for this family, but the sole claimed new exact invariant is already determined uniformly by existing rank theorems. The record does not establish a different invariant or generalize the elementary method to a new class outside that coverage. The motivating nonreduced case is legitimate, but recomputing this already implied formula does not make a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
