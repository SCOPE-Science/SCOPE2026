---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

After closed-neighborhood observation, exactly the cells in empty-row×empty-column rectangle remain; forcing is possible iff fewer than two empty rows or fewer than two empty columns, hence r>=m-1 or d>=n-1. Inclusion-minimal row bases and column bases determine isolated TAR configurations. At budget m, row bases become connected using one temporary added cell; at n−1 the B_{m,n}=n sum_{r=1}^{m−2} binom(m,r)r!Stirling(n−1,r) isolated column bases appear, merging by n. In square case inclusion-exclusion of row and column bases gives 2t^t−t²(t−1)!. Independence checked by direct power-domination forcing on all subsets and explicit TAR BFS for 7 small boards, including the nonmonotone 3×5 profile (75,1,16,1). Universal proof is combinatorial not finite enumeration.

## originality

PASS

The published October 26 rook power-domination polynomial theorem already gives the exact row/column occupancy criterion and minimum-set counts, which are acknowledged prior ingredients. Bjorkman et al. and Curtis et al. give general TAR connectivity/bounds, and a published triangular-graph component spectrum concerns a different graph. None of the inspected mathematical statements determines every two-parameter rook TAR component count with Stirling isolated jump and reentrant connectivity. Best-of-knowledge PASS for the reconfiguration spectrum, not the occupancy characterization.

## value

PASS

The full TAR component phase profile of rook power-dominating sets is natural to understanding sensor-set mobility and robustness under a size budget. The reentrant transition from connected to disconnected to connected, with exact Stirling-number multiplicities and unbounded separation of first versus permanent connectivity thresholds, is a structural graph-theoretic phenomenon not implied merely by knowing minimum power-domination numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
