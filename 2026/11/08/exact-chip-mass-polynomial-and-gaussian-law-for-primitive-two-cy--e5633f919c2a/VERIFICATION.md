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
# Reproducibility and verification

The exact formula counts initially primitive-two configurations of synchronous parallel chip-firing on the labelled simple cycle with no sink, with each site initially carrying a nonnegative integer number of chips. A site with at least two chips sends one to each of its two neighbours at each synchronous step.

The all-size proof is supplied in `RESULT.md` and does not depend on the finite tests. The local firing table proves that all initially primitive-two states have site values at most three. Thus `check_direct.py`, which exhaustively iterates the cube `{0,1,2,3}^n`, really does enumerate **all** primitive-two states for each tested `n`, not merely a sample from a larger unbounded class. It computes the two updates from chip counts, using no matching or transfer-matrix routine, and compares every chip-mass coefficient to the stated formula for `3<=n<=9` (349,504 enumerated configurations in total).

`check_polynomials.py` constructs the quadratic-root power sum independently via its recurrence in `z`, and compares all coefficients to the explicit cyclic-matching formula for `3<=n<=150`. It also validates the support, endpoint coefficients, palindromy and the Pell–Lucas total for each of those `n`. The contained output files are the captured successful program outputs; they do not certify untested infinite cases or constitute an external independent audit.

To reproduce on Python 3 with the standard library only, run `python3 check_direct.py` and `python3 check_polynomials.py`. There are no external software dependencies. The Gaussian limit follows analytically from dominant-root expansion, not from simulation.
