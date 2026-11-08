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

# Reproducibility and checks

Execute `python3 verify.py` with NumPy and SymPy installed. In a fresh run on the embedded checker the process returned exit status 0 and the following output: `PASS 1472 exact and finite-dimensional diagnostic checks`. It checks the characteristic polynomial, products of orthogonal projections, compression powers, spectral location, the regular-polygon nilpotent exception, and a rational two-atom identity.

The checks cover finitely many explicit dimensions and deterministic trials; their success is not an exhaustive classification or an infinite-N proof. The result's universal proof is in RESULT.md. In particular, the passage to the root-rate limit follows from finite-dimensional Gelfand's theorem; nilpotent rigidity follows from the unimodular algebraic identity. Independent mathematical audit and publication-priority verification have not been performed.
