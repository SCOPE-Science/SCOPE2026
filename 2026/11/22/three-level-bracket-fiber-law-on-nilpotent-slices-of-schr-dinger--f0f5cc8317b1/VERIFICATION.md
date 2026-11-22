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

# Verification and reproducibility

The result follows from the five mathematical steps in `RESULT.md`; the direct finite test checks a separate implementation of the original bracket equations. Run `python3 check_schrodinger_fibers.py` with Python 3's standard library. Expected final output: `SCHRODINGER_FULL_NILPOTENT_SLICE_OK`.

The checker enumerates all \(\mathfrak{sl}_2\) matrix pairs giving \(e\), then independently enumerates all one-block Heisenberg inputs, combines the blocks by exact convolution, and compares every prescribed target against the claimed formula. Tested \((q,n)\) pairs are \((3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\), all over prime fields. It checks missing zero-output fibers explicitly, the three-level multiplicities, and the total bracket-pair count. No numerical experiment establishes the arbitrary-extension-field theorem: that follows from the symbolic field-generic argument and quadratic Gauss sums.

No independent mathematical audit has been performed.
