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

The deterministic four-cell partition and invariant density are checked by direct rational branch arithmetic. The accompanying `verify_paired.py` independently reconstructs a four-by-four Markov transition matrix and an eight-by-eight Perron–Frobenius matrix on cellwise affine densities. It checks their symbolic identities, four generating functions, sixteen initial lags, finite-window variances and strict directed asymmetry in those test lags.

Finite checks do not alone imply all-lag claims; the proof in `RESULT.md` supplies an exact rational resolvent identity and a coefficient argument, and the Gaussian sign-sum limit follows from the standard finite-state Markov-chain CLT. No independent external audit was performed. No claim is made for randomly switched maps, nonstationary starts or unequal leakage.
