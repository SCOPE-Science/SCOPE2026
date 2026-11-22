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

Run `python verify.py` with Python 3 and SymPy. SciPy is optional for numerical diagnostics. The symbolic verifier re-derives both the invariant-graph Taylor coefficients and the separate quasi-static positive quadratic-root Taylor coefficients, verifies the strict fast-block stability signs, and checks the exact \(1/(4\gamma)\) coefficient discrepancy and the \(n=5/2\) sign-reversal witness. A passing invocation prints `SYMBOLIC_PASS` and `VERIFY_OK`. The included source was run with SymPy/SciPy and passed, including two independent long-time ODE diagnostics.

The center-manifold and scalar inversion proofs in RESULT.md establish the infinite-time limits; no finite numerical trajectory by itself proves an asymptotic. All statements are local to the disease-free correlation state of the deterministic pair approximation. Neither stochastic-network validation nor independent scientific audit has been performed.
