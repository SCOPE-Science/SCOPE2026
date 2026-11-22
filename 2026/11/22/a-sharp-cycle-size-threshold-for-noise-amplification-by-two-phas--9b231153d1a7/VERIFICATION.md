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

The theorem is proved in `RESULT.md` by a complete unitary two-cell Fourier reduction, exact singular-value calculation, monotonic-mode selection and a Gram determinant identity. That proof applies to all integer cell counts \(m\ge2\) and all real rates strictly between zero and one.

Run `python verify.py` from a directory containing this file and the checker. Python's standard library suffices. The observed output is `VERIFY_OK 538 checks: exact-rational Gram identity, finite-mode spectral gains, phase boundaries`.

The checks comprise 405 exact-fraction validations of the determinant defect, 132 comparisons of the analytically predicted gain/phase with direct real-vector power iterations across multiple mesh sizes and rate pairs, and the explicit \(m=7\) versus \(m=8\) witness at \(a=2/5,b=3/5\). The numerical iterations test only finite instances, and do not constitute a proof for all sizes or all coefficients. Correctness is based on the analytic proof; no independent mathematical audit has been performed.
