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

The standalone Python program `check_geometric_gabor.py` requires Python 3 and NumPy. Run `python check_geometric_gabor.py` from a directory containing this file. It prints `GEOMETRIC_GABOR_CHECKS_PASS 305` when all included numerical assertions pass.

The checker independently forms every normalized geometric window, constructs all cyclic time-frequency shifts, vectorizes every rank-one measurement projector, and compares the singular values of the resulting square matrix with the predicted ambiguity singular spectrum in dimensions \(2\) through \(6\). It separately checks direct ambiguity sums against the closed form, integer rank predictions through dimension \(10\), and both sharp even-order resonance slopes through dimension \(12\) at several radii. Finite floating-point rank tests use a tolerance and should not be mistaken for exact symbolic certification or a proof of arbitrary-dimensional rank.

The analytical argument in `RESULT.md` provides the all-dimensional proof: Weyl-character orthogonality, two finite geometric-series sums, modulus-forced half-shift resonance, elementary arithmetic on the unit circle, and a small-phase trigonometric expansion. The proof assumes the exact cyclic indexing and normalized counting conventions stated there; changing those conventions changes numerical spectral factors. The report records self-review only; an independent mathematical audit has not been performed.
