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

# Reproducible checks and limits

Run `python verify.py` with SymPy and NumPy available. The execution prints `VERIFY_OK 68 symbolic/exact comparisons` when all assertions pass. The symbolic part establishes the quotient characteristic-polynomial identity as a rational function of a symbolic positive integer parameter, checks normalization of the forced weights, and checks the spectral window endpoints. The tests construct 11 uniform exact-rational transition matrices, check their Rayleigh identities, and compare 40 additional reproducibly chosen rational internal-weight instances against numerical spectra. One exact-rational construction reproduces the previously published four-vertex case, with its numerical SLEM comparison within floating-point tolerance.

The graph-size tests are finite. Only the proof in RESULT.md establishes the assertions for every integer in the theorem. The randomized tests use floating-point symmetric eigensolvers and tolerance \(10^{-9}\); they do not constitute exact certification of arbitrary real eigenvalues. No independent mathematical audit has occurred.
