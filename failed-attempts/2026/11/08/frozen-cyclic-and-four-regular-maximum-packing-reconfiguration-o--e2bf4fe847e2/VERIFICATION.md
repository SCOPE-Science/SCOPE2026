---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independent direct enumeration of maximum independent sets of C_N^2 and all host-edge token slides for N=6,7,8,9,10,11,14,17 reproduced the three modular regimes: 3 isolated at residue 0, a single cycle at residue 1, and connected four-regular reconfiguration with N(m+1)/2 states, N(m+1) edges, N triangles at residue 2. N=8 has twelve states each in two triangles; N=11 has triangle incidences 2:11,1:11; N=14 has 2:14,1:14,0:7. The all-N gap proof is valid: slack sum s=N-3m in {0,1,2}, legal moves transfer 1 or 2 units, connectivity follows by defect circulation, and Johnson-triangle classification yields triangles and incidences.

## originality

FAIL

FAIL: the published October 25 all-r cycle-power theorem covers exactly the s=0,1,2 optimum-set token-slide graph by specializing r=2 (the earlier theorem explicitly proves token jumping equals token sliding). It yields the exact counts, connectedness, four-regularity and N triangles. The November 2 paper gives a stronger all-k topological classification and its explicit triangle-incidence table further implies the submitted 2/1/0 incidence and nontransitivity claims. Thus no distinct claimed theorem remains.

## value

FAIL

FAIL as a new contribution: the transition across zero/one/two slack positions is mathematically natural, but an earlier all-cycle-power theorem already gives it, and an earlier stronger cell-complex classification covers the only additional triangle-incidence refinement. Repeating these known results with r=2 does not supply new independently useful data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
