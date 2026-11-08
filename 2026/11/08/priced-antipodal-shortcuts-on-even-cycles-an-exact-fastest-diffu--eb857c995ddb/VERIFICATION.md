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

# Verification instructions and bounds

Run `python3 verify.py` with the accompanying source file in the same directory. Only the Python standard library is required. The reproduced output is `VERIFY_OK 641`.

The verifier includes exact-rational eigenvector checks for the six-vertex boundary instance (used only as a consistency test), independent Jacobi diagonalizations for \(m=3,\ldots,12\) in several price regimes, randomly selected heterogeneous edge conductances assessed against the two Fourier bounds, and long-cycle checks for the stated asymptotic rates and budget fractions.

Numerical tolerances and sample sizes are explicit in the source. The proof in RESULT.md independently establishes the claims for all real \(B>0\), \(c>0\) and integers \(m\ge4\); numerical tests do not prove infinite-domain correctness. The comparison with unindexed literature is incomplete, and publication priority has not been independently established.
