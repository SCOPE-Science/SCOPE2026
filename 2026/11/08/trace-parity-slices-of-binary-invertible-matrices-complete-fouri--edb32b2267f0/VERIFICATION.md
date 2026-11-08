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

# Verification

Run `python3 verify_trace_GL.py` with a standard Python 3 interpreter. This exhaustively evaluates all \(2^{n^2}\) frequencies for \(n=1,2,3,4\), testing direct matrix ranks and direct Walsh transforms of the trace-restricted indicator against the proposed Gaussian-inversion and spectral identities. All steps use exact integers. The expected terminal line is `TRACE_SLICE_BINARY_GL_EXACT_CHECKS_OK`.

The checker is only a finite consistency check. The analytic proof in `RESULT.md` establishes every dimension and the two infinite-dimensional limits; these are not externally certified.
