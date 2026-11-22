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

# Reproducibility and limitations

Execute \(\texttt{python verify_energy_sensor.py}\) with Python 3 and at least the SymPy and mpmath versions listed in \(\texttt{requirements.txt}\). The code checks both covariance integral formulas; exact rational derivative and threshold polynomial identities; the low-noise positive-quartic certificate; the prior energy variance; the root's rational sign isolation; and independent numerical covariance integrations at four sites. It also performs supplementary grid comparisons for several noise values, which are not substitutes for the analytic global proof in RESULT.md.

The core completeness claims depend on derivative factorizations, polynomial signs, Gaussian conditioning and a strict monotone envelope; no finite mesh is used to prove them. The comparison with existing literature was not an exhaustive bibliographic census. Scientific scope is a fixed prior and a single Gaussian-noisy scalar observation.
