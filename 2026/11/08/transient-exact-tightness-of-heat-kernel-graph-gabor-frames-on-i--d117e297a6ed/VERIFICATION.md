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

# Verification of the heat-frame tightness theorem

Run `python verify.py` in the directory containing `RESULT.md`. Python 3 with SymPy, NumPy and SciPy is required. An actual execution produced `GRAPH_HEAT_FRAME_VERIFY_PASS 1424 k1_t 0.34663861547152`.

Exact algebra checks include the factorization of the crossing difference polynomial and all ten coefficients in the Möbius-transformed polynomial. The script compares positive crossing times and signs for \(1\le k\le100\), checks exact rational spectral-projector weights for \(1\le k\le500\), and independently constructs the graph Laplacian and double-time heat matrix for \(k=1,2\), validating eigenvalue multiplicities and heat diagonal formulas.

The **infinite-family** proof is not furnished by sampling. It rests on a six-eigenspace decomposition of the graph Laplacian, orthonormal basis completeness for the frame operator, and an algebraic one-sign-change argument yielding a single positive root via Descartes' rule. The asymptotic statement uses the unique root and its defining exact equation. All tightness claims refer to the explicitly unscaled atom definition in `RESULT.md`; different normalizations or graph Laplacians are not covered.

Scientific limits: no independent audit or external mathematical certification was performed. The proof does not give perturbation robustness or a classification of every graph with finite-time tightness, and historical priority remains provisional.
