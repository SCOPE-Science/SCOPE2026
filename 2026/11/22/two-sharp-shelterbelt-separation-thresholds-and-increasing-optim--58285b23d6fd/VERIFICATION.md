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

# Reproducibility and verification scope

The accompanying `verify_windbreak.py` is a standalone Python 3 checker requiring only the standard library. Run `python3 verify_windbreak.py` beside this file. The observed test result was `PASS 83416 assertions`.

The program checks the independently accumulated wind-speed deficit along three spatial intervals against the closed-form impulse-integral objective, exact rational benchmark arithmetic, critical threshold values, optimizer feasibility and strict gap order, and comparisons against boundary candidates and many sampled competitors. The exact rational benchmark is \(a=1/2\), \(E=1/9\), \(x=2/3\), \(y=1/3\), giving \(S=17/18\) versus \(7/9\) at coincident rows.

Finite sampling does not establish uniqueness for uncountably many parameters. The proof in `RESULT.md` establishes uniqueness using a one-dimensional strictly increasing function with a derivative-sign change, and exact algebra establishes both transitions. The checker does not test fluid-dynamical fidelity, economic costs, calibration, or historical priority. No independent audit or experimental validation has been performed.
