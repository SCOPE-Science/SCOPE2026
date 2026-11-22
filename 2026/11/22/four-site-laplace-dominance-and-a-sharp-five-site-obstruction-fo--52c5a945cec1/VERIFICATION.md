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

# Verification of cyclic reset-destination comparison

The one-attempt clock calculation and infinite series are derived analytically in RESULT.md. The strict positive transform ordering for at most four modes follows from the full-cycle AM–GM inequality, two/three/four-site block bounds, and the periodic block factorization. The exact five-site Brownian witness is independently evaluated with `fractions.Fraction` by running `python3 verify_cyclic.py`. That checker also tests finitely many other rational block inequalities, never claiming finite enumeration is a universal proof.

At the witness, reset rate and diffusivity are one, discount is three, the three distant reset points are at `log(2)` and the two near points at `log(4/3)/2`. The free Brownian transforms are exactly one-quarter and three-quarters. The resulting rational cyclic and independent transforms and negative difference are given in RESULT.md.

The claim does not include general survival stochastic order, nor optimality among arbitrary schedules, nor reversal of mean completion at five modes. Publication priority is not independently validated.
