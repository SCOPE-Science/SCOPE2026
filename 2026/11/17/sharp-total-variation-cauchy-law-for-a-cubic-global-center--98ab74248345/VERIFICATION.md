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

# Verification of the sharp total-variation law

The claim uses the original physical-time probability distribution of a cubic global-center orbit. Its exact density, conservation law and normalized likelihood ratio appear in `RESULT.md` with all quantifiers. The nonstandard step is the first-order \(L^1\) convergence of the truncated kernel: its interior is dominated by \(u/\sqrt{e^u-1}\) and its endpoint contribution is exponentially small. Evaluating the signed \(L^1\) limit yields the positive Clausen coefficient.

Run `python tools/verify.py` from the package root, using only Python 3's standard library. The checker evaluates the energy-normalized integral at \(L=10,20,40,80,160\), calculates the unique density-ratio crossing and the exact finite-energy total variation by integration, and compares the rescaled values to the predicted coefficient. The expected final marker is `CUBIC_TV_DIAGNOSTICS_OK`. The observed values of \(L\,d_{\mathrm{TV}}\) decrease from about \(0.5586\) at \(L=10\) to \(0.3295\) at \(L=160\), consistent with the proved limit \(0.3230659472\ldots\). These finite tests are not themselves proofs of the infinite limit.

No independent audit or external formal certification has been conducted.
