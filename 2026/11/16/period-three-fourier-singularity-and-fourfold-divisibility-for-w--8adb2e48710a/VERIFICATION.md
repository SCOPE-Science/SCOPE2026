---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=3 the weighted matrix-tree identity gives the full unnormalized signed spanning-tree Walsh coefficient as the determinant of M(r,s) with the precise signed (not absolute-degree) reduced Laplacian. Unsigned wheel trees are L_(2n)-2 and have odd count for 3∤n, forcing every signed coefficient odd. For n=3k and arbitrary 2k signs u_j,t_j, the exact (1,1,2)-periodic vector annihilates the specified signed M and yields 4^k distinct zeros. For n divisible by 3, all edge inclusion counts are even: spoke count F_(2n), rim count tau-F_(2n), and total tau=L_(2n)-2 is 0 mod4 by the Lucas matrix recurrence; each signed coefficient is tau-2 sum_{negative e}N_e mod4, so universally divisible by four. Independently checked all 4/16 period-three witnesses at n=3,6 by exact integer matrix multiplication, and small n wheel tree counts; the general proof is algebraic, not inferred from examples.

## originality

PASS

Best-of-knowledge: actual proof and cited primary/read indexed comparisons distinguish the specific result from older general tools and different objects; this is not a guarantee of priority.

## value

PASS

The wheel spanning-tree indicator is a natural symmetric graph kernel; exact characterization of singular versus invertible Walsh convolution and a structural 4^k construction of invisible frequencies are meaningful beyond the classical tree count. Uniform divisibility by four is a nontrivial spectral arithmetic invariant, later supporting sharp inverse-gap studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
