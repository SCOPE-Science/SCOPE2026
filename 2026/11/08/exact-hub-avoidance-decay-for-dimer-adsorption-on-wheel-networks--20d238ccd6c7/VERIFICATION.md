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

`verify_wheel.py` uses Python standard-library `fractions.Fraction`, `itertools`, and `math`, with no third-party dependency. Run `python3 verify_wheel.py` from a directory containing this file. It checks the exact hub-vacancy probability on wheels with rim lengths 4, 6, 8, 10, 12, 14, 16 using **two independent finite rational calculations**, and additionally enumerates all 8! edge-clock rankings for rim length 4. It checks the odd-rim obstruction for five rim vertices and computes the modified-Bessel defining root from a convergent power series; success ends in `ALL_CHECKS_PASS`.

The exact finite-state recurrence counts all currently available rim edges and spokes; the alternative calculation integrates matching-edge clocks separately over all permutations of their arrival ranks. The agreement is independent of the transfer-operator eigenvalue calculation. The derivation of the exponential asymptotic and the proof of a unique positive eigenvalue are mathematical arguments in RESULT.md and are not inferred from computation. The historical literature comparison does not constitute an independent priority certificate.
