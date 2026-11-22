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

# Verification record

The mathematical proof in `RESULT.md` independently establishes the complete claimed spectrum: first verify the Cayley--Laplace unitary conjugation and its normalization, then the logarithmic translation identity, then the norm enclosure and the weakly-null Weyl sequences. At \(t=1/2\), direct multiplication by \(4e^{-x}\) establishes the different essential range. Strong continuity is in the strong operator topology and does not imply spectral continuity.

The numerical supplementary check `checks/finite_sections.py` was executed with NumPy and SciPy using order-200 finite sections for \(t\in\{0.15,0.3,0.45,0.5,0.55,0.7,0.85\}\), together with adjoint scalar identities at four positive points. Every programmed assertion passed. The finite eigenvalues illustrate signs and spectral bounds; they neither exhaust infinite-dimensional spectra nor prove the essential-spectrum theorem.

The exact operator-norm formula is already known from the generalized Hilbert-operator norm theorem and is used as an independently checked benchmark, not presented as novel. No independent audit or external certification has been performed. The published historical-priority risk remains.
