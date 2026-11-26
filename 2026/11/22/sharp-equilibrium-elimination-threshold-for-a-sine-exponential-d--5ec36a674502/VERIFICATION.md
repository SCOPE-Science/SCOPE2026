---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

On the branch open at b, the exponential lies below the chord from (b,0) to (1,c), which is strictly below the diagonal even at its endpoints. At b the sine branch gives 1, and at 0 it gives a>0. On [0,b), divide F(x)-x by cos²(kx) to get a-A_b(x), where A_b=x-(1-x)tan²(kx). Its derivative has the sign of 1-2kE_b(x), with E_b=(1-x)tan(kx). The numerator of E_b' is k(1-b)+u-sin(2u)/2>0, u=π/2-kx, so E_b runs from 0 to infinity. At b/2 it is 1-b/2>b/π. Hence A_b has exactly one maximum x_*<b/2; it starts at 0, rises to a_*>0, and ends at minus infinity. Also A_b(x)≤x<b, so a_*<b. This proves the 2/1/0 census. At a root F'-1=-cos²(kx)A_b', and F'>0 in the interior, giving the two multipliers. The double root has positive second derivative 2(1-a_*)k²cos(2kx_*); the increasing map with positive displacement on each side attracts locally from the left and repels on the right. Dividing the Taylor expansion by the coefficient of z² gives z²=K(b)²δ+O(δ^(3/2)) (the nondegenerate maximum first gives z=O(√δ)), yielding the stated splitting. At fixed x>0, A_b increases with b, so evaluating at the smaller-b maximizer proves strict monotonicity. The critical equation first gives kx_*=O(b) and x_*=O(b²), then kx_*=b/π+O(b³), which gives the stated small-b expansion.

## originality

PASS

The exact phase boundary and its root and multiplier classification distinguish this result from the original example, generic sign criteria and analogous phase diagrams. No equivalent or dominating statement was established in the bounded comparison.

## value

PASS

This settles an analytic parameter-selection question for the very map the source introduced as an equilibrium-free example. The exact boundary eliminates c from that decision and tells which parameter choices inadvertently introduce a stable equilibrium. The root census, multipliers and small-b scale give information absent from the numerical slices. The value is specific to equilibria and does not rely on claims about chaos or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
