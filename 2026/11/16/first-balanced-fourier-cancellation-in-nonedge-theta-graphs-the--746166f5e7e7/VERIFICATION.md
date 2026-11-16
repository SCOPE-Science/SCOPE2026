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
# Reproducing the finite Fourier certificate

Three Python 3 standard-library files are provided in the same directory: `direct_check.py`, `transfer_check.py` and `replay_check.py`. Execute `python replay_check.py` to compare all 25,029 exact coefficient residue triples and assert every claimed classification and degree count. The full seven-row output is recorded in `census.json`.

The direct checker constructs the edges and filters vertex-colour configurations. The transfer checker does not enumerate proper colourings: it independently computes branch contributions by integer coefficient triples in \(\mathbb Z[t]/(t^3-1)\), with cyclic convolution and exact terminal summation. Both checkers verify symmetry-forced zeros and all seven path-length combinations. Their outputs agree per frequency, not only in summary. No floating-point tolerance is used.

The certificate covers exactly the nonedge three-path theta graphs on at most eight vertices. Its finite character census does not imply a result on arbitrary larger theta graphs, different numbers of colours, or full priority against inaccessible historical literature.
