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

Run `python3 verify.py` using Python 3 with no third-party dependencies. The program tests all \(3^n\) configurations for every length \(1\le n\le10\), checking the direct and lifted synchronous updates agree modulo three at each update, initial and propagated 1-Lipschitz bounds, monotonicity, the constant ceiling, the two deterministic time bounds, termination at a uniform height, and the exact maximum \(n+1\). A separately written integer-encoded transition checks the complete extinction-time histograms for lengths \(1\le n\le9\). The actual standard output from one replay is embedded in `verification_output.txt`.

**Limits:** finite exhaustive tests do not verify the infinite convergence claim; this follows analytically from the displayed deterministic inequality, the independent random-walk increment representation, the functional central limit theorem, argmax continuity, and the classical arcsine law. The test program contains no theorem prover. No independent scientific review has been performed.
