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

The mathematical proof rests on three separately checkable ingredients: (i) the generalized Descartes sign-variation lemma for exponential sums, proved by Rolle induction in `RESULT.md`; (ii) the sorting and majorization reduction for three-species probability vectors; (iii) exact power-sum comparisons for the explicit four-species witness.

To reproduce the arithmetic: from this directory run `python3 check.py` (Python 3.9 or later, standard library only). No online resources or external data are used. The checker reports exact integer moment differences \((4,-54,496)\), seven bases with four sign changes, checks exact preservation under appending common species, and performs an independent finite consistency enumeration of ternary profiles.

Finite enumeration is not the proof of the impossibility theorem for arbitrary positive real probabilities, nor of uniqueness of the two witness crossings. Both infinite statements follow from the analytic zero-count lemma combined with the exact sign certificates. Approximate root values serve as illustration only.

The finding is a population-level identity; empirical richness or sample-abundance estimators, confidence bounds, and prior historical priority require separate analysis.
