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

The reduction is exact: integer Zak transform fiberization gives multiplication by the sum of the two half-period channel energies. Direct expansion of the two channels yields the even and odd formulas. Affine minimization in \(t=2x(1-x)\) gives global bounds, not a grid approximation. Unit-modulus degeneracy follows from the equality cases of \(|\cos\theta|\le1\) and the arithmetic parity of \(d\). The zero sets have planar measure zero, proving completeness but not frame stability at the singular parameters. The angular normal-form calculation uses isolated nondegenerate maxima at \(\theta\in\{0,\pi\}\) for every fixed odd delay.

The accompanying `CHECK.py` was executed from the candidate files and passed 3,536 finite direct-expansion, extremum, exact special-case and small-perturbation assertions. Requirements: Python 3 and SciPy. Run `python CHECK.py` from the directory containing the file. Grid-based assertions are consistency checks only, not exhaustive optimization or proof of any continuum claim.

Independent audit has not been performed, and priority in older finite-filter Gabor literature cannot be ruled out from the checked sources alone.
