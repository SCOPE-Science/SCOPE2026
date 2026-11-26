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

On the restricted rectangle, row existence of a 1 and column existence of a 0 reduce independently to shore restrictions. Each strict update peels sinks in the corresponding complete bipartite orientation. Rank counts strict world deletions, not an extra graph-only removal of isolated vertices after one shore is empty. A zero row and a one column cannot coexist, giving the fixed-point inclusion-exclusion count I. Removing exactly the specified one-columns (or zero-rows) leaves a labelled submatrix of the opposite avoidance class, with either a strictly smaller dimension or a terminal empty model. This proves the triangular recurrence and its used boundary entries. Alternating nonempty batches give the stated degree bounds; at saturation, all vertices partition into alternating ordered blocks with the last block on the surviving shore. In equal sizes every block is a singleton; in unequal sizes the smaller shore supplies k singletons while the larger shore supplies k+1 nonempty ordered blocks. Edges point toward earlier opposite-shore blocks, giving the bijection and Stirling counts. For two rows, with types A=00, B=01, C=10, D=11, the support sets by rank are {BC,ABC}; {A,D,BCD,ABCD}; {B,C,AD}; {AB,AC,BD,CD}; {ABD,ACD}. Weighting each by its surjection count gives the displayed spectrum, including n=1. An independent direct grid-world replay enumerated 92,314 valuations across 19 shapes, matched the row/column rank, extremal counts and terminal checkerboard criterion, and matched two-row spectra through n=7. Replay: python3 /workspace/branches/5ae753db-4218-4a5a-8177-4ed8d7da8997/independent_grid_check.py; see adjacent independent_grid_check.out. The proof, not the finite run or source verification status, supplies all dimensions.

## originality

PASS

The full labelled rank polynomial here grades every orientation by rounds of state deletion, including orientations with a nonempty cyclic terminal model. The strongest prior graph results already supply the acyclic sink-block bijection and make the degree and maximizer formula a direct block-count consequence in that sector; the Ferrers generator study also identifies the same extremal staircase patterns on squares and adjacent rectangles. I do not credit those consequences or the sink-sequence correspondence in isolation as new. The frozen record's explicitly primary claim is the full-grid recurrence and rank census for this operator; the inspected operator analogues, acyclic enumerations and first-sink generating functions do not cover that claim.

## value

PASS

The single existential announcement is a natural interacting deletion rule for a Cartesian information model. Its exact rank distribution counts valuations reaching stable nonempty cores as well as valuations peeling to emptiness; the rank-zero and two-row spectra provide concrete calibrations. This fills a different finite-counting gap from the acyclic orientation total or a generic bound on announcements, even though those known methods explain the extremal sector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
