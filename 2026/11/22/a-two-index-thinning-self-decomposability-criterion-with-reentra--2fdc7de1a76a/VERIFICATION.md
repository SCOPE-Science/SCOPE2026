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

# Mathematical and computational verification

The derivation expands the exact probability-generating function and then uses the classical canonical-sequence characterization. The only nonstandard all-index reduction is established analytically in the proof by comparison with a two-exponential log-convex sequence. Finite rational tests are not an infinite proof.

Execute `python3 verify.py` using Python 3 standard library. The script checks a deterministic grid of \(q\), negative \(\alpha\) and \(\lambda\), 21 exact coefficient recurrences per grid point, a finite stretch of canonical differences, and all stated witness fractions and phase signs. It uses only `fractions` and `math`; no external data or packages are required. The checker does not certify historical priority or independent validation.
