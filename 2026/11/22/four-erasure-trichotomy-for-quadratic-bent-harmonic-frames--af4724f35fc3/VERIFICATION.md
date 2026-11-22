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

Exact finite verification of the displayed theorem used only Python 3 standard-library code. Execute `python verify_direct_walsh.py` and `python verify_symplectic_counts.py`; the output is recorded in `verify_direct_walsh.out` and `verify_symplectic_counts.out`. The former calculates actual Fourier/Walsh character sums and all integer Gram characteristic polynomials for \(m=2\); the latter enumerates all four-subsets using symplectic polarization at \(m=2,3\). Both passed.

The proof for all \(m\ge2\) is symbolic and contained in `RESULT.md`: pairwise Walsh factorization, sign switching, two independent linear functionals, and exact ordered-tuple counting. Finite checks do not by themselves establish the infinite theorem. The comparison literature already contains the sixty four-column dependencies at \(m=2\), which are not a novel subclaim. No external independent validation has been performed.
