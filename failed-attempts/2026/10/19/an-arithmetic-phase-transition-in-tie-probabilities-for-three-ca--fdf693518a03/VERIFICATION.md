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

For the two differences, the eight ballots yield the stated centered four-vector with covariance (1/8)[[2,0,1,0],[0,2,0,1],[1,0,2,0],[0,1,0,2]]. The support contains zero and signed basis vectors; hence both the irrational integer marginal and the coprime rational projections have unit full-lattice span. Partial Fourier inversion on the pinned integer coordinates and scaling by sqrt(n) give the Gaussian Schur complement on the unpinned coordinates, nondegenerate even at the rational endpoints. Thus asymptotically half of the pair equalities beat the third committee. Pair-equality masses are 2/sqrt(2 pi (a^2+b^2)n) and 2/(pi n), while triple equalities are O(n^-1) and O(n^-2), respectively. The disjoint exactly-two-plus-triple decomposition gives both constants. A fresh exact replay (python3 /workspace/replay_thiele.py) enumerated ordered profiles through n=4 with exact quadratic-irrational comparisons and recovered 1147/4096 and 1075/4096. The frozen checker uses tolerances in some comparisons; neither it nor the replay establishes the infinite limits.

## originality

FAIL

The separate assigned record 2 already states and proves the entire focal finding in the same model, and gives a further elementary finite-size clause. The two formulations differ by notation and limits versus little-o expansions, not by mathematical content. This is demonstrable frozen-set coverage, not a determination of publication priority or an identification of the two packages as the same record. Xia also covers the rational order independently, but not the constants or irrational law in the inspected theorem.

## value

PASS

As a mathematical result in isolation, the fixed-weight exponent transition and constants give a useful baseline for optimal committee ties and explain why exact irrational weights cannot be replaced by fixed rational approximants for this limit. This value does not make the duplicated theorem a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
