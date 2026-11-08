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
# Verification and limits
Run `python3 artifacts/verify_masks.py` and `python3 artifacts/verify_signatures.py` from the directory holding this file. Both programs use the Python 3 standard library only and construct the twelve-vertex, twenty-four-edge graph explicitly. They verify that no four-landmark subset edge-resolves the graph and that exactly 192 five-landmark subsets do. All valid single replacements and adjacency-constrained slides are enumerated, and exact breadth-first search from every configuration yields the stated network counts, connectivity, degree histograms and eccentricity spectra.

The first implementation uses 276-bit edge-pair distinction masks; the second uses tuples of vertex-to-edge distances and examines every pair of candidate bases. These are independent algorithmic implementations, not independent external mathematical validation. Their captured outputs are in `artifacts/masks_output.txt` and `artifacts/signatures_output.txt` and each ends in `PASS`. The proof makes a finite exhaustive claim about one explicitly specified graph only.
