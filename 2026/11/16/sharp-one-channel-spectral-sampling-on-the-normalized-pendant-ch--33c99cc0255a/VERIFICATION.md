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

# Verification details

The standalone file `checker.py` runs with Python 3, NumPy and SymPy and was executed from the actual packaged directory. It independently checks symbolic endpoint identities and 5,495 numerical assertions: exact two-band fiber eigenvalues, eigenvectors, unit-row lower bounds, quadrature tightness, random complex competing sensors, and direct periodic-graph synthesis by FFT. Expected output: `PASS 5495 fiber and signal checks; exact endpoint identities`.

Critical infinite-dimensional steps are the unitary Fourier decomposition, continuity of the nonconstant Bloch projector over a positive-measure interval, and the rank-two obstruction above \(4/3\). They are proved in `RESULT.md`; finite tests do not prove infinite statements. Full text of the directly motivating preprint could not be inspected, so literature coverage remains a declared originality limitation.
