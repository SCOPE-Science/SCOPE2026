---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

Run `python3 check_core.py` and `python3 check_transfer.py` from the same directory as these files. Both scripts use only the Python standard library. Their captured outputs are in `check_core.out` and `check_transfer.out`. The scripts have also been run directly from their present package paths, with identical outputs.

The first checker builds the underlying labelled prism and Möbius graphs, builds their simple line graphs, applies the threshold-two update, and exhaustively checks three steps for all configurations at sizes \(n=3,4\). It enumerates proper three-edge-colourings independently for \(3\le n\le10\). The second checker independently builds the nine-state transfer, a rail-swap permutation, and multiplies integer matrices to verify the two traces for \(3\le n\le20\).

These computations are finite corroboration. The all-connected-cubic-graph bijection and all-size ladder formulas follow from the combinatorial proof in RESULT.md. No assertion about other temporal periods, basins or universal graph classes is certified by these tests. No independent audit has been performed.
