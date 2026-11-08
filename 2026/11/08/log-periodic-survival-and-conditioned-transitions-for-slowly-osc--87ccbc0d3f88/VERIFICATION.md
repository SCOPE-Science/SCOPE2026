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

# Verification of the log-periodic killed-chain result

The ordinary Python 3 standard-library program `check.py` is bundled alongside the scientific documents. Run `python3 check.py` from the directory containing this document. Its reproducible output begins with `CHECKS_PASSED 63` and prints the exact rational conditioned-response matrix.

The checker independently recomputes the Perron normalization, the mean profile coefficient, the unique centered Poisson solution, and every entry of the two-state response. It also checks row conservation, compares backward-normalized positive matrix products at ten finite horizons with the asserted first-order expansion, and checks stabilization of the survival amplitude after removal of the explicit sine factor. Its longest backward recursion uses a finite terminal horizon of 150000, and its forward normalization diagnostics use horizons up to 16000.

The analytic proof, not the checker, establishes convergence as the terminal horizon tends to infinity, the stated uniform \(O(n^{-2})\) response remainder, the \(O(n^{-1})\) survival error, and failure of ordinary regular variation. Testing a finite set of horizons cannot prove these uniform or infinite statements. Reproducibility uses no external dataset, random seed, downloaded paper, or nonstandard package.
