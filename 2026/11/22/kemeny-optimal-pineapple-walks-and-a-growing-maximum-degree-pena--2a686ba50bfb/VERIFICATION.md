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

The proof uses exact spectral subspaces, strict convexity, and a positive scalar second derivative to establish all-parameter claims. To reproduce the independent small-matrix computations, use Python 3 with SymPy and run `python verify.py`. The script constructs weighted Laplacians directly, computes exact rational inverse traces for 105 matrix instances, checks the maximum-degree benchmark and numerical derivatives, and tests the fixed-leaf large-clique asymptotics. Expected output: `VERIFY_OK 585 exact and numerical assertions`.

Finite samples cannot establish the infinite theorem or prove novelty. The mathematical argument in `RESULT.md` supplies the global proof. Independent validation is not claimed.
