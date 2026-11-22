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

# Verification of the harmonic-trinomial localization theorem

The complete proof is in `RESULT.md`. To reproduce supplementary finite numerical checks, use `python3 CHECK.py` with a standard Python 3 interpreter. The checker was executed against the submitted file and returned `PASS: 39 finite root-configuration diagnostic cases`. It computes branches of the inner and outer rescaled harmonic equations at thirteen coprime pairs and three coefficient values, and compares the individual first-order locations and expected extreme-mode parity.

The proof of completeness uses compactness of every rescaled zero sequence and nonvanishing limiting Jacobians; **the numerical root-finding routine does not establish completeness**. The sharp odd-degree outer-bound defect is derived analytically, not estimated from the numerical experiments. The asymptotic holds for each fixed admissible exponent pair, without an explicit universal coefficient threshold. Historical priority, particularly relative to the full inaccessible 2025 Melman article, is not independently validated.
