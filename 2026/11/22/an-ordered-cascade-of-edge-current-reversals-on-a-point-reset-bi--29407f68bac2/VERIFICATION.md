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

# Reproduction and proof boundaries

Run `python verify_cascade.py` from the same directory. The implementation depends only on the Python standard library and constructs the generator independently of the closed-form root expression. It uses exact rational arithmetic to solve the finite stationary equations and computes independent hopping-edge currents, while a separate floating-point root expression and bracketing check their sign and rate crossings. The implementation checks cycle sizes \(3\) through \(12\), rational rate choices, threshold ordering, and near-symmetric asymptotics. The completed embedded script passed 180 test families and the three quoted \(n=6\) threshold values.

The infinite-family proof depends on the exact characteristic-root representation and the strictly negative grouped derivative of \(\log R_j\), not on the count of test cases. The critical limits \(r\downarrow0\) and \(r\to\infty\), strict roots and finite-size quantifiers are explicitly handled in the proof. Neither a computer algebra package nor any independent formal or external validation is asserted. Generalization beyond the stated homogeneous, one-source Markov system is unproved.
