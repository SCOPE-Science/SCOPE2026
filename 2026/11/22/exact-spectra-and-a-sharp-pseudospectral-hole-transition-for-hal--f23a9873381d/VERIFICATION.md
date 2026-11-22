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
# Verification notes

The analytical verification is self-contained in `RESULT.md` after applying the standard and explicitly cited rational-rotation irreducible-fiber theorem. Exact determinant and trace computations in every two-dimensional fiber, the complex-vector triangle inequality and the strict least-singular-value criterion are the critical proof steps.

`check.py` is a standalone Python 3 standard-library diagnostic. Command: `python check.py`. Expected output: `HALF_FLUX_THREE_TERM_CHECK_OK 24110`. The checker compares matrix determinants and traces for integer coefficient triples over fourth-root phases, verifies singular bound inequalities and exact open-pseudospectrum membership across a rational grid, and tests nontrivial complex coefficients. There are no external dependencies or downloaded datasets. Finite tests neither exhaust all phases nor replace the analytic proof.

For the threshold example with \(B=3\) and \(C=1\), the ordinary spectral inner radius is \(\sqrt8\), while the inner epsilon-pseudospectral hole closes at \(arepsilon=2\). At that exact epsilon the center is excluded because the defining inequality is strict. The classification does not cover irrational flux or more than three Fourier terms.
