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

# Verification and limits

**Analytic verification.** Strict ratio invertibility follows from the negative variance identity for the logarithmic attenuation derivative. The nuisance-parameter Poisson Fisher information follows from the explicit two-by-two Schur complement. Its positive pairwise form and leading two-rate term give the exact information-decay exponent. Uniform endpoint bounds and \(C^2\) compact convergence prove eventual uniqueness of the optimal separation. Unknown source-pool amplitudes are shown to permit exact shift aliases.

**Reproducibility.** Extract the adjacent file `verify.py` and run `python3 verify.py` with Python 3 (standard library only). The included script checks an exact fraction example with information \(16/255\), 2,500 heterogeneous-mixture random challenges, source-ratio monotonicity, Schur-complement reconstruction, limiting normalized information, and the special explicit optimum \(\log((3+\sqrt{17})/2)\). Numeric checks support rather than replace the analytic proof.

**Not verified.** Full field applicability, source-mixture calibration, data-based identification in very low copy counts, model discrepancy, external mathematical priority, independent reproduction, and independent audit. The published ecological source itself reports nonmonotone downstream concentration that the restricted idealized loss-only model does not explain.
