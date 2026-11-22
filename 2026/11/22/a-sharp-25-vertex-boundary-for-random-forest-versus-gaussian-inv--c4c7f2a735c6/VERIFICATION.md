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

# Reproduction and scientific boundaries

Run `python3 verify.py` from this folder with a standard Python 3 interpreter. The program uses exact rational fractions and no external libraries. In the completed check it reported 612 exact rational assertions: scalar square identities, complete-graph boundary calculations, all-\(n\) formula sampling at finitely many integer dimensions, the exact \(n=26\) excess, the crossover polynomial, and direct weighted-rooted-forest enumeration on small trees. An analytic proof is supplied in RESULT.md for every finite connected positive-weight graph and every real \(q>0\); finite verification is supplemental only.

The root-count distribution includes one chosen root per forest component. Changing that definition, changing the Gaussian law to Rademacher signs, or normalizing by runtime changes the estimand or variance comparison. In particular, the calculated phase window is not an empirical claim about computing time. Publication priority and the possibility of equivalent extremal inequalities are not independently verified.
