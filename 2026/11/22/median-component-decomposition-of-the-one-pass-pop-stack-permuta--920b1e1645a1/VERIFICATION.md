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

# Verification performed

`verify.py` is a Python 3 standard-library checker in this package. From a directory containing `verify.py`, run `python3 verify.py`.

The checker builds layered permutations from every composition, computes graph edges by actual adjacent-position swaps, and independently tests the one-pass pop-stack operator against all permutations through length eight. It checks the claimed graph decomposition into fixed-long-layer components, the Fibonacci product of component sizes, the Hamming shortest-path formula for every pair of states through length eight, and all component/isolated/edge counts through length twelve. The rational generating-function coefficient recurrences are also evaluated through degree 120. The recorded deterministic output is in `verification-output.txt`.

The infinite statements use the explicit inversion-graph edge-toggling proof, gap/tiling bijection, and formal generating-function calculation in `RESULT.md`. Numerical verification is supporting evidence, not a replacement for these steps. The historical-priority comparison has the limited coverage documented in `REVIEW.md` and `AUDIT.json`.
