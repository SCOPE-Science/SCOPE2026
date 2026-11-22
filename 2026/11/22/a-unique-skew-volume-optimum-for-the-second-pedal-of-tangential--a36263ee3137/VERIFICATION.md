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

# Reproducibility and proof boundary

The proof in `RESULT.md` applies to every real \(0\le c<1\) by exact vector identities and an elementary derivative-sign inequality. No finite test is used to claim an infinite result.

Run `python verify_rhombic_pedal.py` in a Python environment with SymPy, NumPy and SciPy installed. This checker differentiates the proposed volume formula, confirms its exact algebraic factorization and rational maximizing-root bracket, and tests 48 distinct rational-prism examples. For each test it constructs the actual pedal feet from rational facet normals, selects an exposed-hull triangulation, computes its volume using exact rational determinants, and compares the exact result with the closed formula. The triangulation is selected numerically, so it serves only as an independent diagnostic, not a certified hull algorithm for arbitrary symbolic parameters.

The unique real maximizing root is proved by the strict monotonicity of its quintic, not by an approximate solver. The printed decimals are for orientation only. No independent mathematical audit or external verification has been performed.
