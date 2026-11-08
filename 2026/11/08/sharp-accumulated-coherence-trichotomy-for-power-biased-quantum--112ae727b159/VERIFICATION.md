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

# Reproducibility and proof boundaries

The final claim is the accumulated-coherence trichotomy proved in `RESULT.md`. Its correctness depends on exact spectral decomposition, the positive-real-part hypotheses of the Euler integral, a complex endpoint asymptotic, and an absolutely convergent beta integral. The finite tests below do not certify infinite-time statements.

## Computational check

Using Python 3 with `requirements.txt` installed (mpmath 1.3.0):

```bash
python -m pip install -r requirements.txt
python verify.py
```

The program prints `PASS: 151 deterministic scalar, integral, asymptotic, and critical-circle checks`. It checks Kummer versus transformed Euler integration for twelve parameter combinations, the differential equation and initial derivative, conjugacy of opposite Bohr frequencies, the rational beta integral when absolutely convergent, one direct improper time integration, the critical exponent and phase, large-time coefficient consistency, and the geometric radius identity in a three-level example. The three-level test uses only model parameters and initial off-diagonal entries; the circle proof works for all finite dimensions and all allowed states.

## Mathematical verification limits

Numerical integration is necessarily finite precision, with 48-digit arithmetic and explicit tolerances. The direct infinite-time integral is evaluated only at a parameter safely above threshold; other parameter regimes are treated analytically. There is no infinite enumeration, symbolic proof assistant, external certification or independent audit. Publication priority is qualified by the possibility of an unlocated complex-mode extension of previously known real-spectral Kummer formulas.
