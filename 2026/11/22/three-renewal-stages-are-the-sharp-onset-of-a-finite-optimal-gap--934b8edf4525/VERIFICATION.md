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

# Reproduction

Execute `python3 check.py` with a standard Python 3 installation. The checker independently uses the stationary cyclic phase chain and killed no-call transitions, and also uses a positive Poisson mixture to propagate phases through a silent gap. It then checks these matrix-derived probabilities against the explicit one-, two- and three-stage formulas, tests strict improvement at the three-stage first optimum, and tests its positive and decreasing gap response across several positive windows.

Actual run of the supplied script: `PASS 533 checks`, with optimum \(2.857475425400\) for unit window length and unit phase rate, versus probabilities \(0.057114565415\) (contiguous), \(0.106347655997\) (optimal), and \(0.105985639917\) (infinite-gap limit). The derivation of the unrestricted uniqueness and sharp limits appears in RESULT.md; these are not inferred from any finite test grid.

This is a mathematical model only, and no experimental field data, empirical animal vocalization model, independent audit, or external formal certification is supplied.
