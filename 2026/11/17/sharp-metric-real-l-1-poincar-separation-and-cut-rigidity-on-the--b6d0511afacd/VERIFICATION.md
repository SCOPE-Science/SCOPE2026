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
# Verification of the Heawood constants

Run `python3 verify_heawood.py` alongside this file. The script uses only the Python standard library. It constructs the seven Fano lines as triples of distinct nonzero elements of the three-bit vector space, proves the 21-edge degree-three graph object by assertions, computes each distance shell by BFS, exhaustively evaluates every nontrivial cut (taking complements to reduce comparisons), and uses exact Fraction arithmetic for all relevant ratios. Successful output reports `HEAWOOD_EXACT_OK metric 27/13 l1 24/13 six_cycle_witnesses 28` and a cut minimum-boundary dictionary for sizes 1 to 7.

The analytical argument in RESULT.md proves the graph-wide bound, sharpness and equality cut characterization without depending on floating point calculations. The level-set disintegration extends the cut statement to arbitrary real L1 spaces. No finite brute force search is claimed as proof for any broader graph family. Independent audit has not been performed.
