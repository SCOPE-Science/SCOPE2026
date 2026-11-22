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

The proof is analytic above the explicit cutoff and finite-exhaustive below it. `checker.py` implements two independent character calculations (residue-set membership and Euler's criterion) and tests every odd prime less than 149. `checker-output.txt` records the output of the current execution. Its 17 above-cutoff checks are regression tests only; they do not replace the character-sum proof. The critical bound uses the smooth genus-one models of two cubics and a quartic and the genus-two model of one quintic. Each polynomial is squarefree in odd characteristic. All six mixed-pattern non-occurrences below the cutoff have explicit zero counts; the threshold is sharp at 29. Publication priority and mathematical independence are not asserted.
