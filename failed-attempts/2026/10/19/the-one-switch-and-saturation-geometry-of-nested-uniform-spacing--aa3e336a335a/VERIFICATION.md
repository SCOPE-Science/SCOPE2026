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

Simplex translation gives the joint distinct-coordinate tail (1-s-t)_+^{m-1}; the same-coordinate tail is (1-t)^{m-1}. Diagonal and off-diagonal counting gives the claimed covariance. After factoring out m(1-t)^{m-1}, the derivative at s=0 has sign 1-mt. On s+t<1, after dividing the s-derivative by (m-1)(1-s)^{m-2}, the result is strictly increasing for m>=3 since (1-s-t)/[(1-s)(1-t)] strictly decreases. On s+t>1 the derivative is positive. For m>=3 the derivative is continuous across the cutoff; for m=2 the one-sided slopes suffice (the proof's formula for s+t>=1 should be read from the right at that cutoff). The diagonal at s=t has positive variance except for m=2,t=1/2: near a corner the count is one; near equal lengths it is m or zero when t is below or above 1/m, and at t=1/m there are positive-volume neighborhoods with counts one and m-1 for m>=3. These facts give the claimed positivity or unique crossing, including the exact affine m=2 branches and exception. At s=1-t the bracket is 1-mt^{m-1}, locating the interior-vs-plateau boundary; at interior roots the s-derivative is positive and the t-derivative negative, so the root strictly increases up to that boundary. For t=a/m and s=b/m, the ratio (1-s-t)/[(1-s)(1-t)] is 1-ab/[(m-a)(m-b)]; hence (m-1) times one minus its (m-1)st power tends to ab, giving limiting bracket 1-(1+ab)e^{-b}. The positive root is unique and lies below a for a>1 by convexity and e^a>1+a^2. Evaluating the limit at two fixed points on opposite sides of the root and using the unique finite crossing proves the scaled-root limit. Direct evaluation confirms -3/20 at (m,s,t)=(3,1/5,1/2) and the root 2/5 at t=1/2.

## originality

FAIL

The Oct. 18 circular-coverage record gives the same uniform-simplex model for gap counts (rotate the circle to a sampled point), the identical covariance, the complete sign diagram on the same threshold triangle, the identical saturation segment, and the same scale-limit zero curve in an explicit inverse parameterization. Fixing the other threshold exposes a different plot of the same curve, not a distinct new sign theorem. The genuine extra m=2 endpoint handling is elementary and does not rescue the core claim. This failure is based on a decisive inspected statement, not unavailable classic literature.

## value

FAIL

The complete sign diagram on its own is a worthwhile question, but the existing circular-gap theorem already supplies it on the same simplex law, along with the plateau and scale curve. Replotting that exact diagram and adding a direct two-spacing computation and a numerical substitution do not supply a new useful invariant, classification, or motivated mathematical gap. No surviving repair of the assigned claim is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
