---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The determinant −2 is nonzero modulo 3. Under the edge labeling, each open neighborhood is the rectangle obtained by deleting the corresponding left and right endpoint, giving all nine rectangles. A skew force may originate at either color, so it is exactly completion of one such rectangle. Each completion preserves the connected components of the selected-edge subgraph. Conversely, a missing edge in graphic closure closes a simple selected path of length three or five. For length five the resulting six-cycle has a chord joining opposite shores and cutting it into two four-cycles; complete the one avoiding the missing edge first, then the other. A completed closure is therefore independent of force order and is exactly graphic closure. A spanning set must connect all six vertices and the size-five ones are trees; the reduced Laplacian gives 3^4=81. A separate exact replay agreed on all 512 subsets and found 81, 78, 36, 9 and 1 spanning sets at sizes 5–9, respectively. This establishes no classification of other realizations or orders. The bundled checker uses int.bit_count(), so use Python 3.10+ if replaying that checker; it was read, not executed here.

## originality

PASS

The prior existence claim for a realization with loops is not the claim of a simple loopless realization. The audited graph and its open-neighborhood assignment are genuinely different; classical spanning-tree enumeration is not a separate originality claim.

## value

PASS

The initiating realizability result explicitly permits loops, which change the skew color rule. The candidate resolves that modeling restriction on a natural boundary example by giving a familiar vertex-transitive simple graph and proving all-set closure equivalence, not just a minimum cardinality. Rectangle completion explains how length-six dependencies arise from degree-four neighborhoods. This is useful independently of larger-grid classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
