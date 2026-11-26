---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

The accompanying `verify.py` forms the seven exact stationary equations for the nonconstant occupation monomials by applying the continuous-time generator on all eight configurations, then taking Boolean differences. It solves the equations over a polynomial domain and checks the currents on both bonds and at the left reservoir by exact cancellation. It also checks the quartic derivative, homogeneous and fast-centre limits, strict-comparison factorization and radical example. A separate computation solves configuration balance at 35 admissible rational parameter triples (seven pairs of mean density and contrast, five dwell times for each).

Run with `python3 verify.py` after installing SymPy. The terminating line ends in `35 rational configuration-balance checks.` The symbolic identities, coefficient signs and Descartes' rule prove the claim throughout the parameter domain; the rational samples are bounded implementation checks.
