---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Let H be the Boolean adjacency matrix with zero diagonal shore-blocks and off-diagonal blocks M and its transpose, where M represents R. At each step the full adjacency is cubed: the off-diagonal block is exactly M_t M_t^T M_t, and backtracking retains each old edge. Thus H_t=H^(3^t). A walk of that odd length exists exactly for an opposite-shore pair with finite distance at most 3^t: any shorter path has the same parity and can be padded by retracing one edge. Therefore the first fixed point is the first round that reaches the entire cross-diameter (an earlier fixed point could not later grow). The empty relation is stable at round zero under the stated convention. A simple odd path uses equally many vertices from both shores, hence length at most 2h−1; the balanced path realizes the bound including h=1, with surplus vertices isolated. Each odd separation 2j−1 has 2h−2j+1 possible starting positions along the path, giving exactly J_t(2h−J_t). The anchored recurrence instead gives the off-diagonal block of H^(2t+1), which also checks its comparison. This is an unrestricted proof, not reliance on the frozen finite tests; verify.py was inspected, not executed.

## originality

PASS

Credit is limited to the explicit trajectory, sharp two-shore stopping time and path profile for simultaneous self-composition and their contrast with the anchored rule. The fixed point, walk-power ingredients and analogous uses of graph powering are not original. No inspected result gives the specific claim package for this update.

## value

FAIL

The synchronous-versus-anchored distinction is useful exposition, but the new quantitative content is a routine graph-powering deduction. The typed adjacency cube is the update itself, so every layer follows from ordinary odd walk lengths and backtracking. The maximum is then exactly the elementary upper bound on the length of a simple alternating path, attained by the path, and the profile just counts vertex positions at each separation on that path. No further closure obstruction or non-obvious extremal phenomenon is demonstrated; the sharp formulas here are not enough to elevate the textbook calculation to a separate scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
