---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The exact forty-cell map for F_s=a∘R_{s/5} follows from the dyadic branches on all half-open cells; recursively computing first returns from C_0..C_4 gives heights s=0:(8,8,8,8,8), s=1:(2,2,2,2,32), s=2:(6,6,6,6,6), s=3:(2,2,20,8,8), s=4:(2,8,8,1,1). Independent integer-cell path reconstruction returned exactly 10 omitted cells in two 5-cycles for s=2 and 20 in four 5-cycles for s=4, and zero omissions for s=0,1,3 and induced stationary permutations as asserted. The nonstationary s=3 and s=4 induced maps reach stationary cases. Exact a(7/8+u/8)=a(u)/8 on each dyadic branch proves the infinite descent for covering towers; a(I) excludes zero, hence no finite orbit survives the stationary covering renormalization. The only residual finite arrows have least period five, so endpoint inclusions, masses (0,0,1/4,0,1/2), and global classification follow for all real x∈[0,1), not merely sampled points.

## originality

PASS

Best-of-knowledge PASS for the simultaneous GLOBAL five-rotation pointwise periodic-set classification, not for existence of 4/5 half-measure island. Bruin–Lukina provide the rotated-odometer model, return principles and part of the 2/5 non-covering data. The November 2 exact-quarter-return result already covers all five first-quarter return times, the full half-measure 4/5 periodic island and its endpoints. It expressly does NOT exclude other periodic points in the complement; its full-measure return saturation for s<=3 is not global pointwise aperiodicity. The present exact induced return maps and omitted-cell exhaustion establish those missing universal statements and the 2/5 full intervals.

## value

PASS

Global exact classification of periodic POINTS (not merely measure-a.e. or first-quarter returns) for a naturally defined five-sector rotated-odometer family; the 2/5 vs 3/5 asymmetry and period-five island masses are motivated dynamical invariants. The extra descent and omission proof is a substantive finite-to-infinite argument; it is not simply recomputing the already published return table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
