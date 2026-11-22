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

# Reproducible calculation and proof boundaries

The mathematical proof is in `RESULT.md`; the executable `verify_pentagon_hessian.py` checks the stated finite symbolic identities and an independently assembled numerical second-variation matrix. Reproduce with Python 3, NumPy and SymPy by running `python verify_pentagon_hessian.py` from the directory of the extracted files. There are no input datasets or downloaded dependencies other than the named Python libraries.

Checks performed on this extracted script include (i) the twenty-five oriented facet determinants and the regular-pentagon reference four-volume; (ii) four exact SymPy identities identifying positive spectral bands from cyclic Laplacian eigenvalues and the known sine square; (iii) a direct 30-by-30 constrained half-Hessian calculation from the full facet determinant expansion, with numerical eigenvalues agreeing with the symbolic spectrum to within \(3.1\times10^{-16}\); (iv) twenty randomly generated centered sphere-chart finite differences, with maximum normalized deviation below \(3.5\times10^{-8}\); (v) the limiting Rayleigh quotient of the stated sharp angular first harmonic.

The exact spectrum and its multiplicities rest on the decomposition of the quadratic form into two cycle Laplacians, four transpose-symmetric matrix directions, four orthogonal-orbit directions, and twelve residual directions. The passage from this spectral statement to a local inequality uses the smooth structure of a compact orbit and a stable simplicial facet system. Finite floating-point checks alone do not establish the local theorem or exclude all possible prior literature. There has been no independent mathematical audit.
