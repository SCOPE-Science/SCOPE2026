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

# Reproducibility

The proof's classification is mathematical, and the following stand-alone Python 3 checks are provided to corroborate its finite boundary cases and independently validate the underlying graph presentation.

`python3 verify_direct.py` exhaustively searches the standard eighteen-vertex Pappus graph by selected set size and builds the token-jump and token-slide adjacency lists. Expected: minimum eight, 108 optimal codes, 108 jump edges in 27 four-cycles, and zero slide edges.

`python3 verify_geometry.py` constructs the nine points of \(\mathbb F_3^2\) and the nine retained lines from their equations. It constructs all 108 geometric codes, checks every four-plus-four incidence candidate, and verifies the independently parameterized component partition.

`python3 verify_model.py` verifies a complete explicit 18-vertex relabelling between the standard 27-edge cubic model and the affine incidence model.

The three accompanying `.out` files are the exact standard outputs from execution of the packaged scripts. The verification does not establish historical novelty, and a finite check cannot by itself replace the symbolic structural proof in `RESULT.md`.
