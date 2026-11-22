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

# Reproducibility and scope

Extract `verify.py` next to `RESULT.md` and run `python verify.py` in a Python environment containing NumPy and SciPy. The verifier prints `PASS 852 assertions` on success. It builds weighted \(K_{m,m}\) Laplacians directly, compares their positive numerical eigenvalues with the exact three-class formula, checks rational thresholds for spectral orders zero, one and two, compares one-dimensional numerical minimizers with the predicted edge-support phase, and probes both scaling regimes across multiple network sizes and real orders.

The mathematical theorem is proved from strict convexity and exact spectral/derivative identities in `RESULT.md`; finite checks are only supplementary diagnostics. The proof uses unnormalized Laplacian eigenvalues and requires the resulting weighted graph to remain connected. No certificate of external or independent validation is asserted. The public text reviewed here contains mathematical definitions, computations, references and scientific limitations only.
