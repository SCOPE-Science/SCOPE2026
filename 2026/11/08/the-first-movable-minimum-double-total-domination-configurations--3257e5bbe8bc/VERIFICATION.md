---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The defining open-neighborhood condition at square (i,j) is exactly r_i+c_j-2x_ij>=2. The global minimum size8 follows by empty-column versus all-positive-column row-sum argument. All size8 optima split by column support into exact families of sizes 15,1080,1350,24,720, totaling 3189. Any legal single exchange preserves selected row and occupied-column support; only three-active-column configurations move. For each of 20 triples the four omitted-column symbols have multiplicity <=2 and yield a connected 54-state graph with 144 edges and diameter5. Independent complete C(24,8) binary subset enumeration reproduced count3189, 2880 exchange edges, degree histogram 2109/360/720, and no non-slide exchanges. The first-board cutoff requires checking the finite n*m<=24 grid, not an infinite family assertion.

## originality

PASS

Kazemi–Pahlavsay–Stones 2015 already give minimum double-total domination cardinality 8 for 4x6 and the row/column feasibility inequality, and are credited. Their sample optimal matrices and larger submatrix transitions do not give all 3189 configurations or the single-token exchange graph in the inspected full Section 3. Distinct ordinary total-domination reconfiguration theorems do not apply to minimum double-total domination.

## value

PASS

The exact first mobile board is a natural threshold for optimal redundant detector placements; full optimum count, frozen fraction and connected 54-state exchange geometry are independently useful finite invariants, not mere recomputation of minimum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
