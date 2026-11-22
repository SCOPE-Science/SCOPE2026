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

# Reproducibility and limits

The proof in RESULT.md gives the infinite-domain statements, including uniqueness of the decaying bounded boundary-value solution, an explicit spectral square-root, nontrivial coefficients for every phase pair, and a complete discriminant sign analysis. The independent finite-difference backward-equation solver and matrix-eigenvalue solver are implemented in `verify.py`, which reports its deterministic assertion count. The code does not validate originality, priority, or any infinite theorem on the strength of a finite grid.

Run from the package directory using `python verify.py` with Python 3, NumPy and SciPy. Expected execution reports a PASS count; the checker directly asserts agreement rather than merely writing a log. At the double spectral root the proof uses an exact Jordan-polynomial form rather than unstable numerical eigenvectors. No external service, unpublished paper, or separate evidence file is required to replay the numerical checks.
