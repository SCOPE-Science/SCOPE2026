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

# Reproducible exact checks

The bundled `CHECK.py` uses Python standard-library integer arithmetic only. Running `python3 CHECK.py` enumerates every one of the 11,628 five-part compositions with every part at least two and total span at most 24. It verifies an independent cut-position enumeration, counts every reversal class, and compares exact aperiodic correlations by three independent formulas. It detects no nontrivial fiber below span 24 and precisely two distinct reflection classes in a single fiber at span 24. The independent formula for the number of reflection classes follows from Burnside's lemma; the run/gap composition count follows from stars-and-bars.

The checker also verifies the universal construction as a formal two-variable Laurent coefficient identity: its assertion is algebraic for all positive integer values of both resolutions, not merely a finite experiment. The Python checks supplement the explicit polynomial factorization in the proof. No conclusion is drawn about arbitrary real endpoints, noisy measurements, or first collisions at other minimum widths. Neither external independent mathematical certification nor independent audit has occurred.
