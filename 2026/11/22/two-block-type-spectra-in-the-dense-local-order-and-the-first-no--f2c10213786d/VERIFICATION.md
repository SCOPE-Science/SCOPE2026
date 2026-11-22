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

# Reproducibility of the finite boundary check

Run `python3 checker.py` in a writable directory with Python 3 (standard library only). It produces `small_spectra.json`; its console output is reproduced in `verification_output.txt`.

The dynamic-programming implementation expands the all-order weak-composition formula. A separate implementation loops over all binary assignments to the \(nr\) cross-block edges between two internally transitive tournaments; it never uses the antipodal circular formula for admissibility. Local transitivity is checked directly by searching for forbidden four-vertex configurations: a directed triangle and an additional vertex pointing to all three or receiving arcs from all three. All 28 positive ordered pairs satisfying \(n+r\le8\) are exhaustively checked in both implementations.

The checker asserts exact coefficientwise agreement, the palindromic identity, the total \(2n\binom{n+r-1}{n}\), and that the only nonunimodal pairs are \((3,5),(4,4),(5,3)\). It explicitly asserts the two displayed first-obstruction vectors. `VERIFY_OK` indicates all assertions completed; a failed assertion terminates abnormally.

The all-order identity has a separate symbolic proof through the established circular representation. No finite experiment is substituted for that proof, and no comparison against unpublished historical work is claimed exhaustive. No independent mathematical audit was performed.
