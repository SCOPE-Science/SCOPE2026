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

Inverting the selected 2×2 covariance with off-diagonal ρ^(j−i) gives the stated conditional diagonals inside the interval, and the farther covariance coordinate is a multiple of the nearer one outside, so the exterior diagonals reduce to 1−t^distance. After one pivot these latter diagonals increase strictly with distance, including the exact midpoint tie. For ε=1−t, (1−t^k)/(kε) is the average of 1,t,...,t^(k−1), between 1−(k−1)ε/2 and 1. This bounds both factors and the denominator of the bridge term uniformly, even for short gaps. Summing and scaling gives the uniform objective F(x,y)=x²/2+(1−y)²/2+(y−x)²/6 with error O(nε+1/n). Its strictly convex minimum is 1/10 at (1/5,4/5). The discrete greedy domain converges to the two reflected half-edges, including midpoint ties; on (x,1), 0≤x≤1/2, F=1/8+(2/3)(x−1/4)². Compactness and density give exactly the claimed extreme values 1/8 and 1/6 and the limiting optimizing sites (up to reflection), so the ratios are 5/4 and 5/3. Finally 1−t^(j−i) increases strictly with separation, proving unique finite determinant maximization by the endpoint pair. The analytic argument is sufficient; recorded finite checks were inspected, not rerun.

## originality

PASS

Credit the AR(1) conditional covariance, maximum-residual-diagonal rule, and historical OU design setting to prior work. The supported distinct claim is the sharp simultaneous grid-limit envelope over allowed greedy tie choices and the trace cost of deterministic determinant maximization on this same family. The strongest available related statements do not give these comparisons; this is a bounded judgment, not a priority guarantee.

## value

PASS

This is a natural normalized covariance family with ubiquitous first-pivot ties. The best possible tie still leaves a 25% asymptotic trace penalty, and an endpoint or central start incurs a 2/3 excess over optimal; determinant maximization selects the same asymptotically worst trace choice. These sharp comparisons distinguish criteria and quantify a practical tie-choice effect, beyond identifying the already-studied optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
