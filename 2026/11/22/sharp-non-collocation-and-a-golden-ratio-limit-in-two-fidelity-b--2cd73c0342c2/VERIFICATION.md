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

# Reproducibility checks

Run `python verify.py` from this package's extracted root. The script uses only the Python standard library and does not rely on any historical file or external network request. It verifies 1,745 supplementary assertions: 726 exact rational covariance-versus-sequential-update comparisons, exact positive finite-ratio co-location deficits, the limiting algebraic constant and a finite grid of asymptotic consistency checks. The infinite-parameter existence, localization and uniqueness assertions are proved in `RESULT.md`, not inferred from enumeration.

The exact domain is \(d>0\) and \(x,y\in[0,1]\); the finite-\(d\) strict separation holds for all such values. The exactly two globally maximizing locations and the sharp expansions are asserted only for all sufficiently large \(d\). No numerical threshold is certified. The historical co-kriging literature comparison does not prove exhaustive originality and independent audit has not been performed.
