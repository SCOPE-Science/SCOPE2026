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

The standalone `verify.py` script requires Python 3 with SymPy. Run `python verify.py` in the directory containing this file. It expands the two deterministic branches of the Bernoulli covariance update, checks the exact residual cross-moment closure, matrix entries, determinant and Schur–Jury identities, and enumerates short branches using rational probabilities and stepsizes to compare with moment recurrences. `verification_output.txt` contains a successful run. The proof of stability for every admissible real parameter and nonconvergence outside the window is analytical in `RESULT.md`, not an inference from the finite tests. No independent audit has been performed.
