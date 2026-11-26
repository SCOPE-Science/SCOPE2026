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

By orthogonality the fourth moment is the squared coefficient norm of P². An unordered edge pair with overlap is identified by its doubled vertex and the two single vertices, and a double edge by the two doubled vertices. The three opposite-edge pairs alone collide, at (1,1,1,1), giving 2S²−Σ|a_ij|⁴+8Σ_{r<s} Re(p_r overline(p_s)). On a finite torus M≥3 each pair-sum coordinate lies in {0,1,2}, so there are no extra collisions. With Σ|a_ij|⁴=(Σt_r²+Σδ_r²)/2 and |p_r|≤t_r/2, the displayed identity follows and is nonnegative. The squared-magnitude variance is (Σδ_r²+Σ(t_r−S/3)²)/2, bounded by the first two terms of that identity. All ones give moment 90 at S=6. Nonzero equality has t_r=S/3, δ_r=0, and equal p_r (of common modulus S/6, not literally unit modulus as phrased in the proof). After dividing by the common coefficient magnitude, choose u₁=1, c₀=b₁₂b₁₃/b₂₃, and u_j=b₁j/c₀: the equal product relations then yield the vertex-phase factorization in both directions. Independent exact replay passed 4,096 Gaussian-integer arrays in the continuous model and M=3,4, and 256 equality arrays. The replay found moment 168 at M=2 for all ones, consistent with its exclusion.

## originality

FAIL

Two distinct indexed results cover the scientific content. The all-square-free-layer proof explicitly includes degree two and specializes at n=4 to the norm and vertex-phase equality. More decisively, the six-root packet for q≥5 has the identical partition of unordered pairs by pair sum under the bijection of the three opposite pairs to the three root-antiroot pairs, including all six double edges as singleton fibers. This pair-sum equivalence transfers its entire arbitrary-complex quartic form without requiring a group isomorphism. Its exact deficit becomes the frozen deficit under X=t, D=δ and z=p, and the squared-magnitude bound follows by dropping nonnegative terms. The order-four torsion of the other support does not obstruct the transfer: use its q=5 case to match the collision partition of each target M≥3. The two comparison records are later-indexed; this is a finding of existing mathematical coverage, not a decision about who discovered it first.

## value

FAIL

The six-character layer is naturally motivated and the stability identity is useful, but as a new narrow exact result it has no substantive uncovered invariant after the coefficient-preserving collision transfer. The remaining presentation on this character group, including M=3,4 without aliasing, follows mechanically from the coordinate range {0,1,2} and the known three-pair formula; the magnitude corollary only discards nonnegative terms. No separate valuable repair is supported by changing the representation or restating that corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
