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
# Reproducible verification

Run `python3 verify.py` in Python 3. No nonstandard packages or network access are required. The script checks the vertex-sum identity against a separate lattice-inequality generator for \(k=1,\ldots,9\), integrates both closed-form CDFs to recover the exact proposed second moments, and draws fixed-seed uniform points in a triangular sector of the hexagon. Direct Euclidean nearest-neighbor computations for \(k=1,\ldots,6\) are compared to the formulas at multiple thresholds and to the stated moments. The finite enumeration and random sampling passed. Neither sampling nor the tested finite range proves claims for all \(k\); the proof is in `RESULT.md`.
