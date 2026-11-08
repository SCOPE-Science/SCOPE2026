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

# Verification and reproducibility

Execute `python3 check_rectangle.py` with Python 3 and SymPy installed. The file independently enumerates the feasible vertices of the scalar constraint polytope for ten rational length pairs; 84 exact-radical comparisons and ten scalar–Hilbert gap identities passed during preparation. `RESULT.md` contains the universal proof based on convexity and the parallelogram identity. The exhaustive finite-vertex checks are for the listed ratios only and are not a proof of the full continuum of aspect ratios. The proof covers all positive Euclidean rectangle side lengths and all real Hilbert targets of dimension at least two. No independent mathematical validation has been performed.
