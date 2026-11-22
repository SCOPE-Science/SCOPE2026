---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The frozen RESULT.md supplies distinct simple cubic GP(n,2) edges (outer rim, spokes, 2-step inner), complete include/omit face enumeration, complete per-vertex toggle Morse matching and a full directed-gradient acyclicity test. Critical CW cells: n=6 one 0-cell, three 8-cells and two 9-cells; n=7 one 0-cell and one 10-cell; n=8 one 0-cell and one 12-cell. The n=6 signed integral differential [[0,-1],[-1,-1],[0,-1]] has Smith unit rank 2 and the 8-skeleton is 7-connected; Hurewicz makes the two attaching homotopy classes integral degree vectors, so cancelling the primitive pairs leaves S^8 rather than merely its homology. The alternate reverse matching also has primitive unit matrices. The case n>=9 is unproved. Independent edge-cover inclusion/exclusion counts were independently computed: 69,415 / 447,641 / 2,873,983 augmented faces. The inspected source verifier checks gradient acyclicity and integer Morse elimination; these are complete finite exact cases, not extrapolations.

## originality

PASS

No inspected broader two-matching theorem covers these three edge-complexes. The same-complex earlier Petersen graph n=5 has four 7-spheres, not any n=6,7,8 sphere; graph-vertex higher-independence complexes are a distinct simplicial construction. Exact assigned finding appears in the index, but not a separate preceding same-parameter determination. Priority is best-of-knowledge subject to unindexed finite-complex tables.

## value

PASS

These are three consecutive natural cubic generalized Petersen graphs just beyond the classical Petersen boundary, with different integral sphere multiplicities from the n=5 case. Complete integral homotopy types rather than mod-field Betti ranks are exact natural invariants; their contrasting dimensions and lone-sphere outcome make a mathematically motivated finite boundary/classification, without claiming a general n-formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
