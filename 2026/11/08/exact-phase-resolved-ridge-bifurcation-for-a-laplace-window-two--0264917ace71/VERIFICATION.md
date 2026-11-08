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

# Verification of the Laplace-window two-tone result

Reproduce with `python CHECK.py` after installing `requirements.txt`. It validates the exact rational STFT profile, the cubic derivative and critical slope using symbolic algebra, compares the original integral with numerical quadrature, samples the positive-root count for 3,000 parameter pairs, verifies the aligned and anti-aligned root formulas, and independently samples beat-period ridge fractions. The actual executed output was `LAPLACE_STFT_CHECKS_PASSED 6051`.

The continuous all-parameter classification is proved by coefficient signs, Descartes' rule of signs and positivity of the denominator in `RESULT.md`; the finite numerical tests cannot establish it. The comparison with earlier work is best-knowledge, not independent publication-priority certification. The closest 2026 paper's full preprint was not readable through consulted sources. No independent audit has been performed.
